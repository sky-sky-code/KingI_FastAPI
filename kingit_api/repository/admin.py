from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from kingit_api import models, schemas
import shutil


def save_video(photo, file_name):
    with open(file_name, 'wb') as buffer:
        shutil.copyfileobj(photo.file, buffer)

def get_worker(db: Session):
    workers = db.query(models.Worker).all()
    return workers

def admin_add_worker(
        id: int,
        full_name: str,
        email: str,
        password: str,
        role: str,
        phone: str,
        gender: str,
        photo: UploadFile,
        db: Session,
):
    file_name = f'media/worker/{photo.filename}'
    save_video(photo, file_name)
    info = schemas.Worker(id=id, full_name=full_name, email=email, password=password,
                          role=role, phone=phone, gender=gender, photo=file_name)
    new_worker = models.Worker(**info.dict())
    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)
    return new_worker

def worker_update(
        id: int,
        full_name: str,
        email: str,
        password: str,
        role: str,
        phone: str,
        gender: str,
        photo: UploadFile,
        db: Session
):
    worker = db.query(models.Worker).filter(models.Worker.id == id).first()
    if not worker:
        raise HTTPException(status_code=404,
                            detail=f'Worker with id {id} not found')
    shutil.rmtree(worker.photo)
    file_name = f'media/worker/{photo.filename}'
    save_video(photo, file_name)
    tc = db.query(models.Worker).filter(models.Worker.id == id)
    tc.update({'full_name': full_name, 'email': email,
               'password': password, 'role': role, 'phone': phone,
               'gender': gender})
    db.commit()
    return 'update'

def destroy_worker(id: int, db: Session):
    worker = db.query(models.TC).filter(models.Worker.id == id)
    if not worker.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    worker.delete(synchronize_session=False)
    db.commit()
    return 'done'

