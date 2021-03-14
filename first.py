from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test", Keys.RETURN)

time.sleep(10)

driver.quit()
