from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 設定您的 Twitter 登錄信息
username = '您的用戶名'
password = '您的密碼'
tweet_content = '這是一條通過 Selenium 發布的推文。'

# ID：如果元素有一個唯一的 ID，您可以使用 By.ID。
# 類別名：如果元素有特定的類別名，您可以使用 By.CLASS_NAME。
# XPath：您可以根據元素的結構創建一個 XPath 表達式。
# CSS 選擇器：如果您熟悉 CSS，可以使用 By.CSS_SELECTOR。
# 初始化 WebDriver
driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

# 選擇使用 Google 登入
time.sleep(2)
google_login_button = driver.find_element(By.XPATH, '//span[contains(text(),"Sign in with Google")]')
google_login_button.click()

# 發布推文
time.sleep(5)  # 等待登錄
tweet_box = driver.find_element_by_class_name('public-DraftStyleDefault-block')
tweet_box.send_keys(tweet_content)
tweet_button = driver.find_element_by_xpath('//span[contains(text(), "Tweet")]')
tweet_button.click()

# 關閉 WebDriver
time.sleep(3)  # 等待推文發布
driver.close()
