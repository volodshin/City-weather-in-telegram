#import telebot
import requests
import json
#bot = telebot.TeleBot("")

city = input()
number = 
data = requests.get("https://api.openweathermap.org/data/2.5/forecast?q={}&cnt=10&appid=cb1657161a4c396d7510303571ee489f&units=metric").format(city)

res = requests.get(url)

data = res.json()

print(data)

'''@bot.message_handler(commands=['start'])
def send_welcome(message): 
    bot.send_message(message.chat.id, text="Welcome!, send command /weather to get information about city")

@bot.message_handler(command=['weather'])
def send_weather(message):'''
    