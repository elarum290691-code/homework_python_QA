from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.org/forms/post")

        start_url = driver.current_url

        name = driver.find_element(By.NAME, "custname")
        name.send_keys("Валентин")

        submit = driver.find_element(By.XPATH, "//button[text()='Submit']")
        submit.click()

        assert driver.current_url != start_url

    finally:
        driver.quit()
