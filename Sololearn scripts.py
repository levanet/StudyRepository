# lambda f
'''
print('welcome')

def polynimynal(x,y):
    return x**2 +5*y +4
print(polynimynal(-4,-5))

s=(lambda x,y: x**2 +5*y +4)(-4,-5)
print(s)

triple = lambda x: x*3
add = lambda x,y: triple(x)+y
print(add(1,0))
'''

# map & filter
'''
def add_five(x):
    return x+5

nums = [0,1,2]
for i in range(len(nums)):
    add_five(nums[i])
print(nums)

result1=nums+list(map(add_five,nums))+list(map(lambda x:x+10,nums))

print(result1)

result2= list(filter(lambda x: x%2!=0,result1))
print(result2)
'''
# генераторы-итерируемы тип такой как списки или кортежи, им нельзя присваивать произвольные индексы, поддержка цикла for
# создаются с помощью ф-ции yield-возвращает значение из генератора и определяет его(превращает функцию в генератор)
'''
def countdown():
    i=5
    while i>0:
        yield i
        i-=1
for i in countdown():
    print(i)
#не имеют ограничений по памяти и могут выполнятся бесконечно
#фактически генераторы позволяют объявить функцию которая подобна итератору т.е. может быть использована в цикле
#конечные генераторы могут быть преобразованы в списки, для этого их нужно передать ака аргументы функции list()
def numbers(x):
    for i in range(x):
        if i%2==0:
            yield i
a_list=list(numbers(11))
print(a_list)
'''
'''
#декораторы - предназначены для модификации функций с помощью других функций
#пригодятся тогда когда нужно изменить поведение функции не модифицируя ее
def decor(func):
    def wrap():
        print("===================")
        func()
        print("===================")
    return wrap()
@decor
def print_text():
    print("Hello!")

print_text
'''
# Множества - структуры данных подобные спискам или словарямБ они не могут содержать дубликаты и быть проиндексированы
# Проверка на наличие каких либо элементов происходит быстрее чем в списке
num_set = {1, 2, 3, 4, 5}
word_set = set(["You", "picked", "wrong", "house", "fool!"])
print(3 in num_set)
print("fool!" not in word_set)

print(num_set)
num_set.add(-14)
num_set.remove(3)
num_set.pop()
print(num_set)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)  # объединение
print(first & second)  # пересечение
print(first - second)  # разность
print(second - first)  # разность
print(first ^ second)  # симметрическая разность - возвращает элементы с обоих мн-в, кроме пренадлежащих им обоим

# Советы по использованию структур данных:
# - Словарь: 1) когда требуется установить логическую связь пары ключ:значение 2) когда нужен быстрый поиск по данным используя ключ
# 3) когда данные нужно часто изменять
# - Используйте списки, когда у вас есть база данных, к которой не нужен произвольный доступ.
# Старайтесь создавать списки, когда вам нужна простая, итерируемая и часто модифицируемая коллекция данных.
# - Используйте множества, когда вам нужны уникальные элементы
# - Используйте кортежи, когда ваши данные не будут изменятся.

# Модуль itertools - предоставляет тип функии - бесконечный итератор
from itertools import *

# count - создает бесконечную прогрессию вверх от заданого числа
# cycle - бесконечное число раз перебирает итерируемый объект(например, список или строку)
# repeat - повторяет объект бесконечное или заданное количество раз
# takewhile - возвращает элементы из итерируемого объекта которые удовлетворяют предикативной функции
# chain - объединяет несколько итерируемых объектов в один
# accumulate - возвращает сумму значений внутри итерируемого объекта
# product и permutation - используются когда нужно выполнить задачу со всеми возможными комбинациями некоторых элементов

for i in count(3):
    print(i)
    if i >= 11:
        break

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))


# ООП
# start_try.py
# Попытка вызова атрибута экземпляра, который не был определен вызывает AttributeError.
# Такая же ошибка выдается при вызове несуществующего метода.
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def wolfer(self):
        print("Grrr...")


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")
        super().wolfer()  # метод super предназначен для того, чтобы обращатся к методам суперкласса


fido = Dog("Alfred", "Blue")
print(fido.name)
fido.bark()


# Если наследуемый класс (суперкласс) имеет такие же атрибуты или методы, что и класс-наследник(подкласс)
# то класс наследник переопределяет их

