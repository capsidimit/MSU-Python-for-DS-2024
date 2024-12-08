import pytest
import numpy as np
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

# Описание
Используя присваивания в срез массива NumPy, решите задачу FizzBuzz.

В задаче FizzBuzz необходимо вывести числа от 1 до N включительно, однако:
    1. если число делится на 3, но не делится на 5, вместо числа должно быть выведено слово "Fizz";
    2. если число делится на 5, но не делится на 3, вместо числа должно быть выведено слово "Buzz";
    3. если число делится и на 3, и на 5, вместо числа должно быть выведено слово "FizzBuzz".

Использование циклов запрещено.
Вместо этого используйте операции присваивания одного значения в срез.

# Формат ввода
Натуральное число N.

# Формат вывода
Содержание массива в одной строке.
Слова и числа следуют через пробел, без запятых, кавычек и скобок.
"""
def test_example():
    assert " ".join(fizzBuzz(16)) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16"
    assert " ".join(fizzBuzz(15)) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    assert " ".join(fizzBuzz(14)) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14"
    assert " ".join(fizzBuzz(11)) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11"
    assert " ".join(fizzBuzz(10)) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz"
    assert " ".join(fizzBuzz(9)) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz"
    assert " ".join(fizzBuzz(6)) == "1 2 Fizz 4 Buzz Fizz"
    assert " ".join(fizzBuzz(5)) == "1 2 Fizz 4 Buzz"
    assert " ".join(fizzBuzz(4)) == "1 2 Fizz 4"
    assert " ".join(fizzBuzz(2)) == "1 2"
    assert " ".join(fizzBuzz(1)) == "1"
    assert " ".join(fizzBuzz(0)) == ""
    with pytest.raises(ValueError):
        fizzBuzz(-5)

def fizzBuzz(num: int) -> np.ndarray:
    if num < 0:
        raise ValueError
    arr = np.arange(1, num + 1).astype(str)
    if len(arr) > 2:
        arr[2::3] = "Fizz"
        
    if len(arr) > 4:
        arr[4::5] = "Buzz"
        
    if len(arr) > 14:
        arr[14::15] = "FizzBuzz"
        
    return arr

def main() -> None:
    n = int(input())
    res = fizzBuzz(n)
    print(*res)


if __name__ == "__main__":
    main()
