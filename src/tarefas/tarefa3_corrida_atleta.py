#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Начальная дистанция
    daily_distance = 10.0  # км
    total_distance = 0.0

    print("Расчет дистанции за 7 дней:")
    print("День 1: {:.2f} км".format(daily_distance))

    total_distance += daily_distance

    # Расчет для дней 2-7
    for day in range(2, 8):
        daily_distance = daily_distance * 1.10  # Увеличение на 10%
        total_distance += daily_distance
        print("День {}: {:.2f} км".format(day, daily_distance))

    print("\nСуммарный путь за 7 дней: {:.2f} км".format(total_distance))