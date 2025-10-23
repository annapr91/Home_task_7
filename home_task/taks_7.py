import numpy as np


def guess_nr(number:int=1) -> int:
    count = 0
    low = 1
    hight = 100
    while True:
        count +=1
        res = (low+hight)//2 #50
        if res < number:
            low =res+1
        if res > number:
            hight = res -1
        if res == number:
            break 
        
    return f"Ваш алгоритм угадывает число за:{count} попыток"

#np.random.seed(1)  # фиксируем сид для воспроизводимости
random_number = np.random.randint(1, 101)  
print(guess_nr(random_number))