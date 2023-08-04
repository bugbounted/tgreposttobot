import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define your channel username (without '@')
CHANNEL_USERNAME = 'your_channel_username_here'

# Define your bot token
BOT_TOKEN = 'your_bot_token_here'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot is running and watching the channel!')

def forward_message(update: Update, context: CallbackContext) -> None:
    # Forward the received message to your bot's chat
    context.bot.forward_message(chat_id='your_bot_chat_id_here', from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def main() -> None:
    # Create the Updater and pass your bot token
    updater = Updater(token=BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Define a command handler for /start command
    dispatcher.add_handler(CommandHandler('start', start))

    # Define a message handler to forward messages from the channel
    dispatcher.add_handler(MessageHandler(Filters.chat(username=CHANNEL_USERNAME), forward_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
