import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

Гиперссылки в HTML документах по задумке Тима Бернерса Ли могут содержать URI - уникальный идентификатор ресурса в Сети, в котором указаны протокол доступа к документу, доменное имя сервера на котором лежит документ, путь к документу (файлу) и его расширение.

Требуется из URI выделить только доменное имя включая все доменные зоны, разделёные точками.
"""
def test_example():
    assert getDomain("ftp://yandex.ru/hooray.php") == "yandex.ru"

# Whe could use regex for this task, but we know input format
# `протокол://название.домена.с.точками/папка/файл.расширение`
def getDomain(url:str)-> str:
    return url.split("/")[2]


def main() -> None:
    url = input()
    print(getDomain(url))


if __name__ == "__main__":
    main()