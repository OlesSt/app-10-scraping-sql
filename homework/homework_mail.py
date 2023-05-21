import requests
import selectorlib
from datetime import datetime
import sqlite3

connection = sqlite3.connect("data.db")

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
# def extract_data_from_database(source, time):
#     rows = source.split(',')
#     rows = [item.strip() for items in rows]
#     date, temp = rows
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM events WHERE time=? AND temperature=?", (time, temp))
#     row = cursor.fetchall()
#     print(row)
#     return row



# def save_data_in_txtfile(value, time):
#     with open("/Users/oles/Documents/Python/app-10-scraping-sql/homework/homework_data.txt", "a") as file:
#         file.write(f"{time},{value}\n")

def store(extracted):
    now_time = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?,?)", (now_time, extracted))
    connection.commit()



if __name__ == "__main__":
    timer_count = 10
    while timer_count != 0:
        all_data_from_url = take_data_from_url(URL)
        extracted_data = extracted_data_from_page(all_data_from_url)
        store(extracted_data)
        print(extracted_data)
        timer_count = timer_count - 1

