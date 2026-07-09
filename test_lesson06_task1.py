from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://the-internet.herokuapp.com/dynamic_loading/2"
        )

        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        hello_world = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        driver.save_screenshot("dynamic_loading_result.png")

        assert hello_world.text == "Hello World!"

    finally:
        driver.quit()
