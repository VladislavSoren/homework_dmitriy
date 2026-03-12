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
    
    def __init__(self, title, author, pages):
        # TODO: сохранить title, author, pages
        pass
    
    def is_big(self):
        """Возвращает True, если страниц больше 300"""
        # TODO: реализовать метод
        pass
    
    @classmethod
    def set_genre(cls, new_genre):
        """Меняет жанр для всех книг"""
        # TODO: реализовать метод класса
        pass

# Пример использования
book1 = Book("Война и мир", "Толстой", 1300)
book2 = Book("Колобок", "Народ", 10)

print(book1.is_big())  # True
print(book2.is_big())  # False

print(book1.genre)     # Unknown
Book.set_genre("Роман")
print(book1.genre)     # Роман
print(book2.genre)     # Роман


# Задание 2: Класс "Банковский счет"
# Создай класс BankAccount:

# При создании принимает owner и balance (по умолчанию 0)

# Метод deposit(amount) - пополнение

# Метод withdraw(amount) - снятие (нельзя уйти в минус, вернуть False если недостаточно)

# Метод __repr__ для красивого вывода

class BankAccount:
    def __init__(self, owner, balance=0):
        # TODO: сохранить owner и balance
        pass
    
    def deposit(self, amount):
        """Пополнение счета"""
        # TODO: увеличить баланс и вернуть сообщение
        pass
    
    def withdraw(self, amount):
        """Снятие со счета. Вернуть False если недостаточно средств"""
        # TODO: проверить достаточно ли средств и снять
        pass
    
    def __repr__(self):
        """Вернуть строку вида: BankAccount(Иван, 120)"""
        # TODO: реализовать магический метод
        pass

# # Пример использования
acc = BankAccount("Иван", 100)
acc.deposit(50)        # баланс 150
print(acc.withdraw(30)) # True, баланс 120
print(acc.withdraw(200)) # False (недостаточно)
print(acc)              # BankAccount(Иван, 120)
