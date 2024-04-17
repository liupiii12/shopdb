@router.callback_query(F.data == 'rb')
async def rb(callback: CallbackQuery):
    await callback.answer('Вы выбрали мета в ранговом бою')
    await callback.message.edit_text(text='''Мета для рангового боя
1️⃣Чарли
2️⃣Корделиус
3️⃣Анжело
4️⃣Спайк
5️⃣Нани
6️⃣Бастер
7️⃣Амбер
8️⃣Биби
9️⃣Лари и Лори
Вот список самых лучших персонажей для рангового боя''')
