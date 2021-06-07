from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#Opens Chrome to free-images.com
driver = webdriver.Chrome()
driver.get("https://free-images.com")

searchbar = driver.find_element_by_xpath('//*[@id="sbar"]/form/table/tbody/tr/td[1]/input')

#Sends search query to searchbar
searchbar.send_keys('kittens')
searchbar.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(EC.url_contains("https://free-images.com/search/?q"))

#Finds and prints the address of each search result on the first page
results = driver.current_url

pics = results.find_elements_by_tag_name('img')

#spot = 0
for pic in pics:
    addy = pic.get_attribute('src')
    print(addy)
    #if ".jpg" in addy:
    #   driver.get(pic.get_attribute('src'))
     #  break
     #Skips the webpage's design elements and takes the first definition picture
#    spot = spot + 1
#    if spot > 0:
#      print(pic.get_attribute('src'))
#       driver.get(pic.get_attribute('src'))
#//*[@id="sbtc"]/div/div[2]/input
driver.close()