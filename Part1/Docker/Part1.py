from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

# Search Function
def Search(Location, StartDate, EndDate, Adults, Children, RoomsRequired):
    # Entering the Location
    driver.find_element_by_id('ss').send_keys(Location)

    # Select Dates
    driver.find_element_by_class_name("xp__dates-inner").click()
    driver.find_element_by_css_selector("[data-date='" + StartDate + "']").click()
    driver.find_element_by_css_selector("[data-date='" + EndDate + "']").click()

    # Opening the drop down
    driver.find_element_by_id('xp__guests__toggle').click()

    # Adult Button
    Adult_Element = driver.find_element_by_class_name("sb-group__field-adults").find_element_by_class_name("bui-stepper").find_element_by_class_name("sb-group__stepper-a11y")
    Adults_Count = Adult_Element.find_element_by_class_name("bui-stepper__display")
    Adults_Count = int(Adults_Count.text)
    Adults_Button = Adult_Element.find_element_by_class_name("bui-stepper__add-button ")
    # Incrementing Adult Count if it is less than our desired value
    while(Adults_Count < Adults):
        Adults_Button.click()
        Adults_Count = Adults_Count + 1

    # Child Button
    Child_Element = driver.find_element_by_class_name("sb-group-children").find_element_by_class_name("bui-stepper").find_element_by_class_name("sb-group__stepper-a11y")
    Child_Count = Child_Element.find_element_by_class_name("bui-stepper__display")
    Child_Count = int(Child_Count.text)
    Child_Button = Child_Element.find_element_by_class_name("bui-stepper__add-button ")
    # Incrementing Child Count if it is less than our desired value
    while(Child_Count < Children):
        Child_Button.click()
        Child_Count = Child_Count + 1

    # Room Button
    Room_Element = driver.find_element_by_class_name("sb-group__field-rooms").find_element_by_class_name("bui-stepper").find_element_by_class_name("sb-group__stepper-a11y")
    Room_Count = Room_Element.find_element_by_class_name("bui-stepper__display")
    Room_Count = int(Room_Count.text)
    Room_Button = Room_Element.find_element_by_class_name("bui-stepper__add-button ")
    # Incrementing Room Count if it is less than our desired value
    while(Room_Count < RoomsRequired):
        Room_Button.click()
        Room_Count = Room_Count + 1

    # Submit button
    Submit_Element = driver.find_element_by_class_name("xp__button")
    Submit_Button = Submit_Element.find_element_by_class_name("sb-searchbox__button")
    # Submit to see the results
    Submit_Button.click()
    driver.implicitly_wait(10)

def FilterAndSort():
    # Sorting by Star Rating and Price
    try:
        driver.find_element_by_class_name("sort_class_and_price").click()
    except:
        pass
    try:
        driver.find_element_by_class_name("sort_review_score_and_price").click()
    except:
        pass
    try:
        driver.find_element_by_css_selector("[data-catagory='review_score_and_price']").click()
    except:
        pass
    try:
        driver.find_element_by_css_selector("[data-id='class_and_price']").click()
    except:
        pass
    try:
        driver.find_element_by_css_selector("[data-id='review_score_and_price']").click()
    except:
        pass
    driver.implicitly_wait(60)

    # Filter options
    Hotel = driver.find_element_by_css_selector("[data-id='ht_id-204']")
    Hotel.click()
    driver.implicitly_wait(15)
    # Filter to see only those with score of 8+
    Score = driver.find_element_by_css_selector("[data-id='review_score-80']")
    Score.click()
    driver.implicitly_wait(15)
    # Filter to see rooms with Air conditioning
    Room_AC = driver.find_element_by_css_selector("[data-id='roomfacility-11']")
    Room_AC.click()
    driver.implicitly_wait(15)
    # Filter to be in Downtown Barcelona
    District = driver.find_element_by_css_selector("[data-id='di-2287']")
    District.click()
    driver.implicitly_wait(15)

    # Refreshing the page
    driver.refresh()
    driver.implicitly_wait(100)

def GetResults(NumberOfResults):
    # Getting the results
    Heading = driver.find_element_by_class_name("sr_header").text
    # print(Heading)
    Heading_Temp = Heading.split()
    Num_Prop = int(Heading_Temp[1])
    print("Number: ", Num_Prop)

    # Properties
    Results = driver.find_elements_by_class_name("sr_property_block")
    PropIter = 0
    while(PropIter < NumberOfResults):
        PropertyTitle = Results[PropIter].find_element_by_class_name("sr-hotel__name").text
        PropPrice = Results[PropIter].find_element_by_class_name("bui-price-display__value").text
        PropReview = Results[PropIter].find_element_by_class_name("bui-review-score__text").text
        PropScore = Results[PropIter].find_element_by_class_name("bui-review-score__badge").text
        PropLoc = Results[PropIter].find_element_by_class_name("sr_card_address_line").find_element_by_tag_name('a').text
        if " Show on map" in PropLoc:
            PropLoc = PropLoc.replace(" Show on map", "")
        PropImg = Results[PropIter].find_element_by_class_name("hotel_image").get_attribute("src")
        print("--------------------------------------------------------------------")
        print("Title: ", PropertyTitle, "\nPrice: ", PropPrice, "\nReview: ", PropReview)
        print("Score: ", PropScore, "\nLocation: ", PropLoc)
        print("Source: ", PropImg)
        print("--------------------------------------------------------------------")
        PropIter = PropIter + 1

if __name__ == '__main__':
    # webdriver
    # PATH = "C:\Program Files (x86)\chromedriver.exe"
    USER_AGENT_LIST = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
    ]
    userAgent = "user-agent=" + random.choice(USER_AGENT_LIST)

    opts = Options()
    opts.add_argument('--no-sandbox')
    opts.add_argument('--headless')
    opts.add_argument(userAgent)
    opts.add_argument("window-size=1200,800")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option('useAutomationExtension', False)
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=opts)
    # Search criteria
    Location = "barcelona"
    Adults = 2
    Children = 2
    RoomsRequired = 1
    StartDate = "2020-11-20"
    EndDate = "2020-11-27"

    # Filter criteria
    Property = "hotel"
    Review = "+8"
    Facilities = "air conditioning"
    District = "Downtown Barcelona"

    # Going to the website
    driver.get("https://booking.com/")
    driver.implicitly_wait(10)

    Search(Location, StartDate, EndDate, Adults, Children, RoomsRequired)

    FilterAndSort()

    GetResults(5)

    driver.quit()
