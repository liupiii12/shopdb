from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='💵Буст рангов'),
        KeyboardButton(text='📜Техподдержка')
    ],
    [
        KeyboardButton(text='🚀Мета'),
        KeyboardButton(text='💹Как апать ранги'),
    ]
],resize_keyboard=True,
input_field_placeholder='Выберете пункт меню')


rang = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='⭐25 ранг', callback_data= 'low'),
        InlineKeyboardButton(text='🚀30 ранг', callback_data='midl')
    ],
    [
        InlineKeyboardButton(text='🔥35 ранг', callback_data='ower')
    ],
    [
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])
 
regim = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='💯Соло шд',url='https://youtu.be/4AUSHfQWUmQ?si=XHSYE8CiQDXGcRTs'),
        InlineKeyboardButton(text='💥Дуо шд',url ='https://youtu.be/BIroKFLBZM4?si=Pe5gStvuSMx9_2f4'),
        InlineKeyboardButton(text='💪🏽Броубол',url ='https://youtu.be/aqJt3UgKY0E?si=JwGZQs3tLg124KWr')
    ],
    [
        InlineKeyboardButton(text='🔥Другие 3 на 3 режимы', url='https://youtu.be/CbLhUfhZ4P0?si=EhAepsVtDCKCXN3H')
    ],
    [
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])



meta = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='💥Соло шд',callback_data='mhd'),
        InlineKeyboardButton(text='🔥Дуо шд', callback_data='mdhd')
    ],
    [
        InlineKeyboardButton(text='👑Ранговый бой', callback_data='rb'),
        InlineKeyboardButton(text='💎3 на 3', callback_data='mbb')
    ],
    [
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад',callback_data='back'),
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])

back1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад',callback_data='3back'),
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])

back2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад',callback_data='4back'),
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])

regim2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = '🎯Нокаут', callback_data='nk1'),
        InlineKeyboardButton(text='💪🏽Броубол', callback_data='bb1')
    ],
    [
        InlineKeyboardButton(text='👑Захват кристалов', callback_data='gm1'),
        InlineKeyboardButton(text='🔥Горячая зона', callback_data='gz1')
    ],
    [
        InlineKeyboardButton(text='💎Ограбление', callback_data='gr1')
    ],
    [
        InlineKeyboardButton(text='Назад',callback_data='5back'),
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])


back3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад',callback_data='6back'),
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])


bust = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Написать нам',url = 'https://t.me/XR_bs'),
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])

teh = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Написать нам', url='https://t.me/XR_bs'),
        InlineKeyboardButton(text='В главное меню',callback_data='glm')
    ]
])