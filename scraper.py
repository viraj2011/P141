from bs4 import BeautifulSoup
import requests

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

Stars_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        soap = BeautifulSoup(browser.page_source,"html.parser")

        for ul_tag in soup.find_all("ul", attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []

            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("") 


# Define Header
headers = ["name", "distance", "mass", "radius"]


