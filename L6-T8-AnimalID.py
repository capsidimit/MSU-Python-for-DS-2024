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
ID, вид, пол, кличка, дата рождения и дата поступления в зоопарк. Исходя из этих данных, вывести ID всех животных для каждого вида.
"""
def test_example():
    assert animalIDs("""\
0042 lion male Pushok 13.09.2015 31.12.2016
0043 dog female Dora 29.01.2015 31.12.2016
0003 dog male Max 03.03.2011 31.12.2016
0003 dog male Max 03.03.2011 31.12.2016\
""") == [("dog", ["0003", "0003", "0043"]),("lion", ["0042"])]


def animalIDs(text: str)-> list[tuple[str, list[str]]]:
    animals:dict[str,list[str]] = dict()
    for line in text.splitlines():
        id, animal, *__ = line.split(" ")
        if animal not in animals:
            animals[animal] = [id]
        else:
            animals[animal].append(id)
    sortedIds = list(map(lambda animal: (animal[0], sorted(animal[1])), animals.items()))
    return sorted(sortedIds, key=lambda animal: len(animal[0]), reverse=False)


def main() -> None:
    with open("input.txt", mode="r") as fileIn:
        animals = animalIDs(fileIn.read())
        print(
            *[f"{animal}: {", ".join(ids)}" for animal, ids in animals], 
            sep="\n"
        )


if __name__ == "__main__":
    main()
