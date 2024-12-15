import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.csv      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

# Описание
В таблице содержатся длины треугольников - по три натуральных (целых положительных) числа в каждой строке. Выясните, какое количество троек чисел может являться сторонами треугольника, то есть удовлетворяет неравенству треугольника: длина любой стороны треугольника всегда меньше суммы длин двух его других сторон.



# Формат ввода
Данные содержатся в файле input.csv. Столбцы называются "a", "b", "c".

Пример данных:
a,b,c
10,20,50
10,41,50
100,40,60
100,40,61
20,50,20
20,50,31
60,60,60

Здесь в первой, третьей и пятой строках неравенство треугольника нарушено, а в остальных четырёх - соблюдено.

# Формат вывода
Одно целое число - количество треугольников во входных данных.

Для примера выше это число:

4

# Примечания
1. Данные в файле input.csv представлены в стандартном виде .csv:
    * строки, разделённые '\n',
    * разделитель в каждой строке - запятая без пробелов,
    * названия столбцов записываются в первой строке,
    * названия столбцов: "a", "b", "c".
2. Обратите внимание, что неравенство треугольника должно выполняться для всех сторон исходного треугольника.
"""

def test_example():
    ...


def main() -> None:
    import pandas as pd
    data = pd.read_csv("input.csv", delimiter=",")  
    print(data[
        (data.a < (data.b + data.c)) &
        (data.b < (data.a + data.c)) &
        (data.c < (data.a + data.b))
    ].shape[0])


if __name__ == "__main__":
    main()
