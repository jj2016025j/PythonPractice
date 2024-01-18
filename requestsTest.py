#用來測試請求功能
#功能成功20240118
import requests
import json

# 將這個變量替換成你的 JSON 檔案路徑
config_file = 'config.json'

# 讀取 JSON 檔案
with open(config_file, 'r') as file:
    config = json.load(file)

# 從 JSON 物件中提取資訊
bearer_token = config['twitter']['bearer_token']
username = "Skimmy._."  # 替換為目標 Twitter 用戶名
user_name = config['twitter']['user_name']

url = f"https://api.twitter.com/2/users/by/username/{user_name}"
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

response = requests.get(url, headers=headers)

print(response.json())

# 這是直接丟在cmd的命令
# curl "https://api.twitter.com/2/users/by/username/Skimmy._." -H "Authorization: Bearer %"