from xml.etree import ElementTree as ET
from app.update_manager.parser.base_parser import FiasObjectParser, HouseParser, BaseParser
from app.db.models.base_object import

class FileConsumer:

    def process_file(self, xml_file: str):
        prefix = self.get_file_prefix(xml_file)
        parser = self.get_file_parser(prefix)
        tree = ET.ElementTree(file=xml_file)
        root = tree.getroot()

        for child in root:
            entity = parser.parse(child)

    def get_file_prefix(self, filename: str) -> str:
        # todo написать с регуляркой!
        idx = filename.rfind('_')
        tmp = filename[:idx - 9]
        idx = tmp.rfind('/')
        if idx > 0:
            tmp = tmp[idx + 1:]
        return tmp

    def get_file_parser_and_db_model(self, prefix: str) -> BaseParser:
        match prefix:
            case "AS_ADDR_OBJ":
                return FiasObjectParser()
            case "AS_HOUSES":
                return HouseParser()
            case _:
                raise ValueError("No parser found for file with prefix " + prefix)



p = FileConsumer()
p.process_file("/run/media/aidev/Data/Проекты/ФИАС/FIAS/01/AS_ADDR_OBJ_20220221_29b5b8fb-4081-46d4-a898-36bcd31e59ed.XML")
