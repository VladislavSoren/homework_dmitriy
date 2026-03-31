"""
#дз
- Повторить пройденный материал
- Решить задачи
- Изучить темы:
-- Наследование
-- Композиция и агрегация
-- Полиморфизм
- Подготовить вопросы
"""

# Задание 3: Наследование (Животные)

# Задание 3: Классы "Animal", "Cat", "Dog"
# Создай базовый класс Animal, который:
# - Принимает name, age при создании
# - Имеет метод make_sound(), возвращающий "Some sound"
# - Имеет метод info(), возвращающий строку вида "Animal: {name}, {age} years"

# Создай класс Cat, наследующий от Animal:
# - Принимает дополнительно breed
# - Переопределяет make_sound() -> "Meow"
# - Переопределяет info() -> "Cat: {name}, {age} years, breed: {breed}"

# Создай класс Dog, наследующий от Animal:
# - Переопределяет make_sound() -> "Woof"
# - Добавляет метод fetch() -> "{name} is fetching the ball!"

class Animal:
    def __init__(self, name, age):
        # TODO: сохранить name и age
        pass

    def make_sound(self):
        # TODO: вернуть "Some sound"
        pass

    def info(self):
        # TODO: вернуть "Animal: {name}, {age} years"
        pass


class Cat(Animal):
    def __init__(self, name, age, breed):
        # TODO: вызвать конструктор родителя и сохранить breed
        pass

    def make_sound(self):
        # TODO: вернуть "Meow"
        pass

    def info(self):
        # TODO: вернуть "Cat: {name}, {age} years, breed: {breed}"
        pass


class Dog(Animal):
    def make_sound(self):
        # TODO: вернуть "Woof"
        pass

    def fetch(self):
        # TODO: вернуть "{name} is fetching the ball!"
        pass


# Пример использования
# cat = Cat("Мурка", 3, "Сиамская")
# print(cat.info())          # Cat: Мурка, 3 years, breed: Сиамская
# print(cat.make_sound())    # Meow

# dog = Dog("Шарик", 5)
# print(dog.info())          # Animal: Шарик, 5 years
# print(dog.make_sound())    # Woof
# print(dog.fetch())         # Шарик is fetching the ball!


# Задание 4: Композиция (Автомобиль и Двигатель)

# Задание 4: Классы "Engine" и "Car" (композиция)
# Создай класс Engine:
# - Принимает horsepower, fuel_type при создании
# - Имеет метод start(), возвращающий "Engine started"
# - Имеет метод stop(), возвращающий "Engine stopped"

# Создай класс Car:
# - Принимает brand, model и объект engine
# - Имеет метод drive(), который запускает двигатель и возвращает "{brand} {model} is driving"
# - Имеет метод park(), который останавливает двигатель и возвращает "{brand} {model} is parked"

class Engine:
    def __init__(self, horsepower, fuel_type):
        # TODO: сохранить horsepower и fuel_type
        pass

    def start(self):
        # TODO: вернуть "Engine started"
        pass

    def stop(self):
        # TODO: вернуть "Engine stopped"
        pass


class Car:
    def __init__(self, brand, model, engine):
        # TODO: сохранить brand, model и engine
        pass

    def drive(self):
        # TODO: запустить двигатель и вернуть строку с маркой и моделью
        pass

    def park(self):
        # TODO: остановить двигатель и вернуть строку с маркой и моделью
        pass


# Пример использования
# engine1 = Engine(150, "бензин")
# car1 = Car("Toyota", "Camry", engine1)
# print(car1.drive())   # Engine started
#                       # Toyota Camry is driving
# print(car1.park())    # Engine stopped
#                       # Toyota Camry is parked

# engine2 = Engine(200, "дизель")
# car2 = Car("BMW", "X5", engine2)
# print(car2.drive())   # Engine started
#                       # BMW X5 is driving


# Задание 5: Агрегация (Библиотека и Книга)

# Задание 5: Классы "Book" и "Library" (агрегация)
# Создай класс Book:
# - Принимает title, author, isbn
# - Имеет метод info(), возвращающий "{title} by {author}"

