# tests/test_login.py
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # comment out if you want to see browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver

def take(name, driver):
    os.makedirs("artifacts", exist_ok=True)
    path = f"artifacts/{name}.png"
    driver.save_screenshot(path)
    print("Saved screenshot:", path)

def test_login_valid():
    driver = setup_driver()
    try:
        driver.get("https://example-login-page.com/login")  # replace with your login page URL
        # locate fields (update selectors to match your page)
        driver.find_element(By.NAME, "username").send_keys("valid_user")
        driver.find_element(By.NAME, "password").send_keys("valid_password")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        take("valid_login", driver)
        # assert login success — adjust to your site (presence of logout button, dashboard text)
        assert "dashboard" in driver.current_url.lower() or driver.find_elements(By.ID, "logout")
    finally:
        driver.quit()

def test_login_invalid():
    driver = setup_driver()
    try:
        driver.get("https://example-login-page.com/login")
        driver.find_element(By.NAME, "username").send_keys("invalid_user")
        driver.find_element(By.NAME, "password").send_keys("bad_password")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        take("invalid_login", driver)
        # check for error message existence — adjust selector
        errors = driver.find_elements(By.CLASS_NAME, "error")
        assert len(errors) > 0
    finally:
        driver.quit()
