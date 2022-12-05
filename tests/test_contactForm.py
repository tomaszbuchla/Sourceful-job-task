from page_objects.contact_page import contactPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
import time



@pytest.fixture()
def test_setup():
    global driver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()


def test_sendForm(test_setup):
    driver.get(contactPage.adress)
    driver.find_element(By.ID, contactPage.cookieForm).click()
    driver.find_element(By.NAME, contactPage.nameForm).send_keys(contactPage.name)
    driver.find_element(By.CLASS_NAME, contactPage.mailForm).send_keys(contactPage.mail)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,contactPage.buttonForm).click()
    time.sleep(5)
    confirm = driver.find_element(By.CLASS_NAME,contactPage.confirmForm)
    assert confirm.is_displayed and confirm.text == contactPage.expectedPositiveOutput



