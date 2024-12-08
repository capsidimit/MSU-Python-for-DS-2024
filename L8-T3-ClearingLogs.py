import pytest
"""
*-----------------------*-----------------*
|   Ограничение времени |   1 секунда     |
|   Ограничение памяти  |   64Mb          |
|   Ввод                |   input.csv     |
|   Вывод               |   output.csv    |
*-----------------------*-----------------*

# Описание
Программист Иван очень общительный человек, поэтому в рабочее время он любит общаться с друзьями в социальных сетях. Недавно программист Иван узнал, что его начальники логируют время, проведенное сотрудниками в социальных сетях, и в тот же момент понял, что его карьера висит на волоске. Он выяснил у своего друга и коллеги, как можно получить доступ к лог-файлам и в каком формате логируются данные. Оказалось, что данные логируются в виде двумерного массива размерностью 30 x 12, где каждый элемент массива содержит информацию о том, сколько времени сотрудник провел в социальных сетях в i-й рабочий день j-го месяца, в часах. Ради удобства начальство Ивана считает, что каждый месяц состоит ровно из 30 рабочих дней.

Программист Иван знает, что начальство поймет, что что-то не так, если Иван просто обнулит все свои логи. Иван внимательно с ними ознакомился и узнал, что наибольшее время в социальных сетях он проводил по четным числам нечетных месяцев, и по нечетным числам в четные месяцы. Помогите Ивану занизить логи, уменьшив ровно в 2 раза элементы массива, имеющие один четный и один нечетный индекс.

Вам дан csv-файл с логами, его нужно считать и при помощи операций с массивами (мы рекомендуем Вам использовать присваивание в срез) изменить его так, как сказано в условии задачи. А затем сохранить результат в новый csv-файл.

# Формат ввода
В файле input.csv содержится массив размерностью 30 строк на 12 столбцов с информацией о проведенных часах в социальных сетях.

# Формат вывода
В стандартный поток вывода или в файл output.txt выведите 3 вещественных числа (медиану, среднее арифметическое и среднеквадратическое отклонение) с точностью ровно 2 знака после запятой, разделив их одним пробелом.

# Примечания
1. Использование numpy является обязательным.
2. Данные в файле input.csv представлены в стандартном виде .csv:
    * строки, разделённые '\n',
    * разделитель в каждой строке - запятая без пробелов,
    * в качестве разделителя десятичной и дробной части вещественного числа используется точка.
3. Для вывода количества часов, проведенных в социальных сетях, воспользуйтесь форматированием: "%g".
4. Для вывода результата можно использовать numpy.savetxt().
"""

def test_example():
    ...


def main() -> None:
    import numpy as np
    data = np.loadtxt("input.csv", dtype=float, delimiter=",")
    data[1::2, ::2] /= 2
    data[::2, 1::2] /= 2
    np.savetxt("output.csv", data, "%g", ",")

  
if __name__ == "__main__":
    main()