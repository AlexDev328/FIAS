from attrs import define


@define
class AbstractFiasObject:
    id: int
    object_id: int
    object_guid: str
    update_date: str
    start_date: str
    end_date: str
    is_actual: bool
    is_active: bool

    def import_attributes(self, attributes):
        for attr in attributes:
            setattr(self, attr[0], attr[1])

    @classmethod
    def get_attribute_map(cls):
        return [
            ("id", "ID"),
            ("object_id", "OBJECTID"),
            ("object_guid", "OBJECTGUID"),
            ("update_date", "UPDATEDATE"),
            ("start_date", "STARTDATE"),
            ("end_date", "ENDDATE"),
            ("is_actual", "ISACTUAL"),
            ("is_active", "ISACTIVE")
        ]


@define
class FiasObject(AbstractFiasObject):
    name: str
    type_name: str
    level: int

    @classmethod
    def get_attribute_map(cls):
        return super().get_attribute_map() + [
            ("name", "NAME"),
            ("type_name", "TYPENAME"),
            ("level", "LEVEL"),
        ]


@define
class House(AbstractFiasObject):
    house_num: str
    add_num_1: str
    add_num_2: str
    house_type: str
    add_type_1: str
    add_type_2: str

    @classmethod
    def get_attribute_map(cls):
        return super().get_attribute_map() + [
            ("house_num", "HOUSENUM"),
            ("add_num_1", "ADDNUM1"),
            ("add_num_2", "ADDNUM2"),
            ("house_type", "HOUSETYPE"),
            ("add_type_1", "ADDTYPE1"),
            ("add_type_2", "ADDTYPE2"),
        ]


@define
class Room(AbstractFiasObject):
    room_number: str
    room_type: str

    @classmethod
    def get_attribute_map(cls):
        return super().get_attribute_map() + [
            ("room_number", "ROOMNUMBER"),
            ("room_type", "ROOMTYPE"),
        ]


@define
class Apartment(AbstractFiasObject):
    number: str
    apartment_type: int


    @classmethod
    def get_attribute_map(cls):
        return super().get_attribute_map() + [
            ("number", "NUMBER"),
            ("apartment_type", "APARTTYPE")
        ]


@define
class CarPlace(AbstractFiasObject):
    number: str

    @classmethod
    def get_attribute_map(cls):
        return super().get_attribute_map() + [
            ("number", "NUMBER")
        ]


@define
class Stead(AbstractFiasObject):
    number: str

    @classmethod
    def get_attribute_map(cls):
        return super().get_attribute_map() + [
            ("number", "NUMBER")
        ]


@define
class BaseTypes:
    id: int
    name: str
    desc: str
    short_name: str
    update_date: str
    start_date: str
    end_date: str
    is_active: bool

    @classmethod
    def get_attribute_map(cls):
        return [
            ("id", "ID"),
            ("name", "NAME"),
            ("desc", "DESC"),
            ("short_name", "SHORTNAME"),
            ("update_date", "UPDATEDATE"),
            ("start_date", "STARTDATE"),
            ("end_date", "ENDDATE"),
            ("is_active", "ISACTIVE"),
        ]
@define

class AddrObject_Types(BaseTypes):
    pass


@define
class Room_Types(BaseTypes):
    pass


@define
class House_Types(BaseTypes):
    pass


@define
class AditionalHouseInfo_Types(BaseTypes):
    pass


@define
class Appartment_Types(BaseTypes):
    pass
