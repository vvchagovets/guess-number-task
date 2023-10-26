"""Игра угадай число
Компьютер сам загадывает и сам угадывает число

Два варианта угадывания: случайный подбор (random_predict), делением диапазона пополам
(disect_predict)
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def smart_random_predict(number: int = 1) -> int:
    """Рандомно угадываем число, учитывая больше или меньше догадка 
    по сравнению с загаданным

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    target_range = [1, 101]

    while True:
        count += 1
        predict_number = np.random.randint(target_range[0], target_range[1])  # предполагаемое число
        if predict_number > number:
            target_range[1] = predict_number
        elif predict_number < number:
            target_range[0] = predict_number
        elif predict_number == number:
            break  # выход из цикла если угадали
    return count

def disect_predict(number: int = 1) -> int:
    """Guessing a number by dividing the range in half

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    target_range = [1, 101]
    
    # divides the range into two parts and selects the part with the hidden number
    while True:
        count += 1
        # предполагаемое число
        predict_number = target_range[0] +  (target_range[1] - target_range[0]) // 2 
        if predict_number > number:
            target_range[1] = predict_number
        elif predict_number < number:
            target_range[0] = predict_number
        elif predict_number == number:
            break  # выход из цикла если угадали
    return count

def score_game(prediction_function) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания случайным образом
        disect_predict ([type]): функция угадывания делением диапазона пополам

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(prediction_function(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(disect_predict)
