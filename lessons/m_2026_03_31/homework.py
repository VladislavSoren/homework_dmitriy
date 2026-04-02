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

# Задание 1: Класс "Книга"
# Создай класс Book, который будет:

# Принимать title, author, pages при создании

# Иметь метод is_big(), который возвращает True, если страниц больше 300

# Иметь атрибут класса genre со значением "Unknown"

# Иметь метод класса set_genre(cls, new_genre), который меняет жанр для всех книг


class Book:
    # Атрибут класса
    genre = "Unknown"
    
    def __init__(self, title, author, pages):  # self - наши book1 и book2, т.е. создаваемые объекты
        # TODO: сохранить title, author, pages в создаваемый объект
        # Атрибуты объекта класса 
        self.title = title
        self.author = author
        self.pages = pages

    def is_big(self):
        """Возвращает True, если страниц больше 300, иначе False"""
        # TODO: реализовать метод
        # if self.pages > 300:
        #     return True
        # else:
        #     return False
        return self.pages > 300

    def set_year(self, year):
        """Меняет жанр для всех книг"""
        # TODO: реализовать метод класса
        self.year = year

    @classmethod
    def set_genre(cls, new_genre):  # cls - ссылка на класс Book
        """Меняет жанр для всех книг"""
        # TODO: реализовать метод класса
        cls.genre = new_genre

# Пример использования
book1 = Book("Война и мир", "Толстой", 1300)  # book1 - ("Война и мир", "Толстой", 1300)
book2 = Book("Колобок", "Народ", 10)

# print(book1.is_big())  # True
# print(book2.is_big())  # False

# print(book1.genre)     # Unknown
# Book.set_genre("Роман")
# print(book1.genre)     # Роман
# print(book2.genre)     # Роман


# Задание 2: Класс "Банковский счет"
# Создай класс BankAccount:

# При создании принимает owner и balance (по умолчанию 0)

# Метод deposit(amount) - пополнение

# Метод withdraw(amount) - снятие (нельзя уйти в минус, вернуть False если недостаточно)

# Метод __repr__ для красивого вывода

class BankAccount:
    def __init__(self, owner, balance=0):
        # TODO: сохранить owner и balance
        self.owner = owner
        self.balance = balance
    
    @staticmethod
    def print_hellow():
        print("hellow")

    def deposit(self, amount):  # amount - 50
        """Пополнение счета"""
        # TODO: увеличить баланс и вернуть сообщение
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        """Снятие со счета. Вернуть False если недостаточно средств"""
        # TODO: проверить достаточно ли средств и снять
        current_balance = self.balance

        current_balance = current_balance - amount
        if current_balance < 0:
            return False
        else:
            self.balance = self.balance - amount
        return self.balance
    
    def __repr__(self):
        """Вернуть строку вида: BankAccount(Иван, 120)"""
        # TODO: реализовать магический метод
        return f"BankAccount({self.owner}, {self.balance})"

# # Пример использования
acc = BankAccount("Иван", 100)
acc.deposit(50)        # баланс 150
print(acc.withdraw(30)) # True, баланс 120
print(acc.withdraw(200)) # False (недостаточно)
print(acc)              # BankAccount(Иван, 120)
