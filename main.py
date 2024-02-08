from info import *
import os 
from Subject import *
from threading import Timer
bot=telebot.TeleBot(Token)

@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(message.chat.id,"اهلا وسهلاا" +" : "+ message.chat.first_name +" "+ message.chat.last_name)
    bot.send_message(message.chat.id, " كل ماعليك كتابة اسم المادة وسيتم تزويدك بالنمادج نتمنى لك التوفيق ")
    bot.send_message(message.chat.id, "اختر اسم المادة:\n" + Subject)
    
@bot.message_handler(func=lambda query:True)
def callback_handler(query):
    subject = query.text
    if subject in SubjectList:
        files = os.listdir('Subject/' + subject)
        if bool(files):
            for file in files:
                bot.send_document(query.chat.id, open('Subject/' + subject + '/' + file))
        else:
            bot.send_message(query.chat.id, "لايوجد ملفات لهده المادة")
            
    else:
        bot.send_message(query.chat.id, " اسم المادة غير موجود")
        
bot.infinity_polling()
