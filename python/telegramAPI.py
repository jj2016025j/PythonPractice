import json
import logging
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CallbackContext, CommandHandler, CallbackQueryHandler
from telegram import Update, Document, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
import os

# 创建 img 文件夹（如果不存在）
img_folder_path = os.path.join(os.path.dirname(__file__), 'img')
os.makedirs(img_folder_path, exist_ok=True)

# 讀取配置文件
with open('config.json', 'r') as file:
    config = json.load(file)

# 從配置文件中獲取機器人的 Token
TOKEN = config['TELEGRAM']['TOKEN']
TARGET_CHAT_ID = config['TELEGRAM']['TARGET_CHAT_ID']

# 設置日誌
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Store bot screaming status
screaming = False

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

#訊息列表
messages = []

# 處理接收到的消息
def handle_message(update: Update, context: CallbackContext) -> None:
    message = update.message
    print(update)
    # Print to console
    print(f'Is {update.message.from_user.username} message')

    # Define the target chat ID for forwarding
    target_chat_id = TARGET_CHAT_ID  # Replace with the actual chat ID
    # 替换为目标聊天室的 ID

        # Check if the message should be forwarded to a specific user or back to the sender
    if forward_to_specific_user :
        # Forward the message to the specific user
        context.bot.forward_message(chat_id=target_chat_id, 
                                    from_chat_id=update.message.chat_id, 
                                    message_id=update.message.message_id)
        print(f'Is forward to id [{target_chat_id}] [{update.message.text}]')
        # 转发消息到另一个聊天室 不包含來源
        # context.bot.send_message(chat_id=target_chat_id, text=message.text)
        # 转发消息到 Saved Messages 發送用戶effective_user
        # context.bot.forward_message(chat_id=update.effective_user.id,
        #                             from_chat_id=update.effective_chat.id,
        #                             message_id=message.message_id)     
        # print(f"转发消息到 Saved Messages {update.effective_user.username}")

        # 检查消息类型并相应处理
        if message.text:
            handle_text_message(message)
        elif message.photo:
            handle_media_message(message.photo[-1], context.bot, 'photo', message)
        elif message.video:
            handle_media_message(message.video, context.bot, 'video', message)
        elif message.document:
            handle_document_message(message, context.bot)
        else:
            # This is equivalent to forwarding, without the sender's name
            update.message.copy(update.message.chat_id)
            print(update.message.chat_id)
    else:
        update.message.copy(update.message.chat_id)
        print(f"copy{update.message.chat_id}")
    
    #
    # print(f'{update.message.from_user.first_name} 說了 {update.message.text}')

# handle_text_message, handle_media_message, handle_document_message 和 save_message 函数保持不变


def handle_text_message(message):
    message_data = {
        'user': message.from_user.to_dict(),
        'text': message.text,
        'date': message.date.isoformat()
    }

    save_message(message_data)

def handle_media_message(media, bot, media_type, message):
    file_id = media.file_id
    new_file = bot.get_file(file_id)

    # 獲取文件擴展名
    file_extension = os.path.splitext(new_file.file_path)[1].lower()
    supported_formats = ['.jpg', '.jpeg', '.gif', '.png', '.svg', '.webp', '.mp4', '.avi', '.mov']

    if file_extension in supported_formats:
        # 构建文件保存路径
        file_name = os.path.join(img_folder_path, f'{media_type}_{message.message_id}{file_extension}')
        print("Downloading to:", file_name)
        try:
            new_file.download(file_name)
            print("Download successful")
        except Exception as e:
            print("Error downloading file:", e)

        message_data = {
            'user': message.from_user.to_dict(),
            'media': file_name,
            'date': message.date.isoformat()
        }
        save_message(message_data)
        
def handle_document_message(message, bot):
    document = message.document
    supported_document_formats = ['application/zip', 'application/x-7z-compressed', 'application/x-rar-compressed']

    if document.mime_type in supported_document_formats or document.file_name.lower().endswith(('.jpg', '.jpeg', '.mp4', '.avi', '.mov', '.7z', '.rar', '.webp')):
        file_id = document.file_id
        new_file = bot.get_file(file_id)
        file_name = f'document_{message.message_id}_{document.file_name}'
        print("Downloading to:", file_name)
        try:
            new_file.download(file_name)
            print("Download successful")
        except Exception as e:
            print("Error downloading file:", e)

        message_data = {
            'user': message.from_user.to_dict(),
            'document': file_name,
            'date': message.date.isoformat()
        }
        save_message(message_data)

def save_message(message_data):
    try:
        # 尝试读取现有数据
        with open('messages.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # 如果文件不存在或不是有效的 JSON，开始一个新列表
        data = []

    # 添加新消息到数据列表
    data.append(message_data)

    # 写回完整的数据到文件
    with open('messages.json', 'w') as file:
        json.dump(data, file, indent=4)

def main():
    # 使用從配置文件中讀取的 Token 初始化 Updater
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # 註冊處理程序
    # 添加訊息處理器
    dp.add_handler(MessageHandler(Filters.all, handle_message))

    # 啟動機器人
    updater.start_polling()
    print("Bot started")
    updater.idle()
    print("Bot stopped")

if __name__ == '__main__':
    main()
