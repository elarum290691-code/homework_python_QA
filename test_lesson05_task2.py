from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    try:
        start_url = "https://httpbin.org/forms/post"

        driver.get(start_url)

        name_field = driver.find_element(By.NAME, "custname")
        name_field.send_keys("Валентин")

        submit_button = driver.find_element(
            By.XPATH,
            "//button[normalize-space()='Submit']",
        )
        submit_button.click()

        assert driver.current_url != start_url
    finally:
        driver.quit()
