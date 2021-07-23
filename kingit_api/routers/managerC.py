from decimal import Decimal
from typing import List
from fastapi import APIRouter, Depends, status, File, Form, UploadFile
from sqlalchemy.orm import Session
from kingit_api.db import get_db
from kingit_api.repository import managerC

from kingit_api import schemas

router = APIRouter(
    tags=['ManagerC']
)

@router.get('/api/managerC', response_model=List[schemas.TCBase])
def all_tc(db: Session = Depends(get_db)):
    return managerC.get_all_tc(db)


@router.get('/api/managerC/search_{title}_status', response_model=List[schemas.TCBase])
def search_tc(
    title: str,
    status: str,
    db: Session = Depends(get_db),
):
    return managerC.search_tc(title, status, db)

@router.get('/api/managerC/pavilion', response_model=List[schemas.Pavilion])
def get_pavilion(db: Session = Depends(get_db)):
    return managerC.get_pavilion(db)


@router.get('/api/managerC/pavilion/search_{floor}_{status}', response_model=List[schemas.Pavilion])
def search_pavilion(
        floor: int,
        status: str,
        db: Session = Depends(get_db)
):
    return managerC.search_pavilion(floor, status, db)


@router.post('/api/managerC/add', response_model=schemas.TCBase, status_code=status.HTTP_201_CREATED)
def create_tc(
        title: str = Form(...),
        status: str = Form(...),
        count_pavilions: int = Form(...),
        city: str = Form(...),
        cost: Decimal = Form(...),
        add_value_rito: Decimal = Form(...),
        storyes: int = Form(...),
        photo: UploadFile = File(...),
        db: Session = Depends(get_db),
):
    return managerC.create_tc(title, status, count_pavilions,
                              city, cost, add_value_rito, storyes,
                              photo, db)


@router.put('/api/managerC/edit/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_tc(
        id: int,
        title: str = Form(...),
        status: str = Form(...),
        count_pavilions: int = Form(...),
        city: str = Form(...),
        cost: Decimal = Form(...),
        add_value_rito: Decimal = Form(...),
        storyes: int = Form(...),
        photo: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    return managerC.update_tc(id, title, status, count_pavilions,
                              city, cost, add_value_rito, storyes,
                              photo, db)


@router.delete('/api/managerC/del/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_tc(id: int, db: Session = Depends(get_db)):
    return managerC.destroy_tc(id, db)