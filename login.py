from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium. webdriver. support. wait import WebDriverWait

# This piece of code will not close the web browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

#This code will open the website on the web browser
driver.get('https://practicesoftwaretesting.com/')

# This piece of code solves the issue when cursor is not moving to email and password field because it was not waiting for it.
wait = WebDriverWait(driver, 50)

#Click a sign-on button
login = driver.find_element("xpath", '//*[@id="navbarSupportedContent"]/ul/li[4]/a')
login.click()

# This piece of code solves the issue when cursor is not moving to email and password field because it was not waiting for it.
wait1 = WebDriverWait(driver, 50)
#enter email
driver.find_element("xpath", '//*[@id="email"]').send_keys("beautyinyoubyng3@gmail.com")
#enter password
driver.find_element("xpath", "//*[@id='password']//div//input").send_keys("gulla@10Nyra")
#Click on Login button
Login = driver.find_element("xpath", '/html/body/app-root/div/app-login/div/div/div/form/div[3]/input')
Login.click()
















