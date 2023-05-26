from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
# Set up the Chrome WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the login page
driver.get("https://www.google.com/")
driver.get("https://www.google.com/") #used to search web pages wit .get you can get into the links 
driver.maximize_window() #maximizes the window
time.sleep(3) #waits or stands for n secound for further command to execute
driver.find_element("name", "q").send_keys("LambdaTest Login") 
driver.find_element("name", "q").send_keys(Keys.ENTER) #find_element you can find by id,or you can find by xpath
driver.find_element("partial link text", "Log in - LambdaTest").click()
driver.find_element("id","email").send_keys("ritamg@lambdatest.com") #send keys is used to used to send elements log or files or text to the web app
driver.find_element("id","password").send_keys("Shiva@12")
driver.find_element("id", "login-button").click()
time.sleep(10)
driver.quit() #please always quit the driver so that it doent reaches ideal time out
