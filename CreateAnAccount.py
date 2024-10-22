from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# This piece of code will not close the web browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

#This code will open the website on the web browser
driver.get('https://practicesoftwaretesting.com/auth/login')

# This piece of code solves the issue when cursor is not moving to email and password field because it was not waiting for it.
wait = WebDriverWait(driver, 50)

#Click a sign-on button
CreateAccount = driver.find_element("xpath", '/html/body/app-root/div/app-login/div/div/div/form/div[4]/p/a[1]')
CreateAccount.click()

# fill the fields as email and password
#first_name
driver.find_element("xpath", '//*[@id="first_name"]').send_keys("Nyra")
#last_name
driver.find_element("xpath", '//*[@id="last_name"]').send_keys("Gupta")
#DOB
driver.find_element("xpath", '//*[@id="dob"]').send_keys("12/16/1989")
#Address
driver.find_element("xpath", '//*[@id="address"]').send_keys("12125 caddy row")
#postcode
driver.find_element("xpath", '//*[@id="postcode"]').send_keys("92128")
#City
driver.find_element("xpath", '//*[@id="city"]').send_keys("san diego")
#State
driver.find_element("xpath", '//*[@id="state"]').send_keys("CA")
#Country
driver.find_element("xpath", '//*[@id="country"]').send_keys("United States of America (the)")
#Phone
driver.find_element("xpath", '//*[@id="phone"]').send_keys("6199910383")
#Email
driver.find_element("xpath", '//*[@id="email"]').send_keys("automationdemo@gmail.com")
#enter password
driver.find_element("xpath", "//*[@id='password']//div//input").send_keys("gulla@10Nyra")

#Click on Create Account button
Create = driver.find_element("xpath", '/html/body/app-root/div/app-register/div/div/div/form/div/button')
Create.click()
















