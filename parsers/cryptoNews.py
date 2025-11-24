from bs4 import BeautifulSoup
from utils.json_writer import addDatajson


def parseCryptoNewsArticles(html):

    path = input(r'Введите полный путь к JSON-файлу, в который нужно сохранить данные статей с сайта CryptoNews: ').strip()


    dataAtricles = []

    blocknews = html.find('div', class_='content row')
    allArticlesBlock = blocknews.find_all('div', class_='row news-item start-xs')

    for data in allArticlesBlock:
        nameArticle = data.get('data-title')
        if not nameArticle: continue

        if not nameArticle:
            nameArticle = data.find('div', class_='desc col-xs').find('a', class_='title').get_text()

        tagA = data.find('a')
        if not tagA: continue

        urlAtricle = tagA.get('href')
        if not urlAtricle: continue

        urlImgArticle = tagA.find('span', class_='image lazy').get('data-src')
        if not urlAtricle: continue

        dataAtricles.append({'url': urlAtricle, 'text': nameArticle, 'img_url': urlImgArticle})

        print(f"""
            url cтатьи: {urlAtricle}
            text статьи: {nameArticle}
            url изображения: {urlImgArticle}
""")
    
    addDatajson(path, dataAtricles, fallbackpath=r'storage\cryptoNews.json')

