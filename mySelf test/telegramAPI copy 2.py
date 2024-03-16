from telegram.ext import Updater, CommandHandler
import json

# 读取配置文件
with open('config.json', 'r') as file:
    config = json.load(file)

# 从配置文件中获取所需的值 # 機器人的 Token，您應該從 @BotFather 獲得
TOKEN = config['TELEGRAM']['TOKEN']

def start(update, context):
    update.message.reply_text('Hello! I am your bot.')

def main():
    TOKEN = 'YOUR_BOT_TOKEN'
    updater = Updater(TOKEN)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()