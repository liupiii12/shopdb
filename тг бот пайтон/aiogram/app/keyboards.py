from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder



main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Каталог', callback_data='catalog'),
    ],
    [
        InlineKeyboardButton(text='Корзина', callback_data='basket'),
        InlineKeyboardButton(text='Контакты', callback_data='contacts')
    ]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Youtube', url= 'https://youtube.com')
    ]
])


cars = ['Tesla', 'Mercedes','BMW','Toyota']

async def inline_cars():
    Keyboard = InlineKeyboardBuilder()
    for car in cars:
        Keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com'))
    return Keyboard.adjust(1).as_markup()

