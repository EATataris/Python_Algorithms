"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
import hashlib


def memorize(func):
    cache_dict = {}

    def wrapper(arg):
        if arg not in cache_dict:
            cache_dict[arg] = func(arg)
        else:
            print('using cached value')
        print(cache_dict.items())
        return cache_dict[arg]
    return wrapper


@memorize
def web_page(url):
    salt = 'Super powerful salt ever'
    return hashlib.sha256(salt.encode() + url.encode()).hexdigest()


web_page('https://www.youtube.com')
web_page('https://www.youtube.com')
web_page('https://geekbrains.ru')
