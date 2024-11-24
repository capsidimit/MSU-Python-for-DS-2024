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
    assert couldMakeNewGeneration("""\
0042 cat male Pushok 13.09.2015 31.12.2016
0003 elephant male Archi 03.03.2011 31.12.2016\
""") == []
    
    assert couldMakeNewGeneration("""\
7910 leopard male Leo 04.06.2001 05.15.2010
9315 orangutan male Hiha 01.04.2004 03.24.2012
2226 leopard female Lia 07.28.2007 08.24.2019\
""") == ["leopard"]
    
    assert couldMakeNewGeneration("""\
7910 leopard male Leo 04.06.2001 05.15.2010
9315 orangutan male Hiha 01.04.2004 03.24.2012
2226 leopard female Lia 07.28.2007 08.24.2019
0042 cat male Pushok 13.09.2015 31.12.2016
0043 dog female Dora 29.01.2015 31.12.2016
0003 cat female Eva 03.03.2017 31.12.2016\
""") == ["cat", "leopard"]


def couldMakeNewGeneration(text: str)-> list[str]:
    animals:dict[str,set[str]] = dict()
    for line in text.splitlines():
        _, animal, gender, *__ = line.split(" ")
        if animal not in animals:
            animals[animal] = set([gender])
        else:
            animals[animal].add(gender)

    pair_animals = [animal for animal, genders in animals.items() if len(genders) > 1]
    
    return sorted(pair_animals, key=lambda animal: len(animal), reverse=False)


def main() -> None:
    with open("input.txt", mode="r") as fileIn:
        animals = couldMakeNewGeneration(fileIn.read())
        print(0 if len(animals) == 0 else "\n".join(animals))


if __name__ == "__main__":
    main()
