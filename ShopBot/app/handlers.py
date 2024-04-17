from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
import os
import app.database.requests as rq
from config import ADMIN_ID
router = Router()

class Registr(StatesGroup):
    name = State()
    age = State()
    email = State()
    city = State()
    number = State()

    
@router.message(F.text == 'Каталог')
async def catalog(message:Message):
    await message.answer('Выберете марку кроссовок',
                                     reply_markup = await kb.categories())



    
    
@router.message(CommandStart())
async def registr(message:Message, state:FSMContext):
    await state.set_state(Registr.name)
    await message.answer('Пройдите регистрацию!')
    await message.answer('Введите ваше имя')
    
    
@router.message(Registr.name)
async def registr_name(message:Message, state:FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Registr.age)
    await message.answer('Введите ваш возвраст')
    
@router.message(Registr.age)
async def registr_age(message:Message, state:FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(Registr.city)
    await message.answer('Введите ваш город')
    
@router.message(Registr.city)
async def registr_age(message:Message, state:FSMContext):
    await state.update_data(city = message.text)
    await state.set_state(Registr.email)
    await message.answer('Введите вашу электронную почту')
    
@router.message(Registr.email)
async def registr_age(message:Message, state:FSMContext):
    await state.update_data(email = message.text)
    await state.set_state(Registr.number)
    await message.answer('Введите ваш номер телефона', reply_markup=kb.get_number)
    

    
@router.message(Registr.number, F.contact)
async def registr_number(message:Message, state:FSMContext):
    await state.update_data(number = message.contact.phone_number)
    await message.answer('Вы успешно зарегестрировались!')
    if message.from_user.id == 1581212641:
        await message.answer('Вы вошли в админ-панель', reply_markup=kb.main_admin)
    else:
        await message.answer(text='Привет!\nЭто магазин кроссовок,\nВыберете меню ниже', reply_markup=kb.main)

    
    
@router.message(F.text == 'Личный кабинет')
async def lk(message:Message,state:FSMContext):
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш возвраст: {data["age"]}\nНомер: {data["number"]}\nГород: {data["city"]}\nЭлектронная почта {data["email"]}')




@router.message(F.text == 'Админ-панель')
async def admin(message:Message):
    if message.from_user.id == 1581212641:
        await message.answer(f'Вы администратор!', reply_markup=kb.admin_panel)


@router.callback_query(F.data.startswith('category_'))
async def category(callback:CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберете товар',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))
    
@router.callback_query(F.data.startswith('item_'))
async def category(callback:CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\nОписание:{item_data.description}\nЦена{item_data.price}$',
                                  reply_markup=kb.gl)
    
@router.callback_query(F.data == 'gl')
async def gl(callback:CallbackQuery):
    await callback.message.answer(text='Привет!\nЭто магазин кроссовок,\nВыберете меню ниже', reply_markup=kb.main)