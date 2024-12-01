import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

# Описание
Менеджер крупной столичной фирмы Алексей готовит отчет о прибыльности проекта. Для отчета о прибыли фирмы Алексей проанализировал много данных и построил графики дневной прибыли.

По плану, который был составлен до старта проекта, прибыль должна была увеличиваться линейно каждый день. Если за первый день работы проекта прибыль была 5 у.е., за последний — 15 у.е., а всего проект длился 11 дней, то прибыль за второй день составит 6 у.е., за третий — 7 у.е. и так далее.

На деле оказалось, что участники проекта очень не любят понедельники, и их продуктивность по понедельникам (то есть каждый 7-ой день) снижается в 3 раза по сравнению с ожидаемой, а в пятницу — наоборот: участники проекта чувствуют душевный подъем и работают в 2 раза активнее. Из-за этого прибыль по этим дням изменяется пропорционально продуктивности.

Пример: ожидаемая прибыль проекта (план)

-пн: 6 у.е.
-вт: 8 у.е.
-ср: 10 у.е.
-чт: 12 у.е.
-пт: 14 у.е.
-сб: 16 у.е.
-вс: 18 у.е.
-пн: 20 у.е.
-вт: ... и т.д.

Фактическая прибыль проекта (с поправкой на продуктивность):

-пн: 2 у.е.
-вт: 8 у.е.
-ср: 10 у.е.
-чт: 12 у.е.
-пт: 28 у.е.
-сб: 16 у.е.
-вс: 18 у.е.
-пн: 6.666 у.е.
-вт: ... и т.д.

Вам дана информация об ожидаемой по плану прибыли в первый день запуска проекта, об ожидаемой по плану прибыли в последний день запуска проекта и количестве дней работы проекта. Считаем, что понедельник — всегда первый день запуска проекта. При помощи np.linspace и присваиваний в срез, найдите прибыль в каждый день работы проекта с поправкой на фактическую продуктивность участников.

# Формат вывода
В файле input.txt Вам даны три числа: прибыль (по плану) проекта в первый день (в понедельник), прибыль (по плану) проекта в последний день и количество дней.

# Формат вывода
Выведите в файл output.txt массив, содержащий данные по ежедневной фактической прибыли. Прибыль за каждый день представляет собой вещественное число c точностью 2 знака после запятой, каждое число записывается в отдельной строке.
"""
def test_example():
    assert management(10,50,5) == [3.33, 20.00, 30.00, 40.00, 100.00]

def management(start: float, stop: float, step: int):
    import numpy as np
    arr = np.linspace(start, stop, step)
    if len(arr[0::7]) > 0:
        arr[0::7] = arr[0::7] / 3
    if len(arr[4::7]) > 0:
        arr[4::7] = arr[4::7] * 2
    return np.round(arr, 2).tolist()

def main() -> None:
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(__location__,"input.txt"), mode="r") as fileIn:
        start, stop, step = map(float, fileIn.readlines())
    
    arr = management(start, stop, int(step))
    
    with open(os.path.join(__location__,"output.txt"), mode="w") as fileOut:
        print(
            "\n".join(
                list(
                    map(
                        lambda el : f'{el:.2f}',
                        arr
                    )
                )
            ),
            sep="",
            end="",
            file=fileOut
        )

if __name__ == "__main__":
    main()
