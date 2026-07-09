from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        driver.get("https://gitflic.ru/")

        # Cookie пользователя 1
        driver.add_cookie(
            {
                "name": "SESSION",
                "value": "NDEzMzFkYmEtZjE0Ny00YTg0LWE1YTUtMmE4NTViNDUxZDM5",
                "domain": "gitflic.ru",
                "path": "/",
            }
        )

        driver.add_cookie(
            {
                "name": "X-CSRF-TOKEN",
                "value": "a1802a7d-5d35-41f7-bf7c-f1262bb0afd4",
                "domain": "gitflic.ru",
                "path": "/",
            }
        )

        driver.refresh()

        driver.get(
            "https://gitflic.ru/user/valentin-kravchenko-skyeng-ru"
        )
        user1_url = driver.current_url

        # Разлогиниваемся
        driver.delete_all_cookies()

        driver.get("https://gitflic.ru/")

        # Cookie пользователя 2
        driver.add_cookie(
            {
                "name": "SESSION",
                "value": "ZjU5NDE0ODUtNTJmOC00NmMzLTg5OTEtYTM5ZGQzZjk2N2E5",
                "domain": "gitflic.ru",
                "path": "/",
            }
        )

        driver.add_cookie(
            {
                "name": "X-CSRF-TOKEN",
                "value": "cf5a1584-bb19-4ec4-ad40-839d7bfc0a78",
                "domain": "gitflic.ru",
                "path": "/",
            }
        )

        driver.refresh()

        driver.get("https://gitflic.ru/user/valentin3113")
        user2_url = driver.current_url

        assert user1_url != user2_url

    finally:
        driver.quit()
