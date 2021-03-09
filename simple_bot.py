"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
catch user keyword and reply suitable data.

Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from telegram import *
from telegram.ext import *
from ticker import Ticker

"""Start the bot."""
# Create the Updater and pass it your bot's token.
BOT_TOKEN = "YOUR_TOKEN"
bot = Bot(BOT_TOKEN)
updater = Updater(BOT_TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# on different commands - answer in Telegram

def infoticker(update,context):
    """
    syntax : /info [keyword] [ticker]
    """
    textinp = update.message.text
    textinp1 = textinp.split()
    emiten = Ticker(textinp1[2])
    update.message.reply_text(emiten.get_data_by_key(textinp1[1]))


dispatcher.add_handler(CommandHandler('info',infoticker))

# Start the Bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
