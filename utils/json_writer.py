import json
import os



def addDatajson(path, data, fallbackpath):
    try:

        if not os.path.exists(path):
            print('не верный путь до файла, файл будет создан в директории программы')
            path = fallbackpath
            olddata = []
        
        elif os.path.getsize(path) == 0:
            olddata = []

        else:
            with open(path, 'r', encoding='utf-8') as f:

                olddata = json.load(f)
                if not isinstance(olddata, list):
                    olddata = []

        
        combinedData = olddata + data
        uniqueData = list({item['url']: item for item in combinedData if 'url' in item}.values())
        

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(uniqueData, f, ensure_ascii=False, indent=4)

    except Exception as err:
        print('ошибка при записи данных в json', err)