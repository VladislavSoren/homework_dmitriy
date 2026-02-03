import time

def fun1():
    time.sleep(3)
    print(123)

"""
Декоратор - функция, которая принимает другую функцию и возвращает функцию wrapper, которая содержит дополнительный функционнал.
"""
def timer1(fun1): #Сундук
    def wrapper():#Шкатулка
        print('Привет') #Добавляем что-то в шкатулку
        start_time = time.time()
        fun1() #Сама функция
        print('Пока') #Добавляем что-то еще
        finish_time = time.time()
        processing_time = finish_time - start_time
        print('Прошедшее время', processing_time)
    return wrapper #Возвращаем шкатулку

wrapper = timer1(fun1) #Достаем шкатулку

wrapper() # Открываем шкатулку

# time.time() #Текущее время
# time.sleep(1) #Подождать секунду



