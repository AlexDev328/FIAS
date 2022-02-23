import ormar
from datetime import date
from app.db.models.base_class import MainMeta


class FiasObjectAbstract(ormar.Model):
    class Meta(MainMeta):
        abstract = True

    id: int = ormar.Integer(primary_key=True)
    fias_id: int = ormar.Integer()
    fias_object_id: int = ormar.BigInteger(index=True)
    fias_object_guid: str = ormar.UUID()
    update_date: date = ormar.Date()
    start_date: date = ormar.Date()
    end_date: date = ormar.Date()
    is_actual: bool = ormar.Boolean()
    is_active: bool = ormar.Boolean()


class ADDRObject(FiasObjectAbstract):
    class Meta(MainMeta):
        pass
    name: str = ormar.String(max_length=250)
    type_name: str = ormar.String(max_length=50)
    level: int = ormar.Integer()


class HouseObject(FiasObjectAbstract):
    class Meta(MainMeta):
        pass
    house_num: str = ormar.String(max_length=250)
    add_num_1: str = ormar.String(max_length=250)
    add_num_2: str = ormar.String(max_length=250)
    house_type: int = ormar.Integer()
    add_type_1: int = ormar.Integer()
    add_type_2: int = ormar.Integer()


class Types:
    class Meta(MainMeta):
        abstract = True

    id: int = ormar.Integer()
    name: str = ormar.String(max_length=250)
    desc: str = ormar.String(max_length=250)
    short_name: str = ormar.String(max_length=250)
    update_date: date = ormar.Date()
    start_date: date = ormar.Date()
    end_date: date = ormar.Date()
    is_active: bool = ormar.Boolean()

class RoomTypes(Types):
    class Meta(MainMeta):
        pass

class ADDRObjectTypes(Types):
    class Meta(MainMeta):
        pass

class HouseTypes(Types):
    class Meta(MainMeta):
        pass

class AddHouseTypes(Types):
    class Meta(MainMeta):
        pass

class AppartemntsTypes(Types):
    class Meta(MainMeta):
        pass

class RoomTypes(Types):
    class Meta(MainMeta):
        pass