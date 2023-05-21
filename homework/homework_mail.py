import time
import requests
import selectorlib
from datetime import datetime
import smtplib, ssl
import os

URL = "http://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def take_data_from_url(url):
    response = requests.get(url)
    source = response.text
    return source


def extracted_data_from_page(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperatures"]
    return value


def save_data_in_txtfile(value, time):
    with open("/Users/oles/Documents/Python/app-10-scraping-sql/homework/homework_data.txt", "a") as file:
        file.write(f"{time},{value}\n")


now_time = datetime.now().strftime("%y-%m-%d-%H-%M-%S")


if __name__ == "__main__":
    all_data_from_url = take_data_from_url(URL)
    extracted_data = extracted_data_from_page(all_data_from_url)
    save_data_in_txtfile(extracted_data, now_time)
    print(extracted_data)

