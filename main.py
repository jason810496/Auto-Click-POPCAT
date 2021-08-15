from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time


# set Webdriver default options
opts = Options()
opts.add_argument("user-data-dir=~/.config/google-chrome/Default") 
opts.add_argument("--disable-notifications")
opts.add_argument("--disable-popup-blocking")
opts.add_argument('--no-sandbox')
opts.add_argument("start-maximized")


driver = webdriver.Chrome("/home/jason/Desktop/Webdriver_test/chromedriver" , chrome_options=opts)

CLICK_TIME=1000

try:
    driver.get("https://popcat.click/") 
    # wait to connect to POPCAT
    time.sleep(2)
    # U can either select by id , tag , xpath , etc...
    broswer = driver.find_element_by_class_name('cat-img.p')

    # how huch time U want to click ! 
    for i in range( CLICK_TIME ):
        broswer.click()
except:
    print("Your Wifi suck !")

# done
