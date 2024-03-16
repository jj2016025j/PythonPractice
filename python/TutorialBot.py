import logging

from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

import json

# 读取配置文件
with open('config.json', 'r') as file:
    config = json.load(file)

# 从配置文件中获取所需的值 # 機器人的 Token，您應該從 @BotFather 獲得
TOKEN = config['TELEGRAM']['TOKEN']
TARGET_CHAT_ID = config['TELEGRAM']['TARGET_CHAT_ID']

logger = logging.getLogger(__name__)

# Store bot screaming status
screaming = True

#是否發送訊息給用戶
forward_to_specific_user = True

# Pre-assign menu text
FIRST_MENU = "<b>Menu 1</b>\n\nA beautiful menu with a shiny inline button."
SECOND_MENU = "<b>Menu 2</b>\n\nA better menu with even more shiny inline buttons."

# Pre-assign button text
NEXT_BUTTON = "Next"
BACK_BUTTON = "Back"
TUTORIAL_BUTTON = "Tutorial"

# Build keyboards
FIRST_MENU_MARKUP = InlineKeyboardMarkup([[
    InlineKeyboardButton(NEXT_BUTTON, callback_data=NEXT_BUTTON)
]])
SECOND_MENU_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton(BACK_BUTTON, callback_data=BACK_BUTTON)],
    [InlineKeyboardButton(TUTORIAL_BUTTON, url="https://core.telegram.org/bots/api")]
])

def echo(update: Update, context: CallbackContext) -> None:
    """
    This function would be added to the dispatcher as a handler for messages coming from the Bot API
    """

    # Print to console
    print(f'Is {update.message.from_user.first_name} message')

    # if screaming and update.message.text:
    #     context.bot.send_message(
    #         update.message.chat_id,
    #         update.message.text,
    #         # To preserve the markdown, we attach entities (bold, italic...)
    #         entities=update.message.entities
    #     )
    
    # Define the target chat ID for forwarding
    target_chat_id = TARGET_CHAT_ID  # Replace with the actual chat ID

    # Check if the message should be forwarded to a specific user or back to the sender
    if forward_to_specific_user :
        # Forward the message to the specific user
        context.bot.forward_message(chat_id=target_chat_id, 
                                    from_chat_id=update.message.chat_id, 
                                    message_id=update.message.message_id)
    else:
        update.message.copy(update.message.chat_id)
        print(f'Is fall')

    print(f'{update.message.from_user.first_name} wrote {update.message.text}')

def scream(update: Update, context: CallbackContext) -> None:
    """
    This function handles the /scream command
    """

    global screaming
    screaming = True


def whisper(update: Update, context: CallbackContext) -> None:
    """
    This function handles /whisper command
    """

    global screaming
    screaming = False


def menu(update: Update, context: CallbackContext) -> None:
    """
    This handler sends a menu with the inline buttons we pre-assigned above
    """

    context.bot.send_message(
        update.message.from_user.id,
        FIRST_MENU,
        parse_mode=ParseMode.HTML,
        reply_markup=FIRST_MENU_MARKUP
    )


def button_tap(update: Update, context: CallbackContext) -> None:
    """
    This handler processes the inline buttons on the menu
    """

    data = update.callback_query.data
    text = ''
    markup = None

    if data == NEXT_BUTTON:
        text = SECOND_MENU
        markup = SECOND_MENU_MARKUP
    elif data == BACK_BUTTON:
        text = FIRST_MENU
        markup = FIRST_MENU_MARKUP

    # Close the query to end the client-side loading animation
    update.callback_query.answer()

    # Update message content with corresponding menu section
    update.callback_query.message.edit_text(
        text,
        ParseMode.HTML,
        reply_markup=markup
    )

def start(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text('Hello! I am your bot.')


def main() -> None:
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    # Then, we register each handler and the conditions the update must meet to trigger it
    dispatcher = updater.dispatcher

    # Register commands 前面加上/就可以
    dispatcher.add_handler(CommandHandler("scream", scream))
    dispatcher.add_handler(CommandHandler("whisper", whisper))
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(CommandHandler('start', start))

    # Register handler for inline buttons
    dispatcher.add_handler(CallbackQueryHandler(button_tap))

    # Echo any message that is not a command 任何訊息任何格式
    dispatcher.add_handler(MessageHandler(~Filters.command, echo))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()