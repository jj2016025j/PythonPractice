from selenium import webdriver

# 設定 WebDriver 路徑
driver_path = 'C:/Users/User/WebPractice/PythonTool/chromedriver_win32'  # 替換為你的 ChromeDriver 路徑

# 選項設定
options = webdriver.ChromeOptions()
options.headless = True  # 啟用無頭模式

# 啟動 WebDriver
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# 打開網頁
driver.get('https://kobeantique.com/pages/shop-access')  # 替換為你想截圖的網頁地址

# 截取網頁截圖
driver.save_screenshot('screenshot.png')

# 關閉 WebDriver
driver.quit()
