# Does not work. Curseforge does not allow web-scraping

import requests
import json
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import progress.bar

import pprint


mod_url = 'https://www.curseforge.com/minecraft/mc-mods/gravestone-mod'
ext_url = '/files'

search_url = mod_url + ext_url


def makeSoup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req, timeout=20).read()

    soup = bs(webpage, 'html.parser')

    return soup


if __name__ == '__main__':
    soup = makeSoup(url='https://www.curseforge.com/minecraft/mc-mods/gravestone-mod')

    print(soup)



    
