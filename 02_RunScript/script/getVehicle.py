import requests
from bs4 import BeautifulSoup

def getVehicleData(reg):
    URL = "https://www.carcheck.co.uk/peugeot/"+reg
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    # print(URL)
    page = requests.get(URL, headers=headers)
    # print(page.status_code)

    soup = BeautifulSoup(page.content, "html.parser")
    make = soup.find('th', string='Make').find_next_siblings('td')[0].text
    model = ' '.join(soup.find('th', string='Model').find_next_siblings('td')[0].text.split(' ')[1:])
    year = soup.find('th', string='Year of manufacture').find_next_siblings('td')[0].text

    return make, model, year
    # 

