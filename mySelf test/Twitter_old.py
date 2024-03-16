import tweepy
import json

# 讀取配置文件
with open('config.json', 'r') as file:
    config = json.load(file)

# 從配置文件中獲取所需的值
USER_NAME = config['Twitter']['USER_NAME']
API_KEY = config['Twitter']['API_KEY']
API_SECRET_KEY = config['Twitter']['API_SECRET_KEY']
ACCESS_TOKEN = config['Twitter']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['Twitter']['ACCESS_TOKEN_SECRET']

# 認證並設定 API 對象
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 使用者名稱（screen name）
user_screen_name = USER_NAME

# 獲取用戶的貼文
tweets = api.user_timeline(screen_name=user_screen_name, count=100)

for tweet in tweets:
    print("=== Tweet ===")
    print(tweet.text)
    if 'media' in tweet.entities:
        for media in tweet.entities['media']:
            print("Media URL:", media['media_url'])

    print("\n")

# 使用 API 來抓取用戶的貼文
def get_user_tweets(user_handle, num_tweets=10):
    tweets = api.user_timeline(screen_name=user_handle, count=num_tweets, tweet_mode='extended', include_rts=True)
    for tweet in tweets:
        print(tweet.full_text)
        if 'media' in tweet.entities:
            for media in tweet.entities['media']:
                if media['type'] == 'photo':
                    print(media['media_url_https'])

# 調用方法
get_user_tweets(user_screen_name, num_tweets=10)
