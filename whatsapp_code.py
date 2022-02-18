from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Replace below path with the absolute path
browser = webdriver.Firefox()

phone = ["78s34873405","+917888734439405","+917843488739405"]
message = "questo è il messaggio"

for i in phone:
    url = "https://web.whatsapp.com/send?phone="+ i + "&text=" + message + "&app_absent=1"
    time.sleep(5)

    # Load Whatsapp Web page
    browser.get(url)
    # time.sleep(5)

    # Wait for the page be loaded
    time.sleep(10)

    enter_action = ActionChains(browser)
    time.sleep(5)
    enter_action.send_keys(Keys.ENTER)
    time.sleep(5)

# Send message
    enter_action.perform()
    time.sleep(5)

# Close browser
browser.close()
