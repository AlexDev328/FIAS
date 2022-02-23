import databases
import ormar
import sqlalchemy

from app.core.config import sqlalchemy_url

metadata = sqlalchemy.MetaData()
database = databases.Database(sqlalchemy_url)

engine = sqlalchemy.create_engine(sqlalchemy_url)


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
