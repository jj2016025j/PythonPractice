import tweepy
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
user_name = config['twitter']['user_name']

# 現在你可以使用這些變量來與 Twitter API 進行互動   
# 這裡填入你的 Twitter API 認證

# 認證和初始化 Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# # 發布推文
public_tweets = api.home_timeline()

print(public_tweets)

# def post_tweet(text):
#     try:
#         api.update_status(text)
#         print("Tweet posted successfully.")
#     except Exception as e:
#         print(f"Error: {e}")

# post_tweet("Hello Twitter!")

# def get_tweets(username, count=10):
#     try:
#         tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
#         for tweet in tweets:
#             print(tweet.full_text)
#     except Exception as e:
#         print(f"Error: {e}")

# get_tweets(user_name, 5)  # 獲取指定用戶最近的 5 條推文

# def get_user_info(username):
#     try:
#         user = api.get_user(screen_name=username)
#         print(f"Username: {user.screen_name}")
#         print(f"Followers Count: {user.followers_count}")
#     except Exception as e:
#         print(f"Error: {e}")

# # 获取用户的信息
# get_user_info("twitter_username")

# # "consumer_key": "",
# # "consumer_secret": "",
# # "bearer_token": "%",
# # "access_token": "-",
# # "access_token_secret": "",
