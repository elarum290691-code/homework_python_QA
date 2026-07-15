from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_form():
    driver = webdriver.Edge()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.visibility_of_element_located((By.NAME, "first-name"))
        ).send_keys("Иван")

        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys(
            "test@skypro.com"
        )
        driver.find_element(By.NAME, "phone").send_keys(
            "+7985899998787"
        )

        # Поле Zip code оставляем пустым

        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        wait.until(
            EC.visibility_of_element_located((By.ID, "zip-code"))
        )

        zip_code = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code.get_attribute("class")

        valid_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]

        for field in valid_fields:
            element = driver.find_element(By.ID, field)
            assert "alert-success" in element.get_attribute("class")

    finally:
        driver.quit()
