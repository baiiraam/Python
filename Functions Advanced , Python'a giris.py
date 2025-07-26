# Functions Advanced , Python'a giris

# *ARGS , **KWARGS
import time
t1 = time.time()

def exp(x,y):   # positional arguments all must be present
     return x ** y

# print(exp(3,4))

# print(exp(5,5))


def info(name,surname = 'not entered',age = 'not entered'):     # Keyword argument
    return f'name:{name}, surname:{surname}, age:{age}'

# print(info('Catherine'))


def info2(name = 'not entered',surname = 'not entered',age = 'not entered'):     # Keyword argument
    return f'name:{name}, surname:{surname}, age:{age}'

# print(info2('Kate', age = 32))

# print(info2(surname='Muqqil'))





def sum2(x,y):
    return x + y

def sum3(x,y,z):
    return x + y + z

def idk(*args):     # *args - enter arguments as many as you want , they will be stored inside a tuple
    for arg in args:
        print(arg)

# sum(1,2,3,4,5,'Python',False)


def product(*args):
    pro = 1
    for arg in args:
        pro *= arg
    return pro

# print(product(3,4,5))


def average(*args):
    return round(sum(args) / len(args), 2)

# print(average(5,8,10,12,20,100))


def greet(message,*args):
    # print(message)
    # for arg in args:
    #     print(arg)
    result = ''
    result += message
    result += ' '
    for arg in args:
        result += arg
        result += ' '
    return result

# print(greet('hey','howareyou','tfutfu'))


def func(**kwargs):     # enter as many keyword arguments as you want. They will be stored inside a dictionary.
    print(kwargs)

# func(name='Patrick', surname = 'Star', age = 40)
    

def func2(mandatory,*args,**kwargs):
    print(mandatory)
    print('*******')
    for arg in args:
        print(arg)
    print('*******')
    # for kwarg in kwargs:
        # print(kwarg)
    for k,v in kwargs.items():
        print(k,v)


# func2(12,1,2,3,4,5,6,name='Abraham', age = 29)













# FUNCTIONS INSIDE FUNCTIONS

def outer_func():
    print('outer function is working')
    def inner_func():
        print('inner function is working')
    
    print('outer function have stopped')
    inner_func()

# outer_func()
    
    
def calculations(x):
    def square(a):
        return a ** 2
    def squareroot(a):
        return a ** 0.5
    def factorial(a):
        product = 1
        for i in range(1, a + 1):
            product *= i
        return product
    return f'number:{x}\nsquare:{square(x)}\nsquare root:{round((squareroot(x)) , 3)}\nfactorial:{factorial(x)}'

# print(calculations(6))

def sum_product(*args):
    def sum(a):
        sum = 0
        for i in list(a):
            sum += i
        return sum
    def product(a):
        product = 1
        for i in a:
            product *= i
        return product
    return f'sum:{sum(args)}\nproduct:{product(args)}'


# print(sum_product(1,2,3,4,5,6,7,8,9,10))













# FUNCTIONS -> FUNCTIONS

def func1(x):
    return x*x

a = func1(3)
# print(a)

b = func1
# print(b(5))


def select_an_operator(operation):
    def summ(*args):
        sum = 0
        for arg in args:
            sum += arg
        return sum
    
    def productt(*args):
        product = 1
        for arg in args:
            product *= arg
        return product
    
    def ave(*args):
        return sum(args)/len(args)
    
    if operation == 'sum':
        return summ
    elif operation == 'product':
        return productt
    elif operation == 'average':
        return ave
    
sum_func = select_an_operator('sum')
pro_func = select_an_operator('product')
ave_func = select_an_operator('average')
# print(sum_func(1,2,3,4,5))
# print(pro_func(1,2,3,4,5,6,7))
# print(ave_func(100,200,300))



def select_a_person(person):
    def select_a_team(team):
        return f'{person} is a {team} fan'
    return select_a_team

