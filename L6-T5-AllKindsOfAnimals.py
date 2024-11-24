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
ID, вид, пол, кличка, дата рождения и дата поступления в зоопарк. Исходя из этих данных, вывести все виды животных, которые есть в данном зоопарке.
"""
def test_example():
    assert allKindsOfAnimals("""\
0042 cat male Pushok 13.09.2015 31.12.2016
0003 elephant male Archi 03.03.2011 31.12.2016\
""") == ["cat", "elephant"]
    
    assert allKindsOfAnimals("""\
7910 leopard male Leo 04.06.2001 05.15.2010
9315 orangutan male Hiha 01.04.2004 03.24.2012
2226 leopard female Lia 07.28.2007 08.24.2019\
""") == ["leopard", "orangutan"]


def allKindsOfAnimals(text: str)-> list[str]:
    animals = set()
    for line in text.splitlines():
        _, animal, *__ = line.split(" ")
        animals.add(animal)
    
    return sorted(animals, key=lambda animal: len(animal), reverse=False)


def main() -> None:
    with open("input.txt", mode="r") as fileIn:
        print(*allKindsOfAnimals(fileIn.read()), sep="\n")


if __name__ == "__main__":
    main()
