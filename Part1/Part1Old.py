from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Search criteria
Location = "barcelona"
Adults = 2
Children = 2
StartDate = "2020-11-20"
EndDate = "2020-11-27"

# Filter results
Property = "hotel"
Review = "+8"
Facilities = "air conditioning"
District = "Downtown Barcelona"

# Going to the website
driver.get("https://booking.com/")
driver.implicitly_wait(10)
# Entering the Location
driver.find_element_by_id('ss').send_keys(Location)

# Select Dates
driver.find_element_by_class_name("xp__dates-inner").click()
driver.find_element_by_css_selector("[data-date='"+StartDate+"']").click()
driver.find_element_by_css_selector("[data-date='"+EndDate+"']").click()

# Opening the drop down
driver.find_element_by_id('xp__guests__toggle').click()

# Adult Button
Adult_Element = driver.find_element_by_class_name("sb-group__field-adults").find_element_by_class_name("bui-stepper").find_element_by_class_name("sb-group__stepper-a11y")
Adults_Count = Adult_Element.find_element_by_class_name("bui-stepper__display")
Adults_Count = int(Adults_Count.text)
print("Adults: ", Adults_Count)
Adults_Button = Adult_Element.find_element_by_class_name("bui-stepper__add-button ")
# Incrementing Adult Count if it is less than our desired value
while(Adults_Count < Adults):
    Adults_Button.click()
    Adults_Count = Adults_Count + 1

# Child Button
Child_Element = driver.find_element_by_class_name("sb-group-children").find_element_by_class_name("bui-stepper").find_element_by_class_name("sb-group__stepper-a11y")
Child_Count = Child_Element.find_element_by_class_name("bui-stepper__display")
Child_Count = int(Child_Count.text)
print("Children: ", Child_Count)
Child_Button = Child_Element.find_element_by_class_name("bui-stepper__add-button ")
# Incrementing Child Count if it is less than our desired value
while(Child_Count < Children):
    Child_Button.click()
    Child_Count = Child_Count + 1

# Submit button
Submit_Element = driver.find_element_by_class_name("xp__button")
Submit_Button = Submit_Element.find_element_by_class_name("sb-searchbox__button")
# Submit to see the results
Submit_Button.click()
driver.implicitly_wait(10)

# Sort by Star rating and price
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
# Filter to see only those with score of 8+
Score = driver.find_element_by_css_selector("[data-id='review_score-80']")
# Filter to see rooms with Air conditioning
Room_AC = driver.find_element_by_css_selector("[data-id='roomfacility-11']")
# Filter to be in Downtown Barcelona
District = driver.find_element_by_css_selector("[data-id='di-2287']")

# Clicking the options and wait
Hotel.click()
driver.implicitly_wait(15)
Score.click()
driver.implicitly_wait(15)
Room_AC.click()
driver.implicitly_wait(15)
District.click()
driver.implicitly_wait(15)
driver.refresh()
driver.implicitly_wait(100)

# Getting the results
Heading = driver.find_element_by_class_name("sr_header").text
print(Heading)
Heading_Temp = Heading.split()
Num_Prop = int(Heading_Temp[1])
print("Number: ", Num_Prop)

# Properties
Results = driver.find_elements_by_class_name("sr_property_block")

for Prop in Results:
    PropertyTitle = Prop.find_element_by_class_name("sr-hotel__name")
    PropPrice = Prop.find_element_by_class_name("bui-price-display__value")
    PropReview = Prop.find_element_by_class_name("bui-review-score__text")
    PropScore = Prop.find_element_by_class_name("bui-review-score__badge")
    PropLoc = Prop.find_element_by_class_name("sr_card_address_line").find_element_by_tag_name('a')
    PropImg = Prop.find_element_by_class_name("hotel_image").get_attribute("src")
    print("--------------------------------------------------------------------")
    print("Title: ", PropertyTitle.text, " === Price: ", PropPrice.text, "Review: ", PropReview.text)
    print("Score: ", PropScore.text, " === Location: ", PropLoc.text)
    print("Source: ", PropImg)
    print("--------------------------------------------------------------------")