a = select_a_person('Adam')
b = select_a_person('John')

import time

t2 = time.time()
# print(a('Liverpool'))
# print(b('Osasuna'))


# print(t2 - t1)






# FUNCTIONS INSIDE A FUNCTION AS A PARAMETER


def add(*args):
    return sum(args)
def product(*args):
    i = 1
    for arg in args:
        i *= arg
    return i

def operate(func,*args):
    return func(*args)

# print(operate(product,5,6,7,8))


list_1 = [1,2,3,4,5]
list_2 = [1,3,4,5,8,9,11]
def square(x):
    return x * x
def cube(x):
    return x ** 3

def map_func(func,listt):
    # result = []
    # for i in listt:
    #     result.append(func(i))
    # return result
    result = [func(i) for i in listt]
    return result

# print(map_func(cube,list_2))




# import time
# t1 = time.time()
# '''function'''
# t2 = time.time()
# how much time passed = t2 - t1






# DECORATORS


# def decorator(func):
#     def wrapper():
#         print('functions before operations')
#         func()
#         print('functions after operations')
#     return wrapper

# @decorator
# def func():
#     print('function is working')

# func2 = decorator(func)

# func2()

# decorator(func)()

# func()

# import time

# def calculate_time(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs)
#         finish = time.time()
#         print(f'operation is {finish - start} seconds long.')
#     return wrapper

# @calculate_time
# def square_0(list_):
#     for i in list_:
#         print(i * i)


# square(range(10))         # look at this bud
# @calculate_time
# def cubes_0(list_):
#     for i in list_:
#         print(i ** 3)

# @calculate_time
# def add(a,b):
#     time.sleep(1)
#     print(a + b)

# square_0(range(30000))

# cubes_0(range(30000))

# add(10,20)





import time

