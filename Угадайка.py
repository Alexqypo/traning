import random

secret_num = random.randrange(1, 101)   # создаем случайное число в диапазоне от 1 до 100 включительно
print('Добро пожаловать в числовую угадайку')

def is_valid(num):              # функция проверки числа
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

num_player = input('Введите число от 1 до 100:')         

while not is_valid(num_player):
    num_player = input('А может быть все-таки введем целое число от 1 до 100?')

