import re
import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   input.txt                           |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

В определенном зоопарке находятся животные, каждому из которых присвоены следующие параметры:
ID, вид, пол, кличка, дата рождения и дата поступления в зоопарк. Исходя из этих данных, вывести все виды животных, которые могут размножаться в данном зоопарке (то есть виды животных, которые представлены в зоопарке как мужским, так и женским полом).
"""
def test_example():
    assert mostCommonAnimal("""\
0042 cat male Pushok 13.09.2015 31.12.2016
0003 elephant male Archi 03.03.2011 31.12.2016\
""") == [("cat",1),("elephant",1)]
    
    assert mostCommonAnimal("""\
7910 leopard male Leo 04.06.2001 05.15.2010
9315 orangutan male Hiha 01.04.2004 03.24.2012
2226 leopard female Lia 07.28.2007 08.24.2019\
""") == [("leopard",2),("orangutan",1)]


def mostCommonAnimal(text: str)-> list[tuple[str,int]]:
    from collections import Counter
    
    animals = Counter(
       line.split(" ")[1] for line in text.splitlines()
    )
    return animals.most_common()


def main() -> None:
    with open("input.txt", mode="r") as fileIn:
        animals = mostCommonAnimal(fileIn.read())
        print(*[f"{animal} - {count}" for animal, count in animals], sep="\n")


if __name__ == "__main__":
    main()
