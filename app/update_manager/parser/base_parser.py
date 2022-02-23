from _elementtree import Element
from typing import Generic, TypeVar, Type

from app.update_manager.parser.data_classes import *

T = TypeVar("T", bound=AbstractFiasObject)


class BaseParser(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def parse(self, element: Element) -> T:
        attributes = {}
        for entity_key, xml_key in self.model.get_attribute_map():
            value = element.attrib.get(xml_key)
            attributes[entity_key] = value
        res = self.model(**attributes)
        print(attributes)
        return res


class FiasObjectParser(BaseParser[FiasObject]):
    def __init__(self):
        super().__init__(FiasObject)


class HouseParser(BaseParser[House]):
    def __init__(self):
        super().__init__(House)


class SteadParser(BaseParser[Stead]):
    def __init__(self):
        super().__init__(Stead)


class RoomParser(BaseParser[Room]):
    def __init__(self):
        super().__init__(Room)


class ApartmentParser(BaseParser[Apartment]):
    def __init__(self):
        super().__init__(Apartment)


class CarPlaceParser(BaseParser[CarPlace]):
    def __init__(self):
        super().__init__(CarPlace)
