import json
import pandas as pd
from urllib.parse import unquote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def get_params():
    with open("params.json", "r") as file:
        data = json.load(file)
    return data


def update_params():
    params = get_params()
    params["from"] += 200
    with open("params.json", "w") as file:
        json.dump(params, file)


def url_encoder(params):
    url = "https://doaj.org/search/articles"
    url += "?source=" + unquote(json.dumps(params))
    return url


def get_card_data(card):
    contents = {}
    try:
        contents["Journal Name"] = card.text.split('\n')[0].strip()
        contents["Title"] = card.text.split('\n')[1].strip()
        contents["Keywords"] = card.text.split('\n')[4].strip()
        card.find_element(
            By.CLASS_NAME, "doaj-public-search-abstractaction-results").click()
        contents["Abstract"] = card.find_element(
            By.CLASS_NAME, "doaj-public-search-abstracttext-results").text.strip()
    except:
        return None
    return contents


def main():
    # Get the params
    params_obj = get_params()

    # Initialize the driver
    driver = webdriver.Chrome()
    driver.get(url_encoder(params_obj))

    delay = 10  # seconds

    # Cookie consent clicker
    cookie_consent = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.ID, "cookie-consent-hide")))
    cookie_consent.click()

    while params_obj["from"] < (1250 * 200):
        data = []
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
            row = get_card_data(card)
            if row is not None:
                data.append(row)
        
        # Save the data to a file
        df = pd.DataFrame(data)
        if params_obj["from"] == 0:
            df.to_csv("../data/doaj_articles_data.csv", index=False)
        else:
            df.to_csv("../data/doaj_articles_data.csv", mode="a", header=False, index=False)

        # Update the page number
        update_params()
        params_obj = get_params()
        driver.get(url_encoder(params_obj))

    # Close the driver
    driver.quit()


if __name__ == "__main__":
    main()
