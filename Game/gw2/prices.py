from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time


def load_website():
    chrome_driver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'
    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service)
    driver.get('https://www.gw2tp.com/item/19722-elder-wood-log')

    time.sleep(10)
    html_content = driver.page_source
    driver.quit()

    return html_content


def get_table(website):
    soup = BeautifulSoup(website, 'html.parser')
    table = soup.find("tbody", id="sell-orders")

    if table:
        tr_elements = table.find_all("td", limit=80)

        prices = []
        supplies = []

        i = 0
        max_iteration = 20 * 3

        while i < max_iteration:
            price = (tr_elements[i]).getText()
            supply = (tr_elements[i + 1]).getText()

            prices.append(price)
            supplies.append(supply)

            print(price + " " + supply)
            i += 3

        return prices, supplies

    else:  # Load data again
        print("Load data again.")
        return False


html_content = load_website()
get_table(html_content)
