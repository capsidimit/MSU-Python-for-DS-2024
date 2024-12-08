import pytest
"""
*-----------------------*-----------------*
|   Ограничение времени |   1 секунда     |
|   Ограничение памяти  |   64Mb          |
|   Ввод                |   input.txt     |
|   Вывод               |   output.txt    |
*-----------------------*-----------------*

# Описание
В тот самый момент, когда стажер-аналитик Павел собирается пойти пообедать, директор по связям с общественностью обращается к нему с вопросом: может ли он предоставить для веб-сайта какие-нибудь примечательные факты об уровне зарплат исследователей данных?
Данные имеют конфиденциальный характер, и поэтому Павла снабдили анонимным набором данных, содержащим зарплату каждого сотрудника в долларах в месяц. Но это не проблема, подумал Павел, так как достаточно будет посчитать некоторые статистические показатели по предоставленным ему данным, а именно: медиану, среднее арифметическое, а также среднеквадратическое отклонение зарплат. Помогите Павлу сделать задание и со спокойной душой пойти на перерыв.

# Формат ввода
В файле input.txt дана последовательность целых чисел в диапазоне от 1000 до 10000 включительно.

Числа разделены одним символом пробел.

Количество чисел меньше 100000.

# Формат вывода
В стандартный поток вывода или в файл output.txt выведите 3 вещественных числа (медиану, среднее арифметическое и среднеквадратическое отклонение) с точностью ровно 2 знака после запятой, разделив их одним пробелом.

# Примечания
1. Использование numpy является обязательным.
2. Для нахождения статистик по данным воспользуйтесь соответствующими функциями из библиотеки numpy:
    * numpy.median(),
    * numpy.mean(),
    * numpy.std().
3. Чтобы вывести вещественное число с двумя знаками после запятой воспользуйтесь форматированием строк:
    * print("{:.2f}".format(3.14159)) -> 3.14. Подробнее - см. рекомендации к вводу-выводу.
4. В задаче не разрешается использовать pandas.
5. Для подсчёта суммы отдельно по столбцам или по строкам можно использовать numpy.sum() с указанием параметра axis (см. официальную документацию).
"""

def test_example():
    ...


def main() -> None:
    import numpy as np
    data = np.loadtxt("input.txt", dtype=float, delimiter=" ")
    with open("output.txt", mode="w") as fileOut:
        print("{:.2f} ".format(np.median(data)), end="", file=fileOut)
        print("{:.2f} ".format(np.mean(data)), end="", file=fileOut)
        print("{:.2f}".format(np.std(data)), end="", file=fileOut)

    
if __name__ == "__main__":
    main()