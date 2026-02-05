import time

def fun1():
    time.sleep(3)
    print(123)

"""
Декоратор - функция, которая принимает другую функцию и возвращает функцию wrapper, которая содержит дополнительный функционнал.
"""

def timer1(timeout):
    def wrapper_fun(fun1):
        def wrapper():
            print('Привет') #Добавляем что-то в шкатулку
            start_time = time.time()
            fun1() #Сама функция
            print('Пока') #Добавляем что-то еще
            finish_time = time.time()
            processing_time = finish_time - start_time
            if processing_time > timeout:
                print('Время выполнения превышено')
            print('Прошедшее время', processing_time)
        return wrapper 
    return wrapper_fun
wrapper_fun = timer1(3)
wrapper = wrapper_fun(fun1)

wrapper()


@timer1(timeout=3)
def fun1():
    time.sleep(3)
    print(123)

fun1()


@timer1(timeout=4)
def fun1():
    time.sleep(3)
    print(123)

fun1()

# time.time() #Текущее время
# time.sleep(1) #Подождать секунду