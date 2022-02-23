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
from app.update_manager.parser.base_parser import FiasObjectParser, HouseParser, BaseParser


class FileConsumer:

    def process_file(self, xml_file: str):
        prefix = self.get_file_prefix(xml_file)
        parser = self.get_file_parser(prefix)
        tree = ET.ElementTree(file=xml_file)
        root = tree.getroot()

        for child in root:
            entity = parser.parse(child)
            print(entity)
            print(type(dict(entity)))
            a = ADDRObject(dict(entity))
            a.save()

    def get_file_prefix(self, filename: str) -> str:
        # todo написать с регуляркой!
        idx = filename.rfind('_')
        tmp = filename[:idx - 9]
        idx = tmp.rfind('/')
        if idx > 0:
            tmp = tmp[idx + 1:]
        return tmp

    def get_file_parser(self, prefix: str) -> BaseParser:
        match prefix:
            case "AS_ADDR_OBJ":
                return FiasObjectParser()
            case "AS_HOUSES":
                return HouseParser()
            case _:
                raise RuntimeError("No parser found for file with prefix " + prefix)


'''
p = FileConsumer()
p.process_file("/run/media/aidev/Data/Проекты/ФИАС/FIAS/01/AS_ADDR_OBJ_20220221_29b5b8fb-4081-46d4-a898-36bcd31e59ed.XML")

'''





@app.get("/test")
async def root():
    #a = {'id': '4683', 'object_id': '4252', 'object_guid': '98c67d0a-c63d-4d5e-a5f6-67bcc204ba0c', 'update_date': '2018-07-06', 'start_date': '2018-07-04', 'end_date': '2079-06-06', 'is_actual': '1', 'is_active': '1', 'name': 'Пограничная', 'type_name': 'ул', 'level': '8'}
    p = FileConsumer()
    p.process_file(
        "/run/media/aidev/Data/Проекты/ФИАС/FIAS/01/AS_ADDR_OBJ_20220221_29b5b8fb-4081-46d4-a898-36bcd31e59ed.XML")
    return {"message": "ok"}