# Search Function
def search():
    Location = "barcelona"
    Adults = 2
    Children = 2
    StartDate = "2020-11-20"
    EndDate = "2020-11-27"

    # Filter results
    Property = "hotel"
    Review = "+8"
    Facilities = "air conditioning"
    District = "Downtown Barcelona"

    # Going to the website
    driver.get("https://booking.com/")
    driver.implicitly_wait(10)
    # Entering the Location
    driver.find_element_by_id('ss').send_keys(Location)

    # Select Dates
    driver.find_element_by_class_name("xp__dates-inner").click()
    driver.find_element_by_css_selector("[data-date='"+StartDate+"']").click()
    driver.find_element_by_css_selector("[data-date='"+EndDate+"']").click()

    # Opening the drop down
    driver.find_element_by_id('xp__guests__toggle').click()

    # Adult Button
    Adult_Element = driver.find_element_by_class_name("sb-group__field-adults").find_element_by_class_name("bui-stepper").find_element_by_class_name("sb-group__stepper-a11y")
    Adults_Count = Adult_Element.find_element_by_class_name("bui-stepper__display")
    Adults_Count = int(Adults_Count.text)
    print("Adults: ", Adults_Count)
    Adults_Button = Adult_Element.find_element_by_class_name("bui-stepper__add-button ")
    # Incrementing Adult Count if it is less than our desired value
    while(Adults_Count < Adults):
        Adults_Button.click()
        Adults_Count = Adults_Count + 1

    # Child Button
    Child_Element = driver.find_element_by_class_name("sb-group-children").find_element_by_class_name("bui-stepper").find_element_by_class_name("sb-group__stepper-a11y")
    Child_Count = Child_Element.find_element_by_class_name("bui-stepper__display")
    Child_Count = int(Child_Count.text)
    print("Children: ", Child_Count)
    Child_Button = Child_Element.find_element_by_class_name("bui-stepper__add-button ")
    # Incrementing Child Count if it is less than our desired value
    while(Child_Count < Children):
        Child_Button.click()
        Child_Count = Child_Count + 1

    # Submit button
    Submit_Element = driver.find_element_by_class_name("xp__button")
    Submit_Button = Submit_Element.find_element_by_class_name("sb-searchbox__button")
    # Submit to see the results
    Submit_Button.click()
    driver.implicitly_wait(10)

def FilterAndSort():
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
    # Filter to see only those with score of 8+
    Score = driver.find_element_by_css_selector("[data-id='review_score-80']")
    # Filter to see rooms with Air conditioning
    Room_AC = driver.find_element_by_css_selector("[data-id='roomfacility-11']")
    # Filter to be in Downtown Barcelona
    District = driver.find_element_by_css_selector("[data-id='di-2287']")

    # Clicking the options and wait
    Hotel.click()
    driver.implicitly_wait(15)
    Score.click()
    driver.implicitly_wait(15)
    Room_AC.click()
    driver.implicitly_wait(15)
    District.click()
    driver.implicitly_wait(15)
    driver.refresh()
    driver.implicitly_wait(100)

# FilterCriteria = {
#     "apartments":"[data-id='ht_id-201']",
#     "hotels":"[data-id='ht_id-204']",
#     "family-friendly":"[data-id='family_friendly_property-1']",
#     "guesthouses":"[data-id='ht_id-216']",
#     "hostels":"[data-id='ht_id-203']",
#     "boats":"[data-id='ht_id-215']",
#     "bed-and-breakfast":"[data-id='ht_id-208']",
#     "vacation-homes":"[data-id='ht_id-220']",
#     "homestays":"[data-id='ht_id-222']",
#     "villas":"[data-id='ht_id-213']",
#     "student-accomodations":"[data-id='ht_id-235']"
# }

# def Filter(ListOfFilters):
#     for Filter in ListOfFilters:
#         driver.implicitly_wait(20)
#         driver.find_element_by_css_selector("[" + Filter + "]").click()
#         driver.implicitly_wait(20)
#     driver.refresh()
#     driver.implicitly_wait(100)
if __name__ == '__main__':
    main()
