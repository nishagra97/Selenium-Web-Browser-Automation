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
wait = WebDriverWait(driver, 90)

#Click a sign-on button
login1 = driver.find_element("xpath", '//*[@id="navbarSupportedContent"]/ul/li[4]/a')
login1.click()

# This piece of code solves the issue when cursor is not moving to email and password field because it was not waiting for it.
driver.implicitly_wait(20)
#enter email
driver.find_element("xpath", '//*[@id="email"]').send_keys("automation@gmail.com")

#enter password
driver.find_element("xpath", "//*[@id='password']//div//input").send_keys("gulla@10Nyra")

#Click on Login button
Login = driver.find_element("xpath", '/html/body/app-root/div/app-login/div/div/div/form/div[3]/input')
Login.click()
driver.implicitly_wait(90)

#click  on Categories
categories=driver.find_element("xpath", '//*[@id="navbarSupportedContent"]/ul/li[2]/a')
categories.click()
driver.implicitly_wait(110)

#click  on hand tool
pg=driver.find_element("xpath", '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[1]/a')
pg.click()
#When you face an error "NoSuchElementException" you put implicit wait
driver.implicitly_wait(110)

#click on product
Pro=driver.find_element("xpath", '/html/body/app-root/div/app-category/div[2]/div[2]/div[1]/a[1]/div[1]/img').click()
#When you face an error "NoSuchElementException" you put implicit wait
driver.implicitly_wait(110)

#Add to cart
cart1=driver.find_element("xpath", '//*[@id="btn-add-to-cart"]')
print("clicked add to cart")
cart1.click()
driver.implicitly_wait(110)

#click on cart
cart3=driver.find_element("xpath", '//*[@id="lblCartCount"]')
driver.implicitly_wait(1000)
print("Card count")
cart3.click()
driver.implicitly_wait(110)

#proceed to checkout
checkout=driver.find_element("xpath", '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[1]/app-cart/div/div/button')
checkout.click()
driver.implicitly_wait(100)

driver.implicitly_wait(90)
#Click on Login button
#Login = driver.find_element("xpath", '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[2]/app-login/div/div/div/div/form/div[3]/input')
#Login.click()
driver.implicitly_wait(90)

#Proceed to checkout
checkout = driver.find_element("xpath", '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[2]/app-login/div/div/div/div/button')
driver.implicitly_wait(90)
checkout.click()
driver.implicitly_wait(90)

#checkout
checkout2 = driver.find_element("xpath", '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[1]/app-cart/div/div/button')
#driver.implicitly_wait(90)
checkout2.click()
#driver.implicitly_wait(90)

#Billing Address
driver.find_element("xpath", '//*[@id="address"]').send_keys("12125 caddy row")
driver.implicitly_wait(90)
driver.find_element("xpath", '//*[@id="city"]').send_keys("san diego")
driver.implicitly_wait(90)
driver.find_element("xpath", '//*[@id="state"]').send_keys("CA")
driver.implicitly_wait(90)
driver.find_element("xpath", '//*[@id="country"]').send_keys("US")
driver.implicitly_wait(90)
driver.find_element("xpath", '//*[@id="postcode"]').send_keys("92128")
driver.implicitly_wait(90)
checkout1 = driver.find_element("xpath", '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[3]/app-address/div/div/div/div/button')
driver.implicitly_wait(90)
checkout1.click()

#payment
#choose your payment method

driver.find_element("xpath", '//*[@id="payment-method"]')
confirm = driver.find_element("xpath", '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-completion-step/app-payment/div/div/div/div/button')
confirm.click()





















