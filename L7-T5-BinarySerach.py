import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

# Описание
В данной задаче требуется найти корни функции f(x)=sin(tan(1+x/1000)) методом деления пополам с точностью до 6-го знака после запятой.

Поскольку у этой функции бесконечное количество корней, то на входе заданы промежутки [a,b], для которых гарантируется наличие только одного корня на промежутке,а также знакопеременность функции на границах промежутка, то есть f(a)∗f(b)<0.

# Формат вывода
В первой строке дано целое число N N — количество промежутков для поиска корней. В последующих N N строках по два вещественных числа, разделённых пробелом — границы промежутков.

# Формат вывода
N строк со значениями корней функции f ( x ) f(x), найденных с точностью до 6 знака после запятой. При выводе чисел все знаки после 6-го должны быть отброшены, например, при помощи f-строки: f"{root:.6F}", где root — найденный корень.
"""
def test_example():
    assert f'{search(480,500):.6f}' == '491.386197'
    assert f'{search(460,480):.6f}' == '465.088530'
    assert f'{search(500,510):.6f}' == '507.220145'

def foo(x) -> float:
    from math import sin, tan
    return sin(tan(1 + x/1000))

def search(start: float, stop: float, tolerance=1e-6) -> float:
    from math import fabs
    while (fabs(start - stop) > 2*tolerance):
        middle = (stop + start) / 2
        if foo(middle)* foo(start) < 0.0:
            stop = middle
        else:
            start = middle
    
    return (stop + start) / 2
        

def main() -> None:
    num = int(input())
    for idx in range(num):
        start, stop = map(
            float,
            input().split(" ")
        )
        print(
            f'{search(start, stop):.6f}'
        )

if __name__ == "__main__":
    main()