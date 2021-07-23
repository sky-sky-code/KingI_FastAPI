from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL

from kingit_api.db import Base

class TC(Base):
    __tablename__ = 'TC'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(length=255))
    status = Column(String(length=255))
    count_pavilions = Column(Integer)
    city = Column(String)
    cost = Column(DECIMAL(precision=2))
    add_value_rito = Column(DECIMAL(precision=2))
    storyes = Column(Integer)
    photo = Column(String(255))

class Worker(Base):
    __tablename__ = 'Worker'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    role = Column(String(255))
    phone = Column(String(20))
    gender = Column(String)
    photo = Column(String)

class Pavilion(Base):
    __tablename__ = 'Pavilion'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title_TC = Column(String(255))
    number_pavilion = Column(String(255))
    floor = Column(Integer)
    status = Column(String(255))
    area = Column(Integer)
    cost_sqm = Column(DECIMAL(precision=2))
    add_value_rito = Column(DECIMAL(precision=2))

class Tenant(Base):
    __tablename__ = 'Tenant'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title_phone = Column(String)
    phone = Column(String(20))
    address = Column(String)

class Rent(Base):
    __tablename__ = 'Rent'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title_TC = Column(String(255))
    number_pavilion = Column(String(length=3))
    status = Column(String(255))
    start_rent = Column(DateTime)
    finish_rent = Column(DateTime)
    ID_tenant = Column(Integer, ForeignKey('Tenant.id'))
    ID_worker = Column(Integer, ForeignKey('Worker.id'))