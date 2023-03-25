import telebot
import requests
import json


bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def get_city(message):
    msg = bot.send_message(message.chat.id, text="Send city name")
    global city 
    city = message.text
    bot.register_next_step_handler(msg, get_number)

def get_number(message):
    msg = bot.send_message(message.chat.id, text="Send number of date")
    global number 
    number = int(message.text)
    bot.register_next_step_handler(msg, get_weather)


@bot.message_handler(content_types=['text'])
def get_weather(message):
    if number > 1 and number < 16:
        try:
            data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&cnt={number}&appid=cb1657161a4c396d7510303571ee489f&units=metric").json()
            bot.send_message(message.chat.id, text=(f"In {data['city']['name']}:\nDate: {data['list'][0]['dt_txt']}\nTemp: {data['list'][0]['main']['temp']}\nHumiditi: {data['list'][0]['main']['humidity']}\nWeather: {data['list'][0]['weather'][0]['main']}"))
        except: 
            bot.send_message(message.chat.id, text="Wrong city.")
    else:
        bot.send_message(message.chat.id, text="Wrong number, you can enter number from 1 to 16")

bot.infinity_polling()