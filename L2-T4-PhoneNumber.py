import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

Человек вводит на сайте номер телефона, ему позволено для удобства использовать кроме плюса и цифр знаки '-', ')', '(' и пробелы.
Приведите номер телефона к единому формату, удалив эти лишние символы при помощи нескольких замен методом replace().
"""
def test_example():
    assert processNumber("+7 (673) 897-07-07") == "+76738970707"


def processNumber(url:str)-> str:
    return url. \
            replace("-",""). \
            replace(" ",""). \
            replace("(",""). \
            replace(")","")


def main() -> None:
    phone = input()
    print(processNumber(phone))


if __name__ == "__main__":
    main()