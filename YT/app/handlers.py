from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
router = Router()

@router.message(CommandStart())
async def photo_get(message:Message):
    await message.answer_photo(photo='AgACAgIAAxkBAANCZg-wSy71c-6155P4sM-BCwisjA0AAhTYMRsneYBITb09Wwhic0QBAAMCAAN3AAM0BA', caption= 'Привет, выберете меню ниже', reply_markup=kb.main)
@router.message(F.text == '💹Как апать ранги')
async def puh(message:Message):
    await message.answer(text='❗Выберете ранг который хотите апнуть❗', reply_markup=kb.regim)
    
    

@router.message(F.text == '🚀Мета')
async def meta(message:Message):
    await message.answer_photo(photo='https://catherineasquithgallery.com/uploads/posts/2021-02/1613040611_177-p-oranzhevii-fon-bravl-stars-203.png',caption='❗Для какого режима хотите узнать мету❗',reply_markup=kb.meta)

@router.callback_query(F.data == 'rb')
async def rb(callback: CallbackQuery):
    await callback.answer('Вы выбрали мета в ранговом бою')
    await callback.message.answer_photo(photo='https://i.ytimg.com/vi/ABdG6KgVAlA/maxresdefault.jpg',
                                        caption='''🔶Мета для рангового боя🔶 \n1️⃣Чарли\n2️⃣Корделиус\n3️⃣Анжело\n4️⃣Спайк\n5️⃣Нани\n6️⃣Леон\n7️⃣Амбер\n8️⃣Бель\n🔷Вот список самых лучших персонажей для рангового боя🔷''',
                                        reply_markup=kb.back)

    
@router.callback_query(F.data == 'back')
async def back(callback : CallbackQuery):
    await callback.answer('')
    await callback.message.answer('❗В каком режиме вы хотите узнать мету❗',reply_markup=kb.meta)
    
@router.callback_query(F.data == 'glm')
async def glm(callback:CallbackQuery):
    await callback.message.answer_photo(photo='AgACAgIAAxkBAANCZg-wSy71c-6155P4sM-BCwisjA0AAhTYMRsneYBITb09Wwhic0QBAAMCAAN3AAM0BA', caption= 'Привет, выберете меню ниже', reply_markup=kb.main)
    


@router.callback_query(F.data == 'mhd')
async def mhd1(calback:CallbackQuery):
    await calback.answer('')
    await calback.message.answer_photo(photo='https://i.ytimg.com/vi/7Y3ka65pzQA/maxresdefault.jpg', 
                                       caption='🔶Топ персонажей для соло шд🔶\n1️⃣Корделиус\n2️⃣Пёрл\n3️⃣Пайпер\n4️⃣Анджело\n5️⃣Мелоди\n6️⃣Шелли\n7️⃣Базз\n8️⃣Даг\n9️⃣Мэг\n🔷Это лучшие бойцы для соло шд🔷',
                                       reply_markup=kb.back1)
    
@router.callback_query(F.data == '3back')
async def back3(calback:CallbackQuery):
    await calback.answer('')
    await calback.message.answer('❗В каком режиме вы хотите узнать мету❗',reply_markup=kb.meta)
    
@router.callback_query(F.data == 'mdhd')
async def mdhd(calback:CallbackQuery):
    await calback.answer('')
    await calback.message.answer_photo(photo='https://i.ytimg.com/vi/iqfHisWxJaM/maxresdefault.jpg',caption='1️⃣Корделиус\n2️⃣Шелли\n3️⃣Эдгар\n4️⃣Анджело\n5️⃣Базз\n6️⃣Леон\n7️⃣Пайпер\n8️⃣Кит\n🔷Это топ лучших бойцов для дуо шд🔷',
                                       reply_markup=kb.back2)
    
