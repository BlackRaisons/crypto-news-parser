from utils.fetcher import get_soup
from parsers.cryptoNews import parseCryptoNewsArticles
from parsers.forklog import parseForklogArticles


print('\n\n\nзапуск парсера forklog...\n\n\n')
htmlForklog = get_soup(r'https://forklog.com/')
parseForklogArticles(htmlForklog)


print('\n\n\nзапуск парсера cryptonews...\n\n\n')
htmlCryptoNews = get_soup(r'https://cryptonews.net/ru/')
parseCryptoNewsArticles(htmlCryptoNews)
