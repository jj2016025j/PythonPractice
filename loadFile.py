# 讀取檔案
import json

# 將這個變量替換成你的 JSON 檔案路徑
config_file = 'config.json'

# 讀取 JSON 檔案
with open(config_file, 'r') as file:
    config = json.load(file)

# 從 JSON 物件中提取資訊
consumer_key = config['twitter']['consumer_key']
consumer_secret = config['twitter']['consumer_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

print(consumer_key)
print(consumer_secret)
print(consumer_secret)
print(access_token_secret)

#發文
#修改
#爬文