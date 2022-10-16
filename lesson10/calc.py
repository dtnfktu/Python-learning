import telebot
from telebot import types
import parsing
import parsecomplex
import logger

# иницируем бота
bot = telebot.TeleBot(token)

expr = ''
helptext = 'Введите выражение. Например: (3+2.5)/8\nКомплексные числа заключаем в [ ], у мнимой части ставим i\n '
helptext += 'Например: [4+3.2i]*[3]\n'
helptext += 'При работе с комплексными числами **каждое** число заключаем в [ ], даже без мнимой части'

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/help' or message.text == '/?':
        logger.addlog('calc.log','Help text')
        bot.send_message(message.from_user.id, helptext)
        return
    if message.text == '/stop' :
        logger.addlog('calc.log','Stop bot')
        bot.stop_polling()
        return

    if '[' in message.text :
        try :
            expr = parsecomplex.calculate(message.text)
            logger.addlog('calc.log',message.text + ' = ' + expr)
            bot.send_message(message.from_user.id, expr)
        except :
            logger.addlog('calc.log','Error in expression - ' + message.text)   
            bot.send_message(message.from_user.id, "Ой-ой. Что-то введено не так")
    else :
        print(message.text)
        try:
            expr = parsing.calculate(message.text)
            logger.addlog('calc.log',message.text + ' = ' + expr)
            bot.send_message(message.from_user.id, expr)
        except :
            logger.addlog('calc.log','Error in expression - ' + message.text)
            bot.send_message(message.from_user.id, "Ой-ой. Что-то введено не так")

bot.infinity_polling()
