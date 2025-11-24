from bs4 import BeautifulSoup
from utils.json_writer import addDatajson
import re



def parseForklogArticles(html):

    path = input(r'Введите полный путь к JSON-файлу, в который нужно сохранить данные статей с сайта forklog: ').strip()

    dataAtricles = []
    postItems = html.find_all('div', class_='post_item')  

    for i in postItems:
        img_div = i.find('div', class_='image_blk')

        if not img_div: continue
        img_tag = img_div.find('img') 

        if not img_tag: continue
        urlImgArticle = img_tag.get('data-lazy-src') or img_tag.get('src')

        linkList = i.find_all('a', href=re.compile(r'^https://forklog\.com/news/[A-Za-z0-9/\-_]+$'))

        for a in linkList:
            text_blk = a.find('div', class_='text_blk')

            if not text_blk: continue
            p_tag = text_blk.find('p')

            if not p_tag: continue
            nameArticle = p_tag.get_text(strip=True)


            dataAtricles.append({'url': a.get('href'), 'text': nameArticle, 'img_url': urlImgArticle})

            print(f"""
            url cтатьи: {a.get('href')}
            text статьи: {nameArticle}
            url изображения: {urlImgArticle}
""")
    
    addDatajson(path, dataAtricles, fallbackpath=r'storage\forklog.json')




            

    





        

