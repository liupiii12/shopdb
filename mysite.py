from telebot import*
import webbrowser
bot = telebot.TeleBot('7169332384:AAGKod8AGIu6ZqrC8sRwysi0S97i6mdu48A')
@bot.message_handler(commands=['strat'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.InlineKeyboardButton('Курсы валют')
    item2 = types.InlineKeyboardButton('Дата создания валют')
    item3 = types.InlineKeyboardButton('Открыть брокерский счёт')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
            item4 = types.InlineKeyboardButton('USDT (Курс Доллара)')
            item5 = types.InlineKeyboardButton('BTC (Курс Биткоина)')
            item6 = types.InlineKeyboardButton('Ethereum (Курс Эфириума)')
        
            bot.send_message(message.chat.id, 'Выберете валюту')
        
            markup.add(item4, item5, item6)
    if message.chat.type == 'private':
        if message.text == 'USDT (Курс Доллара)':
            webbrowser.open('https://ru.investing.com/currencies/usd-rub')
        elif message.text == 'BTC (Курс Биткоина)':
            webbrowser.open('https://ru.investing.com/crypto/bitcoin/btc-usd')
        elif message.text == 'Ethereum (Курс Эфириума)':
            webbrowser.open('https://ru.investing.com/crypto/ethereum/eth-usd')
@bot.message_handler(chat_types=['text'])
def bot_data(message):
    if message.chat.text == 'private':
        if message.text == 'Дата создания валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
            item7 = types.InlineKeyboardButton('Дата создания USDT')
            item8 = types.InlineKeyboardButton('Дата создания BTC')
            item9 = types.InlineKeyboardButton('Дата создания Ethereum')
            markup.add(item7 , item8 , item9)
            bot.send_message(message.chat.id, 'Выберете валюту')
    if message.chat.text == 'private':
        if message.text == 'Дата создания USDT':
            bot.send_message(message.chat.id , '''История этой валюты началась в 2013 году, когда разработали алгоритм Mastercoin или Omni Layer. Он основан на блокчейне Bitcoin. В 2015 году компания Tether Limited представила на рынок одноименный токен.

Tether переводится как «привязывать», что отражает суть криптовалюты. Ее курс привязан к доллару США. Буквенное обозначение — USDT (United States Dollar Tether).

В 2015 году стейблкоин вышел на биржу Bitfinex. Сейчас его капитализация достигла более 83 млрд долларов. По этому показателю он находится на третьем месте после Bitcoin и Ethereum (эфир).''')
        elif message.chat.text == 'Дата создания BTC':
            bot.send_message(message.chat.id , '''Биткойн - это первый пример децентрализованных цифровых денег, созданных в 2008 году человеком или группой людей под псевдонимом Сатоши Накамото.''')
        elif message.text == 'Дата создания Ethereum':
            bot.send_message(message.chat.id , '''История криптовалюты Эфириум началась в 2013 году, когда Виталик Бутерин — канадско-российский программист — создал эту цифровую валюту и запустил сеть на ее основе. Монета быстро стала второй в мире по капитализации после биткоина. Точный прирост в стоимости с момента запуска до текущего момента (август 2021) отследить сложно, поскольку курс постоянно меняется, однако примерный показатель — 234 000%.''')
@bot.message_handler(content_types=['text'])
def bot_brc(message):
    if message.chat.text == 'private':
        if message.text == 'Открыть брокерский счёт':
            markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
            item10 = types.InlineKeyboardButton('Открыть в Тинькофф')
            item11 = types.InlineKeyboardButton('Открвть в Сбер')
            item12 = types.InlineKeyboardButton('Открыть в Финам')
            markup.add(item10 , item11 , item12)
        if message.chat.text == 'private':
            if message.text == 'Открыть в Тинькофф':
                webbrowser.open('https://yabs.yandex.ru/count/Wd0ejI_zOoVX2La40nKJ0CEXVYOQbKgbKga4mGHzFfSxUxRVkVDTNpjVl-FrXZlSg3H7LQZ8I4Y65UdEaMHqbCDwT4CfoUWe1zJvpA7FgDD-sZcgGjGSK1mQjQDGvnJFKHMIaGEFIgVsRKjpL8M2bAn8EMpdZUTuBeLAyHnLeQEhjIZ92Cc63Hj7Ti2KpPgg68GNbfJU1go27bFKCEWuUhBXunG-jgpJbSus138GHqKZacbd34255Q1b00gi02q3K5y5Q1c0sWlGIXkTShuEn2YLIgLIcTEzO6m4y9RMrA4QpwWJwhIZjdFwlA6sFPNcKRkEHgFIfot5fL0eRjjIUmKETW4WFAwyTM9Q1c-yXz0bMKFapkSR9XkltrOnzp3yVjN0Gp28QMMf4M_O7ifraSkoGgJXcacOCgG30x1TKkxxlcyyW2yCtY8cUKxoejA-r9fKJXIsW6oHCUIcZWKpwLYnclA9fHG6Dc0mtIAocpdg2grQKyzlcro_RUu-RCh73tycy9OFNae9qlQ_zDWHjE-bnuwWVIvj22V-kuL5GovVEm7AoEJFJe0oCiaqno26cUKOn31ptDnHvlJ3L_q0exDqcI_Nq3afUh8FMzF1zMFQWtVoqgpk_7S3hRT1GQstA7TUwzU2RBkK-AptkdyBe_Cshacv0poYcRbIgLHUwRgbpMGglnFJX1Xebo7A8Fo09W8qQP0vX624t8kNdWiepJsfbJk7FW0K90sKslepF7csVmNerQGtiAVjx68QxV6oq6gnv-HYvqNGDYGH5n4kMdFMC1wee6iHldELu158PZz4i4M3gXLgpgYOERPRfJu66W40~2?etext=2202.tERXcM93XM2Ry2dUaLeIic6zyuql2XLWtO3sNUX3RHpvgKiVIt6AMg9hjz-AAQ1dzTBZgJSXxI8yaer9JjN-4GRib2dwcGtrc2lpYmh4amY.6fe68ae51976d1cd6719f52547787a751cfe7888&from=yandex.ru%3Bsearch%26%23x2F%3B%3Bweb%3B%3B0%3B&q=открыть+брокерский+счет&baobab_event_id=lu8co02ljy')
            elif message.text == 'Открыть в Сбер':
                webbrowser.open('https://yabs.yandex.ru/count/WmSejI_zOoVX2Ldi0yqN04Ddb2OQbKgbKga4mGHzFfSxUxRVkVE6Er-_u_M6Eznd3i960G8gpK7OA43OqzpkiK_a8EoU4r8GKUbFZnFQ0yA90iG9AGWZguoV8AIa4r8GkLCgjUsf5Eh4JqX1L8L-PXoTa8BuaKgdEVGvdKvntBwdqwWpd-BFUoh5yMdqX1H4ZI8X6T7fyuaa0tfFepTE0-ddZjfEf-ryLeraM8E4QY1PatwGh3ICa818a42o0YMDi6731hDh1qpPhAcAGNXXIUbjm2heCKKDWuvZ2IPxPOPRLLrRTBQ-Y197nI9rYr9U680AAq3B01HO0Le6eBuAq380jHUWbJOwvNmTY54gbKgbCgThGMAOv8Sm_S7x8UizS6zfJHsgyOmweKuxQZkdpnjgsrDf7hNhQ3GgVTfIN0g5uhOjjLVWO1S0mkFAMoUcPV362m0V5AvS-S6fOf9du_LR3qcW46PfrS13PXW2CL8Zth0zbEiYbsM5ICCrap1bI0S6OBkatFTzttW0NnXsi9SCo18CsI8cUKxoejA-r2niOtGTnXGsXjpKTN1D-SHI2WCRC9Xk4TdD77M5LgsfvxTDhjyszoKIBi8VdfcyU_jW2e5jKFvtoQEB-xrB7btSprqEDidwEmAJUObVMs5hYD_FLjWQuiSqno1UOPPZ4AyqTvGv_Q0RQNhipxPEzEwhVe3HMVhGbs_QcZHwil_YGsBsOzg3GV3mSeVelqRaDY1tValhkew5t0Rapclz3n_YALC-Y_EeHxe9eNBySKGpSwLIgRpITKkRkQZy7cU08j0kGvG1E_oGLtHT26XIPB8rPI1_OyZUbHFlmVi-3QfeqnhMtX29S7hheTH04rwpL30ehnpXGoZcXwY8eSjVFDexrRbFqbVWambn3tUOTxIQe-8bDV0h8yCJwR3_TgfkkQ3AK0Eevoy-RHcazEWhM12rGOzn1zG_AxyBce6KDh1ABkp2GJX8PmpQkA66cTlwCnLYyCKzGJMLHwihdbfgBLgBZHPrk5MIAg4H~2?etext=2202.tERXcM93XM2Ry2dUaLeIic6zyuql2XLWtO3sNUX3RHpvgKiVIt6AMg9hjz-AAQ1dzTBZgJSXxI8yaer9JjN-4GRib2dwcGtrc2lpYmh4amY.6fe68ae51976d1cd6719f52547787a751cfe7888&from=yandex.ru%3Bsearch%26%23x2F%3B%3Bweb%3B%3B0%3B&q=открыть+брокерский+счет&baobab_event_id=lu8cpbr6i8')
            elif message.text == 'Открыть в Финам':
                webbrowser.open('https://www.finam.ru/landings/otkrytie-scheta/')         
bot.polling()   