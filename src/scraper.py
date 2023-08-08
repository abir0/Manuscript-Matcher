import json
import pandas as pd
from urllib.parse import unquote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def read_page_no():
    with open("page_no.json", "r") as file:
        data = json.load(file)
    return data["start"], data["end"]


def write_page_no(start, end):
    with open("page_no.json", "w") as file:
        json.dump({"start": start, "end": end}, file)


def get_params():
    with open("params.json", "r") as file:
        data = json.load(file)
    return data


def get_card_data(card):
    contents = {}
    try:
        contents["Journal Name"] = card.text.split('\n')[0].strip()
        contents["Title"] = card.text.split('\n')[1].strip()
        contents["Keywords"] = card.text.split('\n')[4].strip()
    except:
        return None
    return contents


def main():
    URL = "https://doaj.org/search/articles"

    data_obj = get_params()
    start, end = read_page_no()
    data_obj["from"] = start * int(data_obj["size"])

    URL += "?source=" + unquote(json.dumps(data_obj))

    # Initialize the driver
    driver = webdriver.Chrome()

    data = []

    delay = 10  # seconds

    while start < end:
        driver.get(URL)

        # Get the cards from the search results
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results__record")))
            cards = driver.find_elements(
                By.CLASS_NAME, "search-results__record")
        except TimeoutException as e:
            print(e)
        
        # Iterate over the card elements
        for card in cards:
            data.append(get_card_data(card))

        break # TODO: Remove this break
        
        # Update the page number
        start += 1
        write_page_no(start, end)
        
    # Save the data to a file
    df = pd.DataFrame(data)
    df.to_csv("../data/doaj_articles_data.csv", index=False)

    # Close the driver
    driver.quit()


if __name__ == "__main__":
    main()
