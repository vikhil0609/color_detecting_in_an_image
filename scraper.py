from selenium import webdriver

path = 'C:\web_drivers\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get("https://www.w3schools.com/colors/colors_rgb.asp")
text_area = driver.find_element_by_id("rgb01")
text_area.send_keys("hello")
text_area.clear()
