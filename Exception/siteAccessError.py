class HttpResponseError(Exception):
    def __init__(self, url, statusCode, msg):
        self.url = url
        self.statusCode = statusCode
        self.msg = msg
    

    def __str__(self):
        if self.statusCode == 404:
                return f'Страница {self.url} не найдена'
        return f'Проблемы с доступом к сайту ({self.statusCode}): {self.msg} | {self.url}'
        