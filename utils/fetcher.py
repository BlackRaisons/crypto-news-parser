from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from Exception.NetworkError import NetworkError
from Exception.siteAccessError import HttpResponseError

def get_soup(link):
    try:
        print('извлекаю html')
        reqObj = Request(link, headers={'User-Agent':  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.118 Safari/537.36",})
        with urlopen(reqObj) as response:
            soup = BeautifulSoup(response.read(), 'lxml')
            print('Возвращаю обьект супа')
            return soup
    except HTTPError as err:
        raise HttpResponseError(err.url, err.code, err.msg)
    except URLError as err:
        raise NetworkError(err.reason)
