from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest

# driver setup
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

name = "testName testSurname"
mail = "test@mail.com"

driver.get(r"https://sourceful.nl/nl/contact-pl/")
nameForm = driver.find_element(By.XPATH, '//*[@id="wpcf7-f1781-p1200-o1"]/form/p[1]/label/span/input')

mailForm = driver.find_element(By.XPATH, '//*[@id="wpcf7-f1781-p1200-o1"]/form/p[2]/label/span/input')

submitButton = driver.find_element(By.XPATH,'//*[@id="wpcf7-f1781-p1200-o1"]/form/p[6]/input')

nameForm.send_keys(name)
mailForm.send_keys(mail)
submitButton.click()


