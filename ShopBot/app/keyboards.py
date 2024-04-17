from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_categories,get_category_item
main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Каталог'),
        KeyboardButton(text='Корзина')
    ],
    [
        KeyboardButton(text='О нас'),
        KeyboardButton(text='Личный кабинет')
    ]
], resize_keyboard=True)


pay = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Купить', callback_data='pay')
    ],
    [
        InlineKeyboardButton(text='На главную', callback_data='gl')
    ]
])

get_number = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Отправить номер',request_contact=True)
    ]
],resize_keyboard=True)

gl = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Главное меню', callback_data='gl')
    ]
])


main_admin = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Каталог'),
        KeyboardButton(text='Корзина')
    ],
    [
        KeyboardButton(text='О нас'),
        KeyboardButton(text='Личный кабинет'),
        KeyboardButton(text='Админ-панель')
    ]
], resize_keyboard=True)


admin_panel = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Добавить товар'),
        KeyboardButton(text='Удалить товар')
    ],
    [
        KeyboardButton(text = 'Сделать рассылку')
    ]
],resize_keyboard=True )

async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name ,callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='gl'))
    return keyboard.adjust(2).as_markup()


#async def items(category_id):
#    all_items = await get_category_item(category_id)
#    keyboard = InlineKeyboardBuilder()
#    for item in all_items:
#        keyboard.add(InlineKeyboardButton(text=item.name ,callback_data=f'item_{item.id}'))
#    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='gl'))
#    return keyboard.adjust(2).as_markup()

async def items(category_id):
    all_items = await get_category_item(int(category_id))
    if not all_items:
        return None  # Обработка случая, когда нет элементов для указанной категории

    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='gl'))
    return keyboard.adjust(2).as_markup()