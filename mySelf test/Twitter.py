import tweepy
import json

# 读取配置文件
with open('config.json', 'r') as file:
    config = json.load(file)

# 从配置文件中获取所需的值
USER_NAME = config['Twitter']['USER_NAME']
BEARER_TOKEN = config['Twitter']['BEARER_TOKEN']

API_KEY = config['Twitter']['API_KEY']
API_SECRET_KEY = config['Twitter']['API_SECRET_KEY']
ACCESS_TOKEN = config['Twitter']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['Twitter']['ACCESS_TOKEN_SECRET']



# 使用 Bearer Token 进行认证
BEARER_TOKEN = config['Twitter']['BEARER_TOKEN']
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# 获取用户的推文
user_screen_name = USER_NAME
user = client.get_user(username=user_screen_name)
user_id = user.data.id
tweets = client.get_users_tweets(id=user_id, max_results=100)

for tweet in tweets.data:
    print(tweet.text)
#================================================================

#提交你的Key和secret
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#獲取類似於內容控制代碼的東西
api = tweepy.API(auth)

#列印我自己主頁上的時間軸裡的內容
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)


#================================================================

# 使用 Bearer Token 进行认证
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# 使用者用户名（screen name）
user_screen_name = USER_NAME

# 获取用户的推文
# 注意：使用 v2 API 时，您需要使用用户的 ID 而不是 screen name
# 首先，获取用户 ID
user = client.get_user(username=user_screen_name)
user_id = user.data.id

# 然后，获取用户的推文
tweets = client.get_users_tweets(id=user_id, max_results=100)

for tweet in tweets.data:
    print("=== Tweet ===")
    print(tweet.text)
    # 在 v2 中，媒体信息可能需要额外的调用来获取

    print("\n")
