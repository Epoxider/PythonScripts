import bs4
import sys
import requests
import urllib.request
from fake_useragent import UserAgent

ua = UserAgent()

def get_soup(url):
    r = requests.get(url, headers={'User-Agent': ua.chrome}) #ua.chrome
    return bs4.BeautifulSoup(r.text, 'lxml')

def Get_SR(player):
    print(player+'s rating')
    url = 'https://www.overbuff.com/players/pc/'+player
    soup = get_soup(url)

    damage = soup.find("tbody", {"class" : "stripe-rows"})
    for row in damage:
        row_text = [x.text for x in row.find_all('td')]
        print(' '.join(row_text))

deeko = 'Deeko-11692'
Get_SR(deeko)

epoxide = 'Epoxide-11387'
Get_SR(epoxide)

