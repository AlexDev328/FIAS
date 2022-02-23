from typing import List, Optional

import databases
import sqlalchemy
from fastapi import FastAPI

import ormar
from app.db.models.base_class import database


app = FastAPI()
app.state.database = database



@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


from app.db.models.base_object import *
from xml.etree import ElementTree as ET




'''
p = FileConsumer()
p.process_file("/run/media/aidev/Data/Проекты/ФИАС/FIAS/01/AS_ADDR_OBJ_20220221_29b5b8fb-4081-46d4-a898-36bcd31e59ed.XML")

'''

from app.update_manager.file_consumer import FileConsumer



@app.get("/test")
async def root():
    #a = {'id': '4683', 'object_id': '4252', 'object_guid': '98c67d0a-c63d-4d5e-a5f6-67bcc204ba0c', 'update_date': '2018-07-06', 'start_date': '2018-07-04', 'end_date': '2079-06-06', 'is_actual': '1', 'is_active': '1', 'name': 'Пограничная', 'type_name': 'ул', 'level': '8'}
    p = FileConsumer()
    # p.process_file("/run/media/aidev/Data/Проекты/ФИАС/FIAS/01/AS_ADDR_OBJ_20220221_29b5b8fb-4081-46d4-a898-36bcd31e59ed.XML")
    await p.process_file(
        "/run/media/aidev/Data/Проекты/ФИАС/FIAS/01/types/AS_ROOM_TYPES_20220221_48ba6d15-6faa-44ea-8439-7b314cc6d5f7.XML")
    return {"message": "ok"}
