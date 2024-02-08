#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

# 目标网页的 URL
url = 'https://leejohnson.ddns.net/templates/'

# 发送 HTTP 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到并打印特定元素（例如，所有的段落）
    for paragraph in soup.find_all('p'):
        print(paragraph.get_text())
else:
    print(f"Error: Unable to retrieve the web page. Status code: {response.status_code}")
