import string
import itertools

passwordReal = "6537"  # пароль, который нужно подобрать

# Множество символов, которые будем использовать для подбора (цифры, буквы, знаки пунктуации)
guessPasswordSet = string.digits + string.ascii_letters + string.punctuation
guessPasswordLength = 1  # начальная длина пароля для подбора

# Функция, которая создает все возможные комбинации символов заданной длины
def stringIter(string, length):
    yield from itertools.product(*([string] * length))  # генерация комбинаций символов

# Цикл для перебора паролей
while True:
    # Перебираем все возможные комбинации символов длиной guessPasswordLength
    for passwordSet in stringIter(guessPasswordSet, guessPasswordLength):
        passwordString = ''.join(passwordSet)  # превращаем кортеж символов в строку
        if passwordString == passwordReal:  # если текущий пароль совпал с реальным
            print("Password is found: ", passwordString)  # выводим найденный пароль
            exit()  # завершаем программу
    # Увеличиваем длину пароля, если совпадение не найдено
    guessPasswordLength += 1
