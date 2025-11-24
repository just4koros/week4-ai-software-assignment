from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login():
    # Correct Selenium 4 driver setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter valid username
    driver.find_element(By.ID, "username").send_keys("student")

    # Enter valid password
    driver.find_element(By.ID, "password").send_keys("Password123")

    # Click login
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    print("Logged in page title:", driver.title)

    driver.quit()


if __name__ == "__main__":
    test_login()
