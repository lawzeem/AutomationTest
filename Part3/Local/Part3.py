from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

def TakeScreenshot(counter):
    ScreenshotName = "screenshot_" + str(counter) + ".png"
    driver.save_screenshot(ScreenshotName)
    print("Saved : ", ScreenshotName)
    return counter + 1

def GoToLinks(ListOfLinks, ScreenshotCounter):
    for Link in ListOfLinks:
        LinkClass = links[Link]
        driver.implicitly_wait(20)
        LinkURL = driver.find_element_by_class_name(LinkClass).find_element_by_tag_name("a").get_attribute("href")
        driver.get(LinkURL)
        driver.implicitly_wait(20)
        ScreenshotCounter = TakeScreenshot(ScreenshotCounter)

if __name__ == '__main__':
    PATH = "C:\Program Files (x86)\chromedriver.exe"

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

    driver = webdriver.Chrome(options=opts, executable_path=PATH)

    driver.get("https://www.wmphvacations.com/")
    ug_verif = driver.execute_script("return navigator.userAgent;")
    print("Browser: ", ug_verif)
    driver.implicitly_wait(30)

    driver.find_element_by_tag_name("a").click()
    driver.implicitly_wait(10)
    ScreenshotCounter = TakeScreenshot(0)

    links = {
        "customer experience" : "menu-item-2570",
        "leaders" : "menu-item-2572",
        "news" : "menu-item-2574",
        "careers" : "menu-item-2573",
        "contact us" : "menu-item-2575"
    }

    ListOfLinks = ["customer experience", "leaders", "careers"]

    GoToLinks(ListOfLinks, ScreenshotCounter)

    driver.quit()
