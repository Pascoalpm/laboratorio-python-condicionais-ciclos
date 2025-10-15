#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввод трех действительных чисел
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число c: "))

    print("Числа, модуль которых не меньше 4:")

    # Проверка каждого числа
    if abs(a) >= 4:
        print(f"a = {a}")

    if abs(b) >= 4:
        print(f"b = {b}")

    if abs(c) >= 4:
        print(f"c = {c}")