import logging #логирование всех сообщений
#импортируем из библиотеки python-telegram-bot
#Updater - отвечает за коммуникацию с сервероми 
#CommandHandler - Для обработки команд

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import setting
logging.basicConfig(filename="bot.log", level=logging.INFO)#куда сохраняются логи и с каким уровнем точности

#создаем функцию "greet_user" для ответа на старт 
def greet_user(update, context):
    print("Вызван /start") #бот сообщает в консоль
    print(update)   #посмотреть в консоле информацию о пользователе
    update.message.reply_text("Здравствуй пользователь") #ответ пользователю

def talk_to_me(update, context):
    text = update.message_text
    print()
    update.message.reply_text(text)

#создаем бота "main" 
def main():
    # Передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(setting.API_KEY, use_context = True)
    dp = mybot.dispatcher #диспетчер dp - сокращенно
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info ("Бот стартовал") #почему-то не работает в bot.log не пишет 
    # Командуем боту начать ходить в Telegram за сообщениями    
    mybot.start_polling()

    # Запускаем бота, он будет работать, пока мы его не остановим принудительно ctrl+c
    mybot.idle()

main()