# Магические методы - это медоды с двойными подчеркиваниями, зачастую применяются для переопределения операторов
# подразумевается опеределение операторов для пользовательских классов, которые поддерживают такие операторы как :"+" и "*"
# пример магического метода __add__ для операции +
# Выражение x + y представляется как x.__add__(y)
# Но если метод __add__ не выполнялся, а х и у различных типов, тогда используется y.__radd__(x)
# у всех упоменутых далее магических методов есть аналогичные методы r
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        print("Вы умножили!")
        return Vector2D(self.x * other.x, self.y * other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first * second
print(result.x)
print(result.y)


# __sub__ - необходим для оператора -
# __mul__ - для *
# __truediv__ - для /
# __floordiv__ - для //
# __mod__ - для %
# __pow__ - для **
# __and__ - для &
# __xor__ - для ^
# __or__ - для |

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("Spam")
hello = SpecialString("Hello!")
print(spam / hello)
# самостоятельный разбор join
'''
a="ТЫ"
b="Говно"
print(a,b)
shit=[a,b]
c= "\n".join(shit)
print(c)
'''


# магические методы для сравнения
# __lt__ - для <
# __le__ - для <=
# __eq__ - для ==
# __ne__ - для != если не выполняется то возвращается противоположное __eq__
# __gt__ - для >
# __ge__ - для >=
class Special_String:

    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


spam = Special_String("Spam")
eggs = Special_String("Eggs")
spam > eggs


# __len__ - для len()
# __getitem__ - для индексации
# __setitem__ - для присваивания значения индексированному элементу
# __delitem__ - для удаления индексированных элементов
# __iter__ - для перебора объектов(например в циклах for)
# __contains__ - для in

# Сокрытие данных
# Условно частные методы и атрибуты оформляются с единым подчеркиванием в начале имени.
# Это частные методы, которые не должны взаимодействовать со внешней частью программы.
# Но часто это правило условно, внешняя часть программы может получить доступ к ним.
# Реальная особенность этих методов лишь в том, что from module_name import * не будет импортировать переменные,
# которые начинаются с единого подчеркивания.

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
a = queue.pop()
print(queue)
print(a)


# Строго частные методы и атрибуты оформляются с двойным подчеркиванием в начале имени.
# Таким образом их имена искажаются, и внешняя часть программы не может получить к ним доступ.
# Но это делается не для того, чтобы обеспечить их частность, а чтобы избежать ошибок,
# если где-либо в коде есть подклассы, которые имеют методы или атрибуты с такими же именами.
# Методы с искаженными именами все же могут быть вызваны извне, но по другим именам.
# Метод __privatemethod класса Spam может быть вызван извне по имени _Spam__privatemethod
class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg()
print(s._Spam__egg)


# print(s.__egg)#error 'cause it's hidden method

# Методы классов и статические методы
# Методы объектов, рассмотренные до этого, вызываются экземпляром класса, который затем передается в параметр метода self.
# Методы класса несколько другие: они вызываются классом, который передается параметру cls метода.
# Чаще всего это используется в фабричных методах: создается экземпляр класса, при этом используются иные параметры, чем те,
# которые обычно передаются в конструктор класса.
# Методы класса оформляются с декоратором classmethod
class Rectange:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectange.new_square(5)
print(square.calculate_area())


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed= False
    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

    def what(self):
        print("Your pizza constructored by: ", self.toppings)

    @property #свойство
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        if value:
            password = input("Enter the password: ")
            if password == "Swordfish":
                self._pineapple_allowed=value
            else:
                raise ValueError("Alert! Intruder!")

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

pizza.what()
print(pizza.pineapple_allowed)
pizza.pineapple_allowed=True
print(pizza.pineapple_allowed)

# Свойства в свойствах мы можем настроить доступ к атрибутам экземпляра.
# Чтобы создать свойства, непосредственно перед методом помещается декоратор property:
# при вызове атрибута экземпляра с таким же именем, что и у метода, вместо него будет вызван метод.
# Один из распространенных способов их применения - присвоение атрибуту свойства "только для чтения"

# Свойства также могут быть заданы с помощью функций setter/getter.
# Функция setter устанавливает значение для соответствующего свойства.
# Функция getter возвращает значение.
# Чтобы определить setter, используется декоратор с таким же именем, что и у свойства, с последующим ключевым словом setter, разделенные точкой.
# Точно так же определяются функции getter.

