from sqlite3 import Date
from xml.dom.minidom import Document
import telebot
import os
from telebot import types

bot = telebot.TeleBot('7811486667:AAGBf7cUvTFX6E0MJPlTCoHJis7s4mXg-cg')


# DECORATOR
@bot.message_handler(commands=['start'])
def start(message):
    welcome_msg = f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}\nМеня зовут Станислав Евгеньевич, я провожу отбор кандидатов в научную роту.\nДля того чтобы зарегистрироваться, ответьте на несколько вопросов.'



    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 1)
    faq = types.KeyboardButton("#FAQ")
    about = types.KeyboardButton("#О_нас")
    tg_channel = types.KeyboardButton("Telegram-канал")
    get_docs = types.KeyboardButton("Заполнить документы")
    markup.add(faq, about, tg_channel, get_docs)
    bot.send_message(message.chat.id,welcome_msg, reply_markup=markup)
@bot.message_handler(content_types=["text"])
def welcome(message):
    if message.text == "Заполнить документы":
        # @bot.message_handler()
        txt = open('ads/1.Лист собеседования.txt', 'rb')
        bot.send_document(message.chat.id, txt)
        pdf = open('ads/2.Согласие.pdf', 'rb')
        bot.send_photo(message.chat.id, pdf)
        photo = open('ads/3.Заявление.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

    if message.text == "Telegram-канал":
        bot.send_message(message.chat.id, "https://t.me/+ntFED2PMwUo2MDZi")


@bot.message_handler(content_types=['document'])
def get_user_docs(message):
    os.makedirs(f'{message.from_user.first_name} {message.from_user.last_name}', exist_ok=True)
    chat_id = message.chat.id

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    src = f'{message.from_user.first_name} {message.from_user.last_name}/{message.document.file_name} ({message.from_user.first_name} {message.from_user.last_name})'
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, f"Отлично🔥\nПолучил от Вас:\n{message.document.file_name}")


# nОтправьте в ответном сообщении:\n1) Фамилию Имя Отчество\n2) ВУЗ (дата окончания) \n3) Уровень образования\n4) Специальность \n5) Средний балл\n6) Откуда узнали о роте'

bot.polling(none_stop=True)
