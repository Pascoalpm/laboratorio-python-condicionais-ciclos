#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Точность вычислений
EPS = 1e-10


def factorial(n):
    """Вычисление факториала числа n"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def shi_function(x):
    """
    Вычисление интегрального гиперболического синуса Shi(x)
    using series expansion
    """
    if x == 0:
        return 0.0

    sum_series = 0.0  # Сумма ряда
    n = 0
    terms_count = 0

    while True:
        # Вычисление текущего члена ряда
        numerator = x ** (2 * n + 1)
        denominator = (2 * n + 1) * factorial(2 * n + 1)
        current_term = numerator / denominator

        # Добавление к сумме
        sum_series += current_term
        terms_count = n

        # Проверка точности
        if abs(current_term) < EPS:
            break

        n += 1

        # Защита от бесконечного цикла
        if n > 1000:
            break

    return sum_series, terms_count + 1


if __name__ == '__main__':
    print("Вычисление интегрального гиперболического синуса Shi(x)")
    print("Точность: ε = 10^-10")
    print()

    try:
        x = float(input("Введите значение x: "))

        # Вычисление Shi(x)
        result, terms_used = shi_function(x)

        print(f"Shi({x}) = {result:.10f}")
        print(f"Количество членов ряда: {terms_used}")

    except ValueError:
        print("Ошибка: введите действительное число")
    except Exception as e:
        print(f"Произошла ошибка: {e}")