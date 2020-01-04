echo "# HabrParser_Bot" >> README.md
git init
git add .
git add *
git commit -m "Initial Commit" -a
git remote add origin origin https://github.com/akbulat/akbulat #Указываем свою ссылку
git push -u origin master

import pyowm
import telebot

bot = telebot.TeleBot("962187705:AAHcTTmtC9luxRYxbf7NIEuNPce_mC2-BmY")
owm = pyowm.OWM('46c398f065a0802ebdc474c1ac3e78b7', language = "ru")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    
    answer = " В городе " + message.text + " cейчас " + w.get_detailed_status() + "\n"
    answer += " Температура " + str (temp) + " ℃ " + "\n\n"
    
    if temp < 1:
        answer += "Господин Акбулат запретил гулять. "
    elif temp >1:
        answer += "Господин Акбулат разрешил выйти на улицу. "

    bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True, timeout=123 )
