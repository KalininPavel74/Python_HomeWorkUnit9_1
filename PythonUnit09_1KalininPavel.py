# Калинин Павел 30.01.2023
# Знакомство с языком Python (семинары) 
# Урок 9. Часть 1. 
# Домашняя работа

#. venv/Scripts/activate

taskName = '''Задание  №1. Создайте любую программу.py 
при помощи виртуального окружения и PIP. 
Отправте репозиторий где будет этот файл и файл requirements.txt.
'''
from isOdd import isOdd

print(taskName)
print()
print('Примеры работы библиотеки isOdd проверяющей числа на четность.')

try:
    print('isOdd("1")=',isOdd("1"))
except Exception as e: print(e)
try:
    print('isOdd("5")=',isOdd("5"))
except Exception as e: print(e)

print('isOdd(0)=',isOdd(0))
print('isOdd(4)=',isOdd(4))

print('isOdd(1)=',isOdd(1))
print('isOdd(-1)=',isOdd(-1))
