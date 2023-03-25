import telebot
import requests
import json
bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def send_welcome(message): 
    bot.send_message(message.chat.id, text="Welcome! Type name city and number of date to get weather information")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text
    if city == "London":
        data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=cb1657161a4c396d7510303571ee489f&units=metric").json()
        bot.send_message(message.chat.id, text=(f"In {data['city']['name']}:\nDate: {data['list'][0]['dt_txt']}\nTemp: {data['list'][0]['main']['temp']}\nHumiditi: {data['list'][0]['main']['humidity']}\nWeather: {data['list'][0]['weather'][0]['main']}"))
    else: 
        bot.send_message(message.chat.id, text="Wrong city.")
bot.infinity_polling()
