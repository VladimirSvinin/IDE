"""Игра угадай число"""

import numpy as np # Импорт необходимой библиотеки
import math #загружаем библиотеку для округления вверх с помощтю функции .ceil()


def random_predict(number: int=1) -> int:
    """загадываем число, которое нужно будет угадать
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток (count)
    """

    # количество попыток
    count = 0
    #создаём минимальные и максимальные значения угадываемого числа
    #которые будут меняться в зависимости от того, угадано число или нет
    low, high = 1, 100

    predict = np.random.randint(1, 101)  # создаём случайное число, которое мы будем сравнивать  с number

    while number != predict: 
        count += 1  # Увеличиваем количество попыток
        if number > predict: 
            low = predict + 1  # Сдвигаем нижнюю границу диапазона
        elif number < predict: 
            high = predict - 1  # Сдвигаем верхнюю границу диапазона вниз
        predict = (low + high) // 2  # Вычисляем среднее значение между low и high для следующего предположения
        
    return count
print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)