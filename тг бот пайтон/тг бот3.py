from telebot import*
bot = telebot.TeleBot('7076474920:AAHeg_NJTEgZMZ1O2Sv8blNTkmN0zTnB6Mw')

from sqlalchemy import BigInteger, String, Column, ForeignKey, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

engine = create_async_engine('sqlite+aiosqlite:///db.sqlite3')
async_session = AsyncSession(engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger)

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(25))

class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    description = Column(String(120))
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)