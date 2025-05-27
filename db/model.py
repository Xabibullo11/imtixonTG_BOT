from sqlalchemy import create_engine, DECIMAL, Text, ForeignKey, BIGINT
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column, relationship, sessionmaker
from sqlalchemy.sql import func

from environment.utils import Env

DB_URL = Env().bot.DB_URL

engine = create_engine(DB_URL)

class Base(DeclarativeBase):
    id : Mapped['int'] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"

class User(Base):
    name: Mapped[str]
    location: Mapped[str]
    contact: Mapped[str]

metadata = Base.metadata

Session = sessionmaker(bind=engine)
session = Session()