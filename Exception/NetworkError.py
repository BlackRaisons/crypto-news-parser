class NetworkError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return f'Сетевая ошибка: {self.error}'
        