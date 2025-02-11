from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

def visit_website(url, min_duration=30, max_duration=180):
    # Настройка Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless') 

    try:
        driver = webdriver.Chrome(options=chrome_options)

        # Открытие сайта
        driver.get(url)

        duration = random.randint(min_duration, max_duration)

        for _ in range(random.randint(3, 8)):
            scroll_amount = random.randint(100, 700)
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            sleep(random.randint(2, 8))

        sleep(duration)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()

def main():
    url = "https://vision-ai.org/" 

    while True:
        try:
            visit_website(url)
            sleep_time = random.randint(60, 300)
            print(f"Ожидание {sleep_time} секунд до следующего посещения...")
            sleep(sleep_time)

        except KeyboardInterrupt:
            print("\nСкрипт остановлен пользователем")
            break

if __name__ == "__main__":
    main()
