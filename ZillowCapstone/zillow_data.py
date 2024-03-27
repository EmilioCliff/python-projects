from bs4 import BeautifulSoup
import requests

zillow_url = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.91870667745268%2C%22south%22%3A37.631598487892596%2C%22east%22%3A-122.24587527636719%2C%22west%22%3A-122.62078372363281%7D%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A474857%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A2600%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%2C%22usersSearchTerm%22%3A%22%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"


class ZillowSoup:
    def __init__(self):
        self.response = requests.post(url=zillow_url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"})
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.prices = []
        self.addresses = []
        self.links = []

    def get_required_data(self):
        all_rentals = self.soup.find_all("li", class_="ListItem-c11n-8-84-3__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wtsrtn-0 iCyebE gTOWtl")
        for rental in all_rentals:
            try:
                self.prices.append(
                    rental.find("span", class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr").text)
                self.addresses.append(rental.find("address").text)
                self.links.append(rental.find("a", class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link")["href"])
            except AttributeError:
                continue