def timepassed(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        finish = time.time()
        print(f'operation is {finish - start} seconds long')
        time.sleep(1)
        return result
    return wrapper

@timepassed
def square(list):
    result = []
    # result.append(i*i for i in list)
    for i in list:
        result.append(i * i)
    return result

@timepassed
def cube(list):
    result = []
    # result.append(i ** 3 for i in list)
    for i in list:
        result.append(i ** 3)
    return result

@timepassed
def add(*args):
    time.sleep(1)
    return sum(args)

# square(range(100))

# print(square(range(1000)))

# square(range(1000))

# print(cube(range(10000)))










# Python OOP Property , Setter , Deleter , Decorator

# @property, @setter, @deleter

# RELATED TO OOP


class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        # self.fullname = name + ' ' + surname    # Attribute?
        
    @property       # Method --> Property
    def fullname(self):
        return f'{self.name}.{self.surname}@corp.com'
    @property       # Method --> Property
    def gmail(self):
        return f'{self.name}.{self.surname}@corp.com'
    
    @fullname.setter
    def fullname(self,isim):
        name,surname = isim.split(' ')
        self.name=name
        self.surname=surname
    @fullname.deleter
    def fullname(self):
        print('deleted')
        self.name=None
        self.surname=None

    
    
person1 = Person('adam', 'sandler')
# del person1
person1.name = 'john'

person1.fullname = '''Ustun Kisa'''
# del person1.fullname
# del person1.name 

# print(person1.name)
# print(person1.fullname)
# print(person1.gmail)











# Lambda Functions


# def square(x):
#     return x * x 

# print(square(5))

t1=time.time()

square = lambda x : x * x

cube = lambda x : x ** 3

add = lambda x, y : x + y

general_add = lambda *args : sum(args)

# print((lambda x,y,z : x * y + z)(3,3,3))

# print((lambda *args : sum(args)/len(args))(2,3,4,5))


def show_age(x):
    return x[1]

list_ = [('yesmar',22),('rafat',27),('kate',24),('john',26),('adam',29)]
# list_.sort(key= lambda x : x[1])    # what are you sorting for?

# list_.sort(key=show_age)

list2 = [{'name':'yesmar', 'surname':'rafat', 'age':28} , {'name':'ahmad', 'surname':'abdelaziz', 'age':23} , {'name':'john', 'surname':'doe', 'age':24}]
list2.sort(key= lambda x : x['age'])

# print(list2)

t2=time.time()
# print(t2-t1)












# Map Function



list1 = [1,2,3,4,5,6,7]
def square(x):
    return x * x

list2 = []
for i in list1:
    list2.append(i * i)

list2 = [i * i for i in list1]
# print(list2)

list3 = map(square,list1)
# print(type(list3))
# print(list3)
list3 = list(map(square,list1))
# print(list3)
list3 = set(map(square,list1))
# print(list3)
list3 = tuple(map(square,list1))
# print(list3)




list1 = [11,18,15,17]
list2 = list(map(lambda x : x * x, list1))
# print(list2)


list3 = list(map(lambda x : x ** 3, list1))
# print(list3)


list1 = [1,3,4,7,8]
list2 = [3,5,9,0,1]
list3 = [2,5,10]

def add(x,y,z):
    return x + y + z

result = list(map(add,list1,list2,list3))

result2 = list(map(lambda x,y,z : x + y + z,list1,list2,list3))
# print(result2)




products = [['shoes',120],['pants',180],['t-shirt',100],['coat',200]]

def discount(x):
    product,cost = x[0],x[1]
    cost = cost * 0.9
    return [product,cost]

result = list(map(discount,products))
# print(result)



names = ['aDaM','JoHn','jAcK','hArRy']

names2 = list(map(lambda x : x.capitalize(),names))
# print(names2)












# Filter Function

list1=[1,2,3,5,6,8,11,17,121,109]

def iseven(x):
    if x % 2 == 0:
        return True
    return False

evens = filter(iseven,list1)
# print(evens)
evens = list(filter(iseven,list1))
# print(evens)


evens = list(filter(lambda x : x % 2 == 0,list1))
# print(evens)

def istwodigits(x):
    if x >= 10 and x < 100:
        return True
    return False

twodigits = list(filter(istwodigits,list1))
# print(twodigits)


twodigits = list(filter(lambda x : x >= 10 and x < 100,list1))
# print(twodigits)


words = ['aquaman','astalavista','binoculars','spider-man','genz','end','ana','ata','sus','kazak']
starts_with_a = list(filter(lambda x : x.startswith('a'),words))
# print(starts_with_a)

contains_a = list(filter(lambda x : 'a' in x,words))
# print(contains_a)

is_polindrome = list(filter(lambda x : x == x[::-1],words))
# print(is_polindrome)




list1 = [1,2,(1,2,3),True,'string','example',{1,2,4}]
strings = list(filter(lambda x : type(x) == str,list1))
strings2 = list(filter(lambda x : isinstance(x,str),list1))
# print(strings)
# print(strings2)
# 0 -- False
# 1 -- True



list1 = [{'name':'johny','age':22},{'name':'kate','age':23},{'name':'adam','age':24},{'name':'bob','age':18}]
starts_with_a=list(filter(lambda x : x['name'].startswith('a'),list1))
# print(starts_with_a)
older_than_20 = list(filter(lambda x : x['age'] > 20,list1))
# print(older_than_20)











# Reduce Function

from functools import reduce

list1 = [2,4,6,9]
def add(x,y):
    return x + y

def product(x,y):
    return x * y

result1 = reduce(add,list1)
# print(result1)

result1 = reduce(lambda x,y : x + y,list1)
# print(result1)

result2 = reduce(product,list1)
# print(result2)

result2 = reduce(lambda x,y : x * y,list1)
# print(result2)


from math import gcd    # gcd <--> GCD = greatest common divisor
# LCM - least common multiple
# a * b = LCM(a,b) * GCD(a,b)
def lcd(x,y):
    return int(x * y / gcd(x,y))

lcd_ = reduce(lcd,list1)
# print(lcd_)


def rockpapercissors(x,y):
    set_ = {x,y}
    if x == y:
        return x
    if set_ == {'rock','scissors'}:
        return 'rock'
    if set_ == {'rock','paper'}:
        return 'paper'
    if set_ == {'paper','scissors'}:
        return 'scissors'
    
list_ = ['rock','paper','rock','scissors','paper','scissors','rock']
result = reduce(rockpapercissors,list_)    
# print(result)












# ZIP Function

list1 = [1,2,3,4]
list2 = ['a','b','c','d']

list3 = zip(list1,list2)
# print(list3)

list3 = list(zip(list1,list2))
# print(list3)

# print(list(zip(list2,list1)))
# print(set(zip(list2,list1)))
# print(tuple(zip(list2,list1)))


list1 = list('Python')
list2 = [1,2,3,4]
list3 = ['A','B','C']
list4 = list(zip(list1,list2,list3))
# print(list4)


list1 = set('Python')
list2 = set([1,2,3,4])
list3 = set(['A','B','C'])
list4 = set(zip(list1,list2,list3))
# print(list4)


list1 = tuple('Python')
list2 = tuple([1,2,3,4])
list3 = tuple(['A','B','C'])
list4 = tuple((zip(list1,list2,list3)))
# print(list4)















### Local, enclosing, global, built-in variables

# def func():
    # print(x)

# func()    it will not work, called function before defining variable
# x = 8
# func()    it will work, called function after defining variable


x = 'global x'

def outer():
    x = 'enclosing x'
    print(x)
    def inner():
        x = 'local x'
        print(x)
    inner()

# outer()
# print(x)
    

def func():
    # x = 5   # x is not the same as outer (global) x
    global x
    x = 5

# func()
# print(x)
    

x = 'global x'

def outer():
    x = 'enclosing x'
    print(x)
    def inner():
        # nonlocal x
        x = 5
    inner()
    print(x)

# outer()
    

    

# def func():
    # y = 'local y'
    # x = 'local x'
    # print(y)
    # print(x)

# func()
# print(x)
# print(y). y is inside a function, it is a local variable.



# sum,max,min,len,lambda are built-in variables in Python.
# They already have a default function set by Python.
# Do not use them as variable name. Instead:
# sum_ , sum1 , maxx, max_  is preferred so that you do not
# overwrite default Python built-in variables.














# Iterators
# __iter__()  and  __next__()
# __iter__() returns an iterator


numbers = [1,2,3]

# for number in numbers:
#     print(number)


# print(dir(numbers))     # if you see __iter__ in methods, the object is iterable.


i_numbers = numbers.__iter__()
# print(type(i_numbers))

numbers = [1,2,3]

i_numbers = iter(numbers)
# print(type(i_numbers))
# print(dir(i_numbers))       # __next__ method --> passes to next iterable item. Essential.


# print(i_numbers.__next__())
# print(next(i_numbers))
# print(next(i_numbers))
# print(next(i_numbers))      # will give an error


numbers = [1,2,3]

i_numbers = iter(numbers)
# print(type(i_numbers))
while True:
    try:
        number = next(i_numbers)
        print(number)
    except StopIteration:
        break



class New_Range:
    def __init__(self,start,end):
        self.starttowritewith = start
        self.end = end
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.starttowritewith >= self.end:
            raise StopIteration
        value = self.starttowritewith
        self.starttowritewith += 1
        return value

numbers = New_Range(10,20)
# for i in numbers:
#     print(i)

# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))








# Custom Iterator

# sentence = 'Hey Guys Welcome'
# for i in sentence:
#     print(i)



class Sentence:
    def __init__(self,sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        tobereturned = self.index
        self.index += 1
        return self.words[tobereturned]
    
newsentence = Sentence('Hey Guys Welcome')

for word in newsentence:
    print(word)