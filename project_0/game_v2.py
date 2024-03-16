"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    number = np.random.randint(1, 101)
    begin = 0  # Начало интервала для проверки наличия number
    end = 100  # Конец интервала для проверки наличия number
    while True:
        count += 1
        predict = round((begin + end) / 2) # вычисление числа по параметрам интервала
        if number == predict:
            # print(count, ":", "(", begin, "-", end, ")", number, "-", predict)
            break
        elif number > predict:
            begin = predict
        elif number < predict:
            end = predict
        # print(count, ":", "(", begin, "-", end, ")", number, "-", predict)
    # Ваш код заканчивается здесь

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
