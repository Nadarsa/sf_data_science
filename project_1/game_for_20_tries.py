"""Game: guess the number

The computer randomly proposes the hidden number and guesses this itself in less than 20 attempts

"""

import numpy as np


def random_predict() -> int:
    """The computer randomly guesses the hudden number

    Args:
        The computer proposes the hidden number itself

    Returns:
        int: The number of attempts
    
    """
    
    number = np.random.randint(1, 101)  # the computer proposes the number that will guess
    guess = np.random.randint(1, 101)  # the computer randomly chooses the first number to guess
    print(f'The computer proposes the hidden number {number} and the first try is {guess}')
    count = 0  # the number of attempts
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
                print(f'The computer chose {guess} to guess')
            elif number < mean_value:
                right = mean_value - 1
                guess = np.random.randint(left, right+1)
                print(f'The computer chose {guess} to guess')
            else:
                guess = mean_value
                print(f'The computer chose {guess} to guess')
    return count


random_predict()


def score_game(accepted_function) -> int:
    """How many attempts, on average, per 1000 approaches, our algorithm guesses the hidden number

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: average number of attempts
    
    """

    count_list = []  # list to save the number of attempts
    np.random.seed(1)  # fixing the led for reproducibility

    for number in range(1000):
        count_list.append(accepted_function())

    score = int(np.mean(count_list))  # find the average number of attempts
    print(f'Your algorithm guesses the hidden number on average for: {score} attempts')
    return(score)


score_game(random_predict)