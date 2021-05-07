import telebot
import lintools

bot = telebot.TeleBot('1729455434:AAG8Qf8AKScj0AsaNtShCL1mw3_ld7ly8gk')

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    if message.text == '/start':
        bot.reply_to(message, 'hi')
    elif message.text == '/help':
        bot.reply_to(message, '''You can use this commands:
                user
                vmstat
                reboot
                ifconfig
                disk''')
    
@bot.message_handler(content_types=['text'])
def command(message):
    answer = str(message.text)
    s = answer.split()
    serv = s[0]
    if answer.lower() == 'user':
        fnc = lintools.user()
        bot.reply_to(message, fnc)
    elif answer.lower() == 'vmstat':
        fnc = lintools.vmstat()
        bot.reply_to(message, fnc)
    elif answer.lower() == 'reboot':
        fnc = lintools.reb()
        bot.reply_to(message, fnc)    
    elif answer.lower() == 'ifconfig':
        fnc = lintools.ifconfig()
        bot.reply_to(message, fnc)    
    elif answer.lower() == 'disk':
        fnc = lintools.disk()
        bot.reply_to(message, fnc)
    elif serv.lower() == 'service':
        comm = s[1]
        name = s[2]
        fnc = lintools.service(comm, name)
        bot.reply_to(message, fnc)
        
bot.polling(none_stop=True, interval=0)

