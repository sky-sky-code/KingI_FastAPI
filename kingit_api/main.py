from fastapi import FastAPI
from kingit_api.routers import admin, managerC
from kingit_api.db import engine

from kingit_api import models

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(managerC.router)
app.include_router(admin.router)
