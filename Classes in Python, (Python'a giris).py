# Object Oriented Programming (OOP) , Classes , Python'a giris

# Creating a class , attributes and methods

# class worker:
#     pass

# Below is not recommended for defining class objects

# worker1 = worker()

# worker1.name = 'Adam'
# worker1.surname = 'Sandler'
# worker1.age = 30
# print(worker1.name)
# print(worker1.surname)

# worker2 = worker()
# worker2.gmail = '@John.com'
# print(worker2.gmail)



# It is done like :
class worker:
    def __init__(self,name='not entered',surname='not entered',age=0):
        print('__init__  function is working')
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):
        print(f'name:{self.name}, surname:{self.surname}, age:{self.age}')


# worker1 = worker(age=20)
# print(worker1.name, worker1.surname, worker1.age)

# worker1.show_info()

# worker2 = worker('Jack', 'Hawk', 25)
# print(worker2.name, worker2.surname, worker2.age)

# worker2.show_info()

# worker.show_info(self=worker1)

# self is given as an input by default
# self is important
# above code shows the principle, try to understand
# yesmar yesmar yesmar yesmaar

# worker2 = worker(surname='Yesmar')
# worker2.show_info()






# Class variables and Instance variables

# Instance is a Class member.

class worker:
    raise_percentage = 1.1
    staff_count = 0
    def __init__(self,name,wage):
        self.name = name
        self.wage = wage
        worker.staff_count += 1

# if staff_count was used like self.staff_count,
# program would have understand that staff_count
# is related to (inside of) instances.

# print(worker.staff_count)
# worker1 = worker('John', 1000)
# worker2 = worker('Adam', 1200)
# print(worker.staff_count)

# print(worker1.name)
# print(worker2.wage)

# print(worker1.__dict__)
# print(worker2.__dict__)
# print(worker.__dict__)

# print(worker.raise_percentage)
# print(worker1.raise_percentage)
# print(worker2.raise_percentage)

# print(worker.__dict__)
# print(worker1.__dict__)

# worker.raise_percentage = 1.2       # value change will be applied to all instances
# # print(worker.raise_percentage)
# # print(worker1.raise_percentage)
# # print(worker2.raise_percentage)

# worker1.raise_percentage = 1.21     # value change will be applied only to worker1
# print(worker.raise_percentage)
# print(worker1.raise_percentage)
# print(worker2.raise_percentage)

# print(worker1.__dict__)
# print(worker2.__dict__)









# Class Methods and Instance Methods
# create a class --> class something:
# init function is mandatory --> def __init__(self,parameter1,parameter2,etc...)
# to call variable inside a class , (name of the class).variable

from datetime import date

class person:
    person_count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        person.person_count += 1
    def info(self):     # Instance Method
        return f'name: {self.name}, age:{self.age}'
    @classmethod
    def how_many_people(cls):       # CLS 63 AMG
        return cls.person_count

    @classmethod
    def create_with_a_string(cls,str_):
        name,age = str_.split('-')
        return cls(name,age)

    @classmethod
    def create_with_birthyear(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)

    @staticmethod
    def calculate_birthyear(person):
        return date.today().year - person.age

    def greet_():
        return 'Hello'

person1 = person('Adam', 25)
person2 = person('John', 26)

# print(person.how_many_people())

person3 = person.create_with_a_string('Kate-25')
# print(person.how_many_people())
'Kate-25'
# print(person3.name)

person4 = person.create_with_birthyear('Jack', 1989)
# print(person4.name, person4.age)

# print(person.calculate_birthyear(person1))

# print(person.greet_())



# print(person.info(self=person1))
# print(person.info(person1))
# print(person1.info())



# LOOK AGAIN , EXPLORE AGAIN , UNDERSTAND AGAIN









# OOP Inheritance

class Worker:
    raise_percentage = 1.1
    def __init__(self,name,surname,wage):
        self.name = name
        self.surname = surname
        self.wage = wage
        self.gmail = name + surname + '@corporation.com'

    def info(self):
        return f'name:{self.name}, surname: {self.surname}, wage: {self.wage}, gmail:{self.gmail}'



worker1 = Worker('Adam', 'Sandler', 2000)
worker2 = Worker('John', 'Doe', 1800)

# print(worker2.gmail)


