import requests
from bs4 import BeautifulSoup
import os
import time
from selenium import webdriver
import telegram
from token2 import api_token
from webdriver_manager.chrome import ChromeDriverManager

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))+'\\'
print(BASE_DIR)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(3)

bot = telegram.Bot(token=api_token)
chat_id = '5339073127'

while True:
    req = driver.get('https://www.youtube.com/watch?v=-JhoMGoAfFc')
    value = driver.find_element_by_xpath('//*[@id="count"]/ytd-video-view-count-renderer/span[1]')
    try:
        latest = value.text
    except:
        latest = ""
    print(latest)

    with open(BASE_DIR+'latest.txt', 'r+') as f_read:
        before = f_read.readline()
        if before != latest:
            bot.sendMessage(chat_id=chat_id, text=f'new value: {latest}')
        # else:
        #     bot.sendMessage(chat_id=chat_id, text='새 글이 없어요 ㅠㅠ')
        f_read.close()

    with open(BASE_DIR+'latest.txt', 'w+') as f_write:
        f_write.write(latest)
        f_write.close()

    time.sleep(60)