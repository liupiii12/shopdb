
            
from telebot import *
import webbrowser

bot = telebot.TeleBot('6960030139:AAEWVfQZWZpJSVbCto8ye-G9-RXvb4qm68g')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Открыть веб сайт')
    item2 = types.KeyboardButton('Помощь')
    
    
    markup.add(item1, item2, )
    
    bot.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Открыть веб сайт':
            webbrowser.open('https://yabs.yandex.ru/count/WcKejI_zOoVX2LcO0hqI01CYW2OQbKgbKga4mGHzFfSxUxRVkVE6Er-_u_M6ErmbwuoWf9yGX6Wa8Lbf6241_H1HYuIkFpIAg40bY92iIaf5IzIW8EfFaVN8oFv9EhBjdnb7EQHEA9v7ezEVgj0H4JKe1rIQuxPJ2dL2xPyLBYAem88V6zQY6ibQHJAgYwn7HYIIP1G9LOkeGoIMa4OGKOk4hYDisB2nk0EcRDPauS34NKf_qzFt4rE5GSVHYtr80VpISZVeH6Th8ejgYj1EY1KZqaQdd2yD8cfb5Zq-TLHQKuTgs58xQjlG9vuxy-azlQFrr9ddqUZpUKkVk6rBRGbmiFxli6oioKaLGiORhqVKuTQyT6-0Esxs7B4B0nOrdAiZX3PUlrt2zHb-lshW8Tj3kIvoMLQ8D5pzwdEIw4L6jSnq4669Ye0Y9dbEygBIljIQL4uKjfw23ZEX_9EeTSMGcpeMZwa9wrIZP4-33XutFJ3T8hAREUeAhLfJps-RNBzjxZ1NHi0_ZDDZHv4Fti14xUv__P2riE_rGzR2FjSx-SBxkmTDW7PV-ulidVtiBx9tnZG7m3Z9B0V0EFcrOKKtcIp2Bxt7F5BHMr_r0upE-ZfVdg13EVHaBwTdzkR7j0SRy0P52jT_ZtxK5NdpMrhNzSOVTKNUl5R6PptDp9LAfV9AKn1fBxVA_yTsOoQ3Ux0G7Fp-OO44LyDM5FVHBaO_TdDQZTuH0O-omZWB-bbI1YIuOMlIXtz3U8q4DJ0uBeF2GRuz1niSDqi8t8KbGsBEBca7kgSnWYDm6bmmYwRt-gtITsQy~2?etext=2202.z2jNtyxwdsGcIoltfx5ri2FkbG93cmRycGdzc25veHc.4d1d03335c9ddbccc7b4ee09fe391d85c35d943a&from=yandex.ru%3Bsearch%26%23x2F%3B%3Bweb%3B%3B0%3B&q=финам&baobab_event_id=lu7vn2i1oc')
        elif message.text == 'Помощь':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Находка бага или ошибки')
            item2 = types.KeyboardButton('Другое')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Помощь', reply_markup=markup)
        elif message.text == 'Назад':
            start(message)  # вызываем функцию start
        elif message.text == 'Находка бага или ошибки':
            bot.send_message(message.chat.id, 'Опишите проблему')
        elif message.text == 'Другое':
            bot.send_message(message.chat.id, 'Опишите проблему')

bot.polling()
    
                
                

            
                
    
    
            
            
            
            

            

            b2125dd2bc6b3f16c30fa4cebdc01c7f
    
    
bot.polling(non_stop= True)#Делаем бесконечный цикл работы бота, писать в конце