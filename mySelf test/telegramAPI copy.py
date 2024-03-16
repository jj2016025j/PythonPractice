# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# from telegram import Update, Filters
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import logging
import json

# 啟用日誌記錄
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# 读取配置文件
with open('config.json', 'r') as file:
    config = json.load(file)

# 从配置文件中获取所需的值 # 機器人的 Token，您應該從 @BotFather 獲得
TOKEN = config['TELEGRAM']['TOKEN']

def start(update, context):
    """發送一條消息當命令 /start 被發出來。"""
    update.message.reply_text('Hi! I am your bot.')

def echo(update, context):
    """回顯用戶發送的消息。"""
    update.message.reply_text(update.message.text)

def error(update, context):
    """記錄錯誤。"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """啟動機器人。"""
    # 創建 Updater 並傳入你的機器人的 TOKEN。
    updater = Updater(TOKEN)

    # 獲取 dispatcher 來註冊處理程序
    dp = updater.dispatcher

    # 不同的處理程序
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # 記錄所有錯誤
    dp.add_error_handler(error)

    # 開始機器人
    updater.start_polling()

    # 運行機器人，直到您按 Ctrl-C 或機器人停止
    updater.idle()

if __name__ == '__main__':
    main()
