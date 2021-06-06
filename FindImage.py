from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://images.google.com")

searchbar = driver.find_elements_by_tag_name('input')

searchbar.send_keys('kittens')
searchbar.send_keys(Keys.ENTER)


#pics = driver.find_elements_by_tag_name('img')

#spot = 0
#for pic in pics:
#    addy = pic.get_attribute('src')
#    if ".jpg" in addy:
#        driver.get(pic.get_attribute('src'))
#        break
     #Skips the webpage's design elements and takes the first definition picture
#    spot = spot + 1
#    if spot > 0:
#      print(pic.get_attribute('src'))
#       driver.get(pic.get_attribute('src'))
#i hate this