@router.callback_query(F.data == '4back')
async def back4(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer('❗В каком режиме вы хотите узнать мету❗',reply_markup=kb.meta)
    
@router.callback_query(F.data == 'mbb')
async def mbb(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer('❗Выберете режим❗', reply_markup=kb.regim2)
    
@router.callback_query(F.data == 'gr1')
async def gr1(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(photo='https://i.ytimg.com/vi/BySxcbcK18E/maxresdefault.jpg', 
                                        caption='1️⃣Чак\n2️⃣Кольт\n3️⃣Коллет\n4️⃣Джеси\n5️⃣Спайк\n6️⃣Нита\n7️⃣Брок\n8️⃣Бык\n❗Это топ бойцов для ограбления❗',
                                        reply_markup=kb.back3)

@router.callback_query(F.data == '6back')
async def back6(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer('❗Выберете режим❗', reply_markup=kb.regim2)
    
@router.callback_query(F.data == 'nk1')
async def nk1(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(photo='https://i.ytimg.com/vi/GEXetkXy3dc/maxresdefault.jpg', 
                                        caption='1️⃣Пёрл\n2️⃣Джин\n3️⃣Спраут\n4️⃣Пайпер\n5️⃣Мэг\n6️⃣Анжело\n7️⃣Леон\n8️⃣Нани\n❗Это топ бойцов для нокаута❗',
                                        reply_markup=kb.back3)
    
@router.callback_query(F.data == 'gm1')
async def gm1(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(photo='https://avatars.dzeninfra.ru/get-zen_doc/4398042/pub_602e948c3ad6ee787c2093b6_602f5d116ce3da78042a6e79/scale_1200', 
                                        caption='1️⃣Пайпер - Вагонетка без тормозов\n2️⃣Чарли - Сельский клуб\n3️⃣Анжело - Сельский клуб \n4️⃣Амбер - Вжух Вжух\n5️⃣Спайк - Подрыв, Острый угол\n6️⃣Гриф - Вжух Вжух\n7️⃣Макс - Роковая шахта\n8️⃣Сэнди - Затопленная\n9️⃣Бастер - Затопленная шахта\n🔟Лола - Вжух Вжух\n❗Это топ бойцов для захвата кристалов❗',
                                        reply_markup=kb.back3)
    
@router.callback_query(F.data == 'bb1')
async def bb1(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(photo='https://brawldb.ru/wp-content/uploads/2021/10/maxresdefault-18-1024x576-1.jpg', 
                                        caption='1️⃣Мелоди - Мечта вратаря\n2️⃣Пёрл - Окружение\n3️⃣Корделиус - Пляжный воллейбол\n4️⃣Леон - Мечта вратаря\n5️⃣Сту - Окружение\n6️⃣Фэнг - Почти на всех картах\n7️⃣Джеки - В центре внимания\n8️⃣Лу - Сечатка\n9️⃣Лари и Лори - Пинбол\n🔟Пчела - Вне линии\n❗Это топ бойцов для броубола❗',
                                        reply_markup=kb.back3)
    

@router.callback_query(F.data == 'gz1')
async def bb1(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(photo='https://www.brawlstarsdicas.com.br/wp-content/uploads/2020/01/novo-modo-hot-zone-brawl-stars-dicas-zona-quente-1536x863.jpg', 
                                        caption='1️⃣Рико - Разрыв\n2️⃣Мико - Разрыв\n3️⃣Мег - Огненное кольцо\n4️⃣Джесси - Муравьиные бега\n5️⃣Коллет - Открытая зона\n6️⃣Бель - Муравьиные бега\n7️⃣Джеки - В центре внимания\n8️⃣Гейл - Разрыв\n9️⃣Поко - Открытая зона\n🔟Спайк - Огненное кольцо\n❗Это топ бойцов для горячей зоны❗',
                                        reply_markup=kb.back3)
    
    
@router.callback_query(F.data == '5back')
async def back5(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer('❗В каком режиме вы хотите узнать мету❗', reply_markup=kb.meta)
    
    
@router.message(F.text == '💵Буст рангов')
async def bust(message:Message):
    await message.answer(text='❗Напишите нам по поводу буста чтобы узнать все подробности❗',
                         reply_markup=kb.bust)
    
@router.message(F.text == '📜Техподдержка')
async def teh(message:Message):
    await message.answer(text='Опишите проблему',reply_markup= kb.teh )

    
    

    
    
    