# Создай класс Library:
# - Принимает name и пустой список книг (по умолчанию)
# - Имеет метод add_book(book) — добавляет книгу в список
# - Имеет метод remove_book(isbn) — удаляет книгу по ISBN, если найдена
# - Имеет метод find_by_author(author) — возвращает список названий книг этого автора
# - Имеет метод list_books() — выводит информацию о каждой книге

class Book:
    def __init__(self, title, author, isbn):
        # TODO: сохранить title, author, isbn
        pass

    def info(self):
        # TODO: вернуть "{title} by {author}"
        pass


class Library:
    def __init__(self, name, books=None):
        # TODO: сохранить name, а books сделать пустым списком, если не передан
        pass

    def add_book(self, book):
        # TODO: добавить книгу в список
        pass

    def remove_book(self, isbn):
        # TODO: найти книгу по isbn и удалить из списка
        pass

    def find_by_author(self, author):
        # TODO: вернуть список названий книг указанного автора
        pass

    def list_books(self):
        # TODO: вывести информацию о каждой книге (можно через print)
        pass


# Пример использования
# book1 = Book("1984", "Оруэлл", "978-0-452-28423-4")
# book2 = Book("Скотный двор", "Оруэлл", "978-0-451-52634-2")
# book3 = Book("Мастер и Маргарита", "Булгаков", "978-5-699-12345-6")

# lib = Library("Главная библиотека")
# lib.add_book(book1)
# lib.add_book(book2)
# lib.add_book(book3)

# print(lib.find_by_author("Оруэлл"))   # ['1984', 'Скотный двор']
# lib.remove_book("978-5-699-12345-6")
# lib.list_books()   # Вывод информации об оставшихся книгах


# Задание 6 (дополнительное): Наследование + композиция (Сотрудники и Отдел)

# Задание 6: Классы "Employee", "Manager", "Department"
# Создай базовый класс Employee:
# - Принимает name, salary
# - Имеет метод work(), возвращающий "{name} is working"
# - Имеет метод get_info(), возвращающий строку с именем и зарплатой

# Создай класс Manager, наследующий от Employee:
# - Принимает дополнительно team_size
# - Переопределяет work(), возвращая "{name} is managing a team of {team_size}"

# Создай класс Department:
# - Принимает name и список сотрудников (по умолчанию пустой)
# - Имеет метод hire(employee) — добавляет сотрудника
# - Имеет метод fire(employee_name) — удаляет сотрудника по имени
# - Имеет метод get_total_salary() — возвращает сумму зарплат всех сотрудников
# - Имеет метод show_employees() — выводит информацию о каждом сотруднике

class Employee:
    def __init__(self, name, salary):
        # TODO: сохранить name и salary
        pass

    def work(self):
        # TODO: вернуть "{name} is working"
        pass

    def get_info(self):
        # TODO: вернуть строку с именем и зарплатой
        pass


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        # TODO: вызвать конструктор родителя и сохранить team_size
        pass

    def work(self):
        # TODO: вернуть "{name} is managing a team of {team_size}"
        pass


class Department:
    def __init__(self, name, employees=None):
        # TODO: сохранить name, employees сделать пустым списком, если не передан
        pass

    def hire(self, employee):
        # TODO: добавить сотрудника в список
        pass

    def fire(self, employee_name):
        # TODO: удалить сотрудника по имени (если есть)
        pass

    def get_total_salary(self):
        # TODO: вернуть сумму зарплат всех сотрудников
        pass

    def show_employees(self):
        # TODO: вывести информацию о каждом сотруднике
        pass


# Пример использования
# emp1 = Employee("Иван", 50000)
# emp2 = Employee("Мария", 60000)
# mgr = Manager("Петр", 80000, 5)

# dept = Department("IT")
# dept.hire(emp1)
# dept.hire(emp2)
# dept.hire(mgr)

# dept.show_employees()
# print(f"Общая зарплата: {dept.get_total_salary()}")  # 190000
# dept.fire("Мария")
# dept.show_employees()   # Марии уже нет

