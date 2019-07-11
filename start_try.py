#lambda f
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

#map & filter
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
#перемещено в Sololearn scripts
#Найти слово в строке полезная функция split()
def searhc_jeez(text,symb):

    text=text.split()
    clear=list(filter(lambda x: x[0]==symb or x[0]==symb.upper(),text))

    print(clear)

text='Advertisers study how people learn so that they can ‘teach’ them to respond to their advertising. They want us to be interested, to try something, and then to do it again. These are the elements of learning: interest, experience and repetition. If an advert can achieve this, it is successful. If an advert works well, the same technique can be used to advertise different things. So, for example, in winter if the weather is cold and you see a family having a warming cup of tea and feeling cosy, you may be interested and note the name of the tea … Here the same technique is being used as with the cool, refreshing drink.'
searhc_jeez(text,'a')

import array
import random
import numpy as np
from collections import deque
import sys
import math
'''
#Поиск суммы между min и max
nums=[]
for i in range(random.randrange(10,25)):
    nums.append(random.randrange(-250,250))
print(nums)
print(min(nums),max(nums))
a=nums.index(min(nums))
b=nums.index(max(nums))
print(a,b)
c=int()
sum=0
if a>b:
    c=a
    a=b
    b=c
for i in range(a+1,b):#строго между!!
    sum=sum+nums[i]
print(sum)

#модуль array
a=array.array('i',[1,2,7,4,5])
list(a)
print(a[2:3])
slice_list=a[2:]
print(slice_list)
'''
#сумма элементов в матрице
'''
sum=0
A=  [[1,2,3]
    ,[4,5,6]
    ,[7,8,9]]
for row in A:
    for element in row:
        sum+=element
jeez=[]
for row in range(len(A)):
    jeez=jeez+A[row]
sum=0
print(jeez)
print(min(jeez))
print(max(jeez))
a=jeez.index(min(jeez))
b=jeez.index(max(jeez))
print(a,b)
if a>b:
    c=a
    a=b
    b=c
##по горизонтали
for i in range(a+1,b):
    sum+=jeez[i]
print(sum)
'''
'''#сумма по диагоналям
sum=0
for i in range(len(A[0])):
    sum+=A[i][i]
'''
N = 5
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random.random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

sumMain = 0
sumSecondary = 0
for i in range(N):
    sumMain += matrix[i][i]
    sumSecondary += matrix[i][N-i-1]

print(sumMain)
print(sumSecondary)
# вывод наибольшего элемента из класса по кол-ву продаж
'''
class Product(object):

    def input(self):
        self.name=input('Название: ')
        self.fname=input('Страна: ')
        self.max = int(input('Кол-во продаж: '))
    def out(self):
        print(self.name,' ',self.fname,' ',self.max)
    def mx(self):
        return self.max


mall=[]
mx=0
pos=0
for i in range(2):
    mall.append(Product())
    mall[i]=Product()
    mall[i].input()
    mall[i].out()
    if mall[i].mx()>mx:
        mx=mall[i].mx()
        pos=i
print('Продукт с наибольшим кол-вом продаж: ',mall[pos].mx())



abc=['a','b','c']
zzz=['a','d','k']
print(zzz[0] in abc)
'''
for i in range(4,-1,-1):
    print(i)
import random
##############1-й чебзик###############
#Обработка списка в виде ф-ции
def listing():
    N=int(input('Размер матрицы: '))
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(random.random() * 10))
        matrix.append(row)

    for row in matrix:
        print(row)

    sumMain = 0
    sumSecondary = 0
    sum_row=0
    for i in range(N):
        sumMain += matrix[i][i]
        sumSecondary += matrix[i][N - i - 1]

    for row in matrix:
        if (sum(row)/N)<N:
            sum_row+=1

    print('Сумма элементов главной диагонали: ', sumMain)
    print('Сумма элементов побочной диагонали: ', sumSecondary)
    print('Сумма диагональных элементов: ', sumMain + sumSecondary)
    print('Строки в которых avg меньше N: ',sum_row)


def listing_one():
    j=0
    mass=[]
    abs_sum=0
    n=int(input('Введите размер массива' ))
    for i in range(n):
        mass.append(int(random.random() * 10))

    for i in range(n):
        if mass[i]==0:
            j=i

    for i in range(j,n):
        abs_sum+=abs(mass[i])
    print(mass)
    print(abs(max(mass)))
    if j!=0:
        print('Сумма модулей после 0', abs_sum)

listing()
listing_one()

#########2-й чебзик#######
import random

def listing3():
    sum_row_zero=0
    elem_sum=0
    N=int(input('Размер матрицы: '))
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(random.random() * 10))
        matrix.append(row)

    for row in matrix:
        print(row)
        if 0 not in row:
            sum_row_zero+=1

    for i in range(N):
        for j in range(N):
            if matrix[i][j]>0 & matrix[i][j]%2==0:
                elem_sum=elem_sum+matrix[i][j]

    print('Кол-во столбцов без нулей: ',sum_row_zero)
    print('Сумма четных положительных элементов: ',elem_sum)

listing3()

class Production():
    def input(self):
        self.name = input('Название: ')
        self.syph = input('Шифр: ')
        self.v = int(input('Объем поставок '))
        self.z= int(input('Оптовая цена '))
        self.o=self.v*self.z

    def out(self):
        print(self.name, ' ', self.syph, ' ', self.v,' ', self.z,' ', self.o)

    def mx(self):
        return self.o

def production_pop():
    n=int(input('Кол-во продуктов для ввода: '))
    mall = []
    mx = 0
    pos = 0
    for i in range(n):
        mall.append(Production())
        mall[i] = Production()
        mall[i].input()
        mall[i].out()
        if mall[i].mx() > mx:
            mx = mall[i].mx()
            pos = i
    print('Продукт с наибольшим объемом продаж: ')
    print(mall[pos].out())
    try:
        production_pop()
    except:
        print('что-то пошло не так')    
import random
def listing4():
    sumupMain=0
    sumundMain=0
    sum_row_zero = 0
    elem_sum = 0
    N = int(input('Размер матрицы: '))
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(random.random() * 10))
        matrix.append(row)

    for row in matrix:
        print(row)
    for row in range(N):
        for col in range(row+1,N):
            if matrix[row][col]%2==0 & matrix[row][col]>0:
                sumupMain += 1

    for row in range(1,N):
        for col in range(0,row):
            sumundMain+=abs(matrix[row][col])
            print(matrix[row][col])

    print('кол-во над главной диагональю : ',sumupMain)
    print('Сумма под главной ддиагональю : ',sumundMain)

listing4()
sys.exit()