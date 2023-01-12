import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

bot = telegram.Bot(token='your_bot_token_goes_here')

def create_poll(bot, update, args):
    question = " ".join(args)
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],
                [InlineKeyboardButton("Option 3", callback_data='3')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=update.message.chat_id,
                     text=question,
                     reply_markup=reply_markup)

def handle_callback(bot, update):
    query = update.callback_query
    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

def main():
    updater = Updater(token='your_bot_token_goes_here')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('create_poll', create_poll, pass_args=True))
    dp.add_handler(CallbackQueryHandler(handle_callback))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
################################
#         Bot Details
# TelegramBots/pull-bot 
# Version: 1.0
################################
#         Copy Right Details
# © OpenBotBook
# https://github.com/OpenBotBook
# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
################################
