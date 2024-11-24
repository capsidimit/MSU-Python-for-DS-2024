import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

Провести частотный анализ числа и найти наиболее редко встречающуюся цифру.

При наличии нескольких одинаково редко встречающихся цифр вывести меньшую из них по значению.
"""
def test_example():
    assert mostReareDigit("2021") == "0"
    assert mostReareDigit("2120") == "0"

def test_single_digit():
    assert mostReareDigit("1") == "1"
    assert mostReareDigit("9") == "9"

def test_repeated_digits():
    assert mostReareDigit("1111") == "1"
    assert mostReareDigit("2222") == "2"

def test_all_digits_same_frequency():
    assert mostReareDigit("1234567890") == "0"
    assert mostReareDigit("9876543210") == "0"

def test_mixed_digits():
    assert mostReareDigit("12345678901234567890") == "0"
    assert mostReareDigit("98765432109876543210") == "0"
    assert mostReareDigit("00123234") == "1"

def test_large_input():
    large_input = "1" * 100000 + "2" * 100000 + "3" * 100000
    assert mostReareDigit(large_input) == "1"

def mostReareDigit(number: str)-> str:
    # Processing number
    result = {}
    for digit in number:
        if digit not in result:
            result[digit] = 1
        else:
            result[digit] = result[digit] + 1
    # Sorting by rarity
    result = sorted(result.items(), key=lambda pair: pair[1], reverse=False)
    min_frequency = result[0][1]
    # Filtering to get only rearest digits
    rare_digits = [digit for digit, count in result if count == min_frequency]
    # Sorting digits by it's value
    result = sorted(rare_digits, reverse=False)
    # Returning smallest rearest digit
    return result[0]


def main() -> None:
    text = input()
    print(mostReareDigit(text))


if __name__ == "__main__":
    main()