class dev(Worker):
    raise_percentage = 1.2

    def __init__(self,name,surname,wage,language):
        super().__init__(name,surname,wage)     # Parent Class
        self.language = language
    raise_percentage = 1.2
    def info(self):
        return f'name:{self.name}, surname: {self.surname}, wage: {self.wage}, gmail: {self.gmail}, language: {self.language}'
    def language_(self):
        return f'language: {self.language}'

dev1 = dev('Kate', 'Mccall', 2200, 'Python')
dev2 = dev('Josh', 'Clusky', 2100, 'Java')




class manager(Worker):

    def __init__(self, name, surname, wage, workers = None):
        super().__init__(name,surname,wage)
        if workers == None:
            self.workers = []
        else:
            self.workers = workers

    def add_worker(self,worker):
        if worker not in self.workers:
            self.workers.append(worker)

    def remove_worker(self,worker):
        if worker in self.workers:
            self.workers.remove(worker)

    def show_workers(self):
        for worker in self.workers:
            print(worker.info())

manager1 = manager('Abu', 'Dakar', 6000)

manager1.add_worker(worker1)
manager1.add_worker(dev1)

# manager1.show_workers()
# print('********')
# manager1.remove_worker(worker1)
# manager1.show_workers()


manager2 = manager('Abdelaziz', 'Manchester', 700, [dev1,dev2,worker1])
# manager2.show_workers()


# print(isinstance(dev2, Worker))
# print(isinstance(dev1, Worker))
# print(isinstance(dev1,manager))
# print(isinstance(dev2,manager))

# print(issubclass(Worker,dev))
# print(issubclass(dev,Worker))







# print(dev2.gmail)
# print(worker1.raise_percentage)
# print(dev2.raise_percentage)

# print(dev2.info())
# print(dev1.info())
# print(worker1.info())

# print(dev1.language_())









# __str__   and   __repr__


a = 'Python'
b = 2 / 11

# print(str(b))
# print(repr(b))


import datetime

today = datetime.date.today()
# print(today)
# print(str(today))       # for user ... bRuh
# print(repr(today))      # for developer ... Bruh

c = datetime.date(2024, 3, 13)


class Footballer:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'name:{self.name} surname:{self.surname} age:{self.age}'

    def __repr__(self):
        return f"'Footballer: '{self.name}','{self.surname}','{self.age}'"

footballer1 = Footballer('Harry', 'Baller', 18)

# print(footballer1)
# print(footballer1.__repr__())









# Dunder Methods , Magic Methods are the same

# print(3 + 5)
# print(int.__add__(3,5))

# print('hey' + 'there')
# print(str.__add__('hey','there'))

# print([1,2,3] + [4,5,6])
# print(list.__add__([1,2,3],[4,5,6]))


# class Mylist(list):
#     # pass    # same as list class
#     def __add__(self,other):        # overwriting
#         if not len(self) == len(other):
#             return 'They cannot be added'
#         else:
#             result = Mylist()
#             for i in range(len(self)):
#                 result.append(self[i] + other[i])
#         return result

#     def __sub__(self,other):
#         if not len(self) == len(other):
#             return 'They cannot be substracted'
#         else:
#             result = Mylist()
#             for i in range(len(self)):
#                 result.append(self[i] - other[i])
#         return result

#     def __eq__(self,other):
#         if sum(self) == sum(other):
#             return True
#         return False

#     def __abs__(self):
#         result = Mylist()
#         for i in self:
#             if i >= 0:
#                 result.append(i)
#             else:
#                 result.append(-1 * i)
#         return result




# list1 = Mylist([1,2,12,-10,-2])
# list2 = Mylist([4,5,6,-5,-7])

# print(list1 + list2)
# print(list2 - list1)
# print(list1 == list2)
# print(abs(list2))
# print(abs(list1))





class Footballer:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def __eq__(self,other):         # == operator
        if self.name == other.name and self.surname == other.surname:
            return True
        return False

    def __add__(self,other):        # + operator
        name = self.name[0] + other.name[0]
        surname = self.surname[0] + other.surname[0]
        age = self.age + other.age
        return Footballer(name,surname,age)

    def __lt__(self,other):
        if self.age < other.age:
            return True
        return False

    def __gt__(self,other):
        if self.age > other.age:
            return True
        return False



baller1 = Footballer('adam','sandler',27)
baller2 = Footballer('kate','dodge',31)

# print(baller1 == baller2)

baller3 = baller1 + baller2
# print(baller3)
# print(baller3.name)
# print(baller1<baller2<baller3)
# print(baller3>baller2>baller1)