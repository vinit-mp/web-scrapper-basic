import requests
from bs4 import BeautifulSoup






def scrape():
    url = "https://www.example.com"
    response = requests.get(url)
    soupe_instance = BeautifulSoup(response.text, 'html.parser',)
    print("{}".format(soupe_instance))
    search =   soupe_instance.find("<h1>Example Domain</h1>")
    print("search content: {}".format(search))



if __name__ == "__main__":
    scrape()
