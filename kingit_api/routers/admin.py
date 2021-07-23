from typing import List
from fastapi import APIRouter, Depends, status, File, Form, UploadFile
from sqlalchemy.orm import Session
from kingit_api.db import get_db
from kingit_api.repository import admin

from kingit_api import schemas

router = APIRouter(
    tags=['Admin']
)

@router.get('/api/admin', response_model=List[schemas.Worker])
def get_worker(db: Session = Depends(get_db)):
    return admin.get_worker(db)


# TODO сделать admin search

@router.post('/api/admin/add', response_model=schemas.Worker)
def admin_add(
        id: int = Form(...),
        full_name: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        role: str = Form(...),
        phone: str = Form(...),
        gender: str = Form(...),
        photo: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    return admin.admin_add_worker(id, full_name, email, password, role, phone, gender, photo, db)


@router.put('/api/admin/edit/{id}', status_code=status.HTTP_202_ACCEPTED)
def worker_update(
        id: int,
        full_name: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        role: str = Form(...),
        phone: str = Form(...),
        gender: str = Form(...),
        photo: UploadFile = File(...),
):
    return admin.worker_update(id, full_name, email, password, role,
                               phone, gender, photo)


@router.delete('/api/admin/del/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_worker(id: int, db: Session = Depends(get_db)):
    return admin.destroy_worker(id, db)