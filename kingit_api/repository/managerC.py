from decimal import Decimal

from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from kingit_api import models, schemas
import shutil


def save_photo(photo, file_name):
    with open(file_name, 'wb') as buffer:
        shutil.copyfileobj(photo.file, buffer)

def get_all_tc(db: Session):
    tc = db.query(models.TC).all()
    return tc

def search_tc(title: str, status: str, db: Session):
    list_tc = db.query(models.TC).filter(models.TC.title == title,
                                         models.TC.status == status).all()
    return list_tc

def get_pavilion(db: Session):
    pavilions = db.query(models.Pavilion).all()
    return pavilions

def search_pavilion(floor: int, status: str, db: Session):
    pavilions = db.query(models.Pavilion).filter(models.Pavilion.floor == floor,
                                                 models.Pavilion.status == status).all()
    return pavilions

def create_tc(
        title: str,
        status: str,
        count_pavilions: int,
        city: str,
        cost: Decimal,
        add_value_rito: Decimal,
        storyes: int,
        photo: UploadFile,
        db: Session,
):
    file_name = f'media/tc/{photo.filename}'
    save_photo(photo, file_name)
    info = schemas.TCBase(id=2, title=title, status=status, count_pavilions=count_pavilions,
                          city=city, cost=cost, add_value_rito=add_value_rito, storyes=storyes, photo=file_name)
    new_tc = models.TC(**info.dict())
    db.add(new_tc)
    db.commit()
    db.refresh(new_tc)
    return new_tc

def update_tc(
        id: int,
        title: str,
        status: str,
        count_pavilions: int,
        city: str,
        cost: Decimal,
        add_value_rito: Decimal ,
        storyes: int,
        photo: UploadFile,
        db: Session,
):
    tc = db.query(models.TC).filter(models.TC.id == id).first()
    if not tc:
        raise HTTPException(status_code=404,
                            detail=f'TC with id {id} not found')

    shutil.rmtree(tc.photo)
    file_name = f'media/tc/{photo.filename}'
    save_photo(photo, file_name)
    tc = db.query(models.TC).filter(models.TC.id == id)
    tc.update({'id': id, 'title': title, 'status': status, 'count_pavilions': count_pavilions,
               'city': city, 'cost': cost, 'add_value_rito': add_value_rito, 'storyes': storyes, 'photo': file_name})
    db.commit()
    return 'update'

def destroy_tc(id: int, db: Session):
    tc = db.query(models.TC).filter(models.TC.id == id)
    if not tc.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'TC with id {id} not found')
    tc.delete(synchronize_session=False)
    db.commit()
    return 'done'