from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import requests
import os
import time

if __name__ == '__main__':
    # PATH = "C:\Program Files (x86)\chromedriver.exe"

    USER_AGENT_LIST = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
    ]
    userAgent = "user-agent=" + random.choice(USER_AGENT_LIST)

    opts = Options()
    opts.add_argument(userAgent)
    opts.add_argument('--no-sandbox')
    opts.add_argument('--headless')
    opts.add_argument("window-size=1280,800")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option('useAutomationExtension', False)
    opts.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=opts)

    FileType = "pdf"

    driver.get("https://file-examples.com/")
    driver.implicitly_wait(10)

    driver.find_element_by_id("menu-item-27").click()
    driver.implicitly_wait(20)

    driver.find_element_by_tag_name('input').send_keys(FileType)
    driver.implicitly_wait(10)

    driver.find_element_by_class_name("file-link").click()
    driver.implicitly_wait(20)

    Table = driver.find_elements_by_tag_name("tr")
    UUID = 0
    for file in Table:
        row = file.text
        if(len(row) > 0):
            size = file.find_element_by_class_name("file-ext").text
            size = size.replace(" ","")
            link = file.find_element_by_class_name("download-button").get_attribute("href")
            print("Size: ", size)
            print("Link: ", link)
            TimeStamp = time.strftime("%d-%m-%Y-%H-%M-%S")
            FileName = TimeStamp + "_" + str(UUID) + "_" + size + "." + FileType
            UUID = UUID + 1
            r = requests.get(link, stream=True)
            with open(FileName, 'wb') as f:
                f.write(r.content)
    driver.quit()
