import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions

op = ChromeOptions()
op.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=op)

driver.maximize_window()
driver.implicitly_wait(50)
driver.get(url="https://www.facebook.com/")

for i in range(0, 5):
    print(i)

