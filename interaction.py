from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.quit()
#
# a = driver.find_element(By.CSS_SELECTOR, "#articlecount a" )
#
# all_portals = driver.find_element(By.LINK_TEXT, "Wikiversity")
# #all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# #search.send_keys("python\ue007")
#


driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_name.send_keys("Sudharson")

second_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
second_name.send_keys("S")

email = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email.send_keys("suda@gmail.com")


submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()

driver.quit()