from robocorp.tasks import task
from robocorp import browser
import requests
from bs4 import BeautifulSoup

@task
def fetch_price():

    browser.configure(
        browser_engine="chromium",
        screenshot="only-on-failure",
        headless=True
        #slowmo=2000,        
    )
    # The URL of the product page you want to scrape
    # product_url = "https://www.verkkokauppa.com/fi/product/926983/Asus-AMD-Radeon-DUAL-RX7800XT-O16G-naytonohjain#list=OZCYkR8mw3qLYgY1LOT4k8bVCD8AFDJLYRst6TS0c8s1Oq8rShn8Aed58rfNJ8Ibcv8mwfb6Q9dELz7TKLl9X9LVYAb8IATz6QZCsLOTINLOTQF8rpXb8Q5ib8rfBa8As60YENo0Lk552LZvIHLHviK8QhHj86I8H8IAB58s18HLVY7K6fi6980BlF6tkLE8rSXa62IME6esyJ8WmXz8PtUWqJUY08rj0J8rah162sOvLOBik8IbNcr"
    product = "7800XT Näytönohjain"
    link = "https://www.verkkokauppa.com/fi/product/926983/Asus-AMD-Radeon-DUAL-RX7800XT-O16G-naytonohjain#list=OZCYkR8mw3qLYgY1LOT4k8bVCD8AFDJLYRst6TS0c8s1Oq8rShn8Aed58rfNJ8Ibcv8mwfb6Q9dELz7TKLl9X9LVYAb8IATz6QZCsLOTINLOTQF8rpXb8Q5ib8rfBa8As60YENo0Lk552LZvIHLHviK8QhHj86I8H8IAB58s18HLVY7K6fi6980BlF6tkLE8rSXa62IME6esyJ8WmXz8PtUWqJUY08rj0J8rah162sOvLOBik8IbNcr"
    page = browser.goto(link)
    try:
        # response = requests.get(product_url)
        # response.raise_for_status()  # Raise an error for bad HTTP responses

        # soup = BeautifulSoup(response.text, 'html.parser')
        
        # price_element = soup.select_one("data.sc-jnOGJG liCZew")  #class
        # if price_element:
        #     price = price_element.get_text(strip=True)
        #     print(f"The current price of the product is: {price}")
        # else:
        #     print("Price element not found. Please check the selector.")
        hinta = page.locator(".jeFktI .sc-jnOGJG").text_content()
        print(hinta)
        print(product + " " + hinta + " " + link)
        send_message(product + " " + hinta + " " + link)
        

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the product page: {e}")

def send_message(mes):
    TOKEN = ""
    chat_id = ""
    message = mes
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message