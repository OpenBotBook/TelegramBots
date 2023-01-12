import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

bot = telegram.Bot(token='your_bot_token_goes_here')

def create_event(bot, update, args):
    event_name = args[0]
    event_time = args[1]
    keyboard = [[InlineKeyboardButton("Going", callback_data='going'),
                 InlineKeyboardButton("Not Going", callback_data='not_going')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=update.message.chat_id,
                     text=f"Event {event_name} created at {event_time}",
                     reply_markup=reply_markup)

def handle_callback(bot, update):
    query = update.callback_query
    bot.edit_message_text(text=f"You selected {query.data} for event {event_name}",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

def main():
    updater = Updater(token='your_bot_token_goes_here')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('create_event', create_event, pass_args=True))
    dp.add_handler(CallbackQueryHandler(handle_callback))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

################################
#         Bot Details
# TelegramBots/events-bot/main.py 
# Version: 1.0
################################
#         Copy Right Details
# © OpenBotBook
# https://github.com/OpenBotBook
# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
################################
