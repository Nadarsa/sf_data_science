"""Игра угадай число
Компьютер сам загадывает и сам угадывает число меньше чем за 20 попыток
"""

import numpy as np


def random_predict() -> int:
    """Рандомно угадываем число

    Args:
        Компьютер сам загадывает число

    Returns:
        int: Число попыток
    """
    number = np.random.randint(1, 101) # загадываем число, которое будем угадывать
    guess = np.random.randint(1, 101) # выбираем первое число для угадывания
    print(f'The computer guessed the number {number} and the first try is {guess}')
    
    count = 0 # число попыток
    left = 1
    right = 100
    
    
    while True:
        count += 1
        mean_value = (left + right) // 2
        if guess == number:
            print(f'Congratulations! The hidden number is {guess} and the computer guessed it for {count} tries')
            break
        else:
            if number > mean_value:
                left = mean_value + 1
                guess = np.random.randint(left, right+1)
                print(f'The computer chose {guess}')
            if number < mean_value:
                right = mean_value - 1
                guess = np.random.randint(left, right+1)
                print(f'The computer chose {guess}')
            if number == mean_value:
                guess = mean_value
                print(f'The computer chose {guess}')
    return count
 
random_predict()            
    



