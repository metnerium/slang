import openai
openai.api_key = "token"
engine="text-davinci-003"
import telebot
from telebot import types
bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Начать")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот для изучения английского сленга в различных сферах, начнем?)".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Начать"):
        prompt = "дай мне англицизм дай его перевод на английский скажи из какой он сферы придумай одно предложение с ним и переведи его на английский"
        completion = openai.Completion.create(engine=engine,
                                              prompt=prompt,
                                              temperature=0.5,
                                              max_tokens=1000)
        bot.send_message(message.chat.id, text=completion.choices[0]['text'])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Запомнил, идем дальше!")
        button2 = types.KeyboardButton("СЛоЖнА, помогите!")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="all right?", reply_markup=markup)

    elif (message.text == "Запомнил, идем дальше!"):
        prompt = "дай мне англицизм дай его перевод на английский скажи из какой он сферы придумай одно предложение с ним и переведи его на английский"
        completion = openai.Completion.create(engine=engine,
                                              prompt=prompt,
                                              temperature=0.5,
                                              max_tokens=1000)
        bot.send_message(message.chat.id, text=completion.choices[0]['text'])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Запомнил, идем дальше!")
        button2 = types.KeyboardButton("СЛоЖнА, помогите!")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="ok?", reply_markup=markup)

    elif( message.text == "СЛоЖнА, помогите!"):
        prompt = "дай мне развернутый ответ на прошлый англицизм"
        completion = openai.Completion.create(engine=engine,
                                              prompt=prompt,
                                              temperature=0.5,
                                              max_tokens=1000)
        bot.send_message(message.chat.id, text=completion.choices[0]['text'])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Запомнил, идем дальше!")
        button2 = types.KeyboardButton("СЛоЖнА, помогите!")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="продолжим?", reply_markup=markup)





bot.polling(none_stop=True)
