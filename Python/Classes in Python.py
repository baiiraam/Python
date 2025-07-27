# # Object Oriented Programming (OOP) , Classes , Python'a giris

# # Creating a class , attributes and methods

# # Below is not recommended for defining class objects

# # class worker:
# #     pass

# # worker1 = worker()

# # worker1.name = 'Adam'
# # worker1.surname = 'Sandler'
# # worker1.age = 30
# # print(worker1.name)
# # print(worker1.surname)

# # worker2 = worker()
# # worker2.gmail = '@John.com'
# # print(worker2.gmail)



# # It is done like :
# class worker:
#     def __init__(self,name='not entered',surname='not entered',age=0):
#         print('__init__  function is working')
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def show_info(self):
#         print(f'name:{self.name}, surname:{self.surname}, age:{self.age}')


# worker1 = worker(age=20)
# print(worker1.name, worker1.surname, worker1.age)

# worker1.show_info()

# worker2 = worker('Jack', 'Hawk', 25)
# print(worker2.name, worker2.surname, worker2.age)

# worker2.show_info()

# worker.show_info(self=worker1)

# # self is given as an input by default
# # above code shows the principle, try to understand

# worker2 = worker(surname='Yesmar')
# worker2.show_info()






# # Class variables and Instance variables

# # Instance is a Class member.

# class worker:
#     raise_percentage = 1.1
#     staff_count = 0
#     def __init__(self,name,wage):
#         self.name = name
#         self.wage = wage
#         worker.staff_count += 1

# # if staff_count was used like self.staff_count,
# # program would have understand that staff_count
# # is related to (inside of) instances.

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
# print(worker.raise_percentage)
# print(worker1.raise_percentage)
# print(worker2.raise_percentage)

# worker1.raise_percentage = 1.21     # value change will be applied only to worker1
# print(worker.raise_percentage)
# print(worker1.raise_percentage)
# print(worker2.raise_percentage)

# print(worker1.__dict__)
# print(worker2.__dict__)









# # Class Methods and Instance Methods
# # create a class --> class something:
# # init function is mandatory --> def __init__(self,parameter1,parameter2,etc...)
# # to call variable inside a class , (name of the class).variable

# from datetime import date

# class person:
#     person_count = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         person.person_count += 1
#     def info(self):     # Instance Method
#         return f'name: {self.name}, age:{self.age}'
#     @classmethod
#     def how_many_people(cls):
#         return cls.person_count

#     @classmethod
#     def create_with_a_string(cls,str_):
#         name,age = str_.split('-')
#         return cls(name,age)

#     @classmethod
#     def create_with_birthyear(cls, name, birthyear):
#         return cls(name, date.today().year - birthyear)

#     @staticmethod
#     def calculate_birthyear(person):
#         return date.today().year - person.age

#     def greet_():
#         return 'Hello'

# person1 = person('Adam', 25)
# person2 = person('John', 26)

# print(person.how_many_people())

# person3 = person.create_with_a_string('Kate-25')
# print(person.how_many_people())
# 'Kate-25'
# print(person3.name)

# person4 = person.create_with_birthyear('Jack', 1989)
# print(person4.name, person4.age)

# print(person.calculate_birthyear(person1))

# print(person.greet_())



# print(person.info(self=person1))
# print(person.info(person1))
# print(person1.info())









# # OOP Inheritance

# class Worker:
#     raise_percentage = 1.1
#     def __init__(self,name,surname,wage):
#         self.name = name
#         self.surname = surname
#         self.wage = wage
#         self.gmail = name + surname + '@corporation.com'

#     def info(self):
#         return f'name:{self.name}, surname: {self.surname}, wage: {self.wage}, gmail:{self.gmail}'



# worker1 = Worker('Adam', 'Sandler', 2000)
# worker2 = Worker('John', 'Doe', 1800)

# print(worker2.gmail)


# class dev(Worker):
#     raise_percentage = 1.2

#     def __init__(self,name,surname,wage,language):
#         super().__init__(name,surname,wage)     # Parent Class
#         self.language = language
#     raise_percentage = 1.2
#     def info(self):
#         return f'name:{self.name}, surname: {self.surname}, wage: {self.wage}, gmail: {self.gmail}, language: {self.language}'
#     def language_(self):
#         return f'language: {self.language}'

# dev1 = dev('Kate', 'Mccall', 2200, 'Python')
# dev2 = dev('Josh', 'Clusky', 2100, 'Java')



# class manager(Worker):

#     def __init__(self, name, surname, wage, workers = None):
#         super().__init__(name,surname,wage)
#         if workers == None:
#             self.workers = []
#         else:
#             self.workers = workers

#     def add_worker(self,worker):
#         if worker not in self.workers:
#             self.workers.append(worker)

#     def remove_worker(self,worker):
#         if worker in self.workers:
#             self.workers.remove(worker)

#     def show_workers(self):
#         for worker in self.workers:
#             print(worker.info())

# manager1 = manager('Abu', 'Dakar', 6000)

# manager1.add_worker(worker1)
# manager1.add_worker(dev1)

# manager1.show_workers()
# print('********')
# manager1.remove_worker(worker1)
# manager1.show_workers()







# print(dev2.gmail)
# print(worker1.raise_percentage)
# print(dev2.raise_percentage)

# print(dev2.info())
# print(dev1.info())
# print(worker1.info())

# print(dev1.language_())