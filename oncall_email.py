from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

import getpass

options = Options()
options.headless = True

user = input("Username: ") 
pw = getpass.getpass("Password: ")


driver = webdriver.Firefox()
driver.get("https://vplanner.dst.ibm.com/team/index/60665/")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "dijitDialogCloseIcon")))
driver.find_element_by_class_name("dijitDialogCloseIcon").click()
inputUsername = driver.find_element_by_name("email")
inputUsername.send_keys(user)
driver.find_element_by_name("password").send_keys(pw)
driver.find_element_by_name("submit").click()
driver.find_element_by_class_name("dijitDialogCloseIcon").click()
