import databases
import ormar
import sqlalchemy


metadata = sqlalchemy.MetaData()
database = databases.Database("postgresql://fias:3285@127.0.0.1:5432/fias")

engine = sqlalchemy.create_engine("postgresql://fias:3285@127.0.0.1:5432/fias")


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
