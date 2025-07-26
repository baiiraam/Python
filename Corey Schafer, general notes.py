### COREY SCHAFER


# print('yo yo')
# my_message = 'hello world'
# print(my_message)


# message = 'bobby\'s world'          # escape character \
# print(message)


# message = "bobby's world"
# print(message)



# message = 'Hello World'
# print(len(message))
# print(message[0])
# print(message[6])
# print(message[0:5])
# print(message[:5])
# print(message[6:])
# print(message.lower())
# print(message.upper())
# print(message.count('l'))
# print(message.find('World'))
# message = message.replace('Hello', 'Hey')
# print(message)



# greeting = 'hey'
# name = 'mike'
# hey_message = greeting + ', ' + name
# print(hey_message) 


# message = '{}, {}. Welcome!'.format(greeting, name)
# print(message)


# new_message = f'{greeting}, {name}. Welcome!'
# print(new_message)


# verynew_message = f'{greeting}, {name.upper()}. Welcome!'          # with this, f'{}' method, you can place function inside placeholder({})
# print(verynew_message)

# print(dir(name))          # all things you can use with variable

# print(help(str))          # help with smth used









### SLICING LISTS AND STRINGS



# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9 index
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 index negative


# list[start:end:step]


# print(my_list)
# print(my_list[0])     # 0th index in list
# print(my_list[-10])   -10th index in list
# print(my_list[0:5])     #from 0th index to 5th index, 5th not included
# print(my_list[3:8])
# print(my_list[-7:-2])
# print(my_list[1:-2])
# print(my_list[1:])      # 1st index to the end
# print(my_list[:9])
# print(my_list[:-1])
# print(my_list[:])
# print(my_list[2:-1:2])    # from 2nd index -1st, only 2nd values
# print(my_list[2:-1:1])
# print(my_list[-1:2:-1])
# print(my_list[-2:1:-1])
# print(my_list[-2:1:-2])
# print(my_list[::-1])      reverse list


# url = 'I watch Suits'
# print(url)


# print(url[::-1])
# print(url[-5:])
# print(url[2:])









# STRING FORMATTING, ADVANCED OPERATIONS FOR DICTS, LISTS, NUMBERS, AND DATES



# person = {'name': 'Bayram', 'age': 20, 'movie': 'Suits'}


# l = ['profesyonel otuzbirci', '31', 'turkish']


# for i in range (1,11):
    # sentence = 'value is {}'.format(i)
    # print(sentence)


# for i in range (1,11):
    # sentence = 'value is {:02}'.format(i)
    # print(sentence)


# sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)


# import datetime
# my_date = datetime.datetime(2024, 1, 8, 22, 22)


# sentence = '{:%B %d, %Y}'.format(my_date)
# sentencenew = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
# print(sentencenew)




# pi = 3.14159265


# sentence = 'pi is equal to {:.3f}'.format(pi)
# print(sentence)


# sentence_neg1 = 'my name is {0[0]} and I am {0[1]} and also {0[2]}.'.format(l)
# print(sentence_neg1) 


# sentence = 'My name is {}. I am {} years old. I watch {}.'.format(person['name'], person['age'], person['movie'])
# print(sentence)


# sentence_1 = 'My name is {0}, I am {1} years old, I watch {2}.'format(person['name'], person['age'], person['movie'])
# print(sentence_1)


# tag = 'h1'
# text = 'this is a headline'


# sentence_2 = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence_2)


# sentence_3 = 'my name is {0[name]} and I am {0[age]} years old, I watch {0[movie]}.'.format(person,person)
# print(sentence_3)


# sentence_4 = 'my name is {0[name]} and I am {0[age]} years old, I watch {0[movie]}.'.format(person)
# print(sentence_4)









# INTEGERS AND FLOATS - WORKING WITH NUMERICAL DATA


# num = 3.14


# print(type(num))


# arithmetic operators
# addition          3 + 2
# substraction      3 - 2
# multiplication    3 * 2
# division          3 / 2
# floor division    3 // 2
# exponent          3 ** 2
# modulus           3 % 2           duduw qaliq


# comparisons :
# equal             3 == 2
# not equal         3 != 2
# greater than      3 > 2
# less than         3 < 2
# greater or equal  3 >= 2
# less or equal     3 <= 2



# print(11 % 6)


# num = 1
# num = num + 1
# print(num)


# num += 1            meaning, num = num + 1
# print(num)


# print(abs(-3))
# print(round(3.31))
# print(round(3.69, 1))


# num_1 = 31
# num_2 = 69
# print(num_1 < num_2)


# num_1 = '100'
# num_2 = '200'
# print(num_1 + num_2)


# num_1 = int(num_1)
# num_2 = int(num_2)
# print(num_1 + num_2)









# LISTS, TUPLES, SETS.          STARTING WITH LISTS



# courses = ['history', 'math', 'physics', 'compsci']
# courses_2 = ['some', 'variables', 'to', 'add', 'to', 'this', 'list']
# nums = [1, 4, 15, 9, 7]


# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[-1])
# print(courses[3])
# print(courses[0:3])
# print(courses[:3])
# print(courses[1:])


# courses.remove('history')
# print(courses)


# courses.pop()
# print(courses)


# popped = courses.pop()
# print(popped)


# courses.reverse()
# print(courses)


# courses.sort()                        # sorted in alphabetical order
# print(courses)
# courses.sort(reverse = True)          # sorted in reverse alphabetical order
# print(courses)


# sorted_courses = sorted(courses)      # sorting function        
# print(sorted_courses)


# nums.sort()                           # numbers sorted in ascending order
# print(nums)
# nums.sort(reverse = True)             # numbers sorted in descending order
# print(nums)


# print(min(nums))                      # min value of list
# print(max(nums))                      # max value of list
# print(sum(nums))                      # sum of list values


# print(courses.index('CompSci'))       # index of a certain item in a list


# print('math' in courses)              # if item is in list or not


# for item in courses:
#     print(item)


# for i in courses :
#     print(i)


# for index, course in enumerate(courses):
#     print(index, course)


# for index, course in enumerate(courses, start =1):
#     print(index, course)


# course_str = ', '.join(courses)         # join list as a string
# course_str1 = ' - '.join(courses)
# print(course_str1)


# new_list = course_str1.split(' - ')     # attention to inside of split in here and upper part
# print(new_list)


# courses.append('mastering 31')
# print(courses)


# courses.insert(0, 'skibidi')
# print(courses)


# courses.insert(0, courses_2)
# print(courses)


# courses.append(courses_2)
# print(courses)


# courses.extend(courses_2)
# print(courses)









# its a mad mad world that we living in (whats wrong with us), TUPLES



# list_1 = ['history', 'bullshit', 'math', 'nice']
# list_2 = list_1


# print(list_2)
# print(list_1)


# list_2[0] = 'art'

# print(list_2)
# print(list_1)


# Immutable

# tuple_1 = ('history', 'math', 'physics', 'compsci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'art'      # tuples are immutable, cannot be changed. haha

# print(tuple_1)
# print(tuple_2)




# Sets



# cs_courses = {'history', 'math', 'physics', 'compsci'}
# # no duplicates in sets
# art_courses = {'history', 'math', 'art', 'design' }


# # print(cs_courses)
# # print('math' in cs_courses)


# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))


# # Empty Lists
# empty_list = []
# empty_list = list()


# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()


# # Empty Sets
# empty_set = {}
# empty_set = set()









# Dictionaries



# student = {'name' : 'John' , 'age' : 25 , 'courses' : ['Math', 'CompSci'], 1 : 'huvulele one'}

# student['phone'] = '055-555-55-55'
# student['name'] = 'Jack'
# student.update({'name' : 'bomboclaaat', 'age' : 26 , 'phone' : '055-611-14-30' })
# del student['age']
# name = student.pop('name')
# print(name)
# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

# for key in student:
#     print(key)

# for key, value in student.items():
#     print(key,value)


# print(student)
# # print(student['name'])
# print(student['courses'])
# print(student['courses'][0])
# print(student[1])
# print(student.get('name'))
# print(student.get('phone'))
# print(student.get('phone', 'not found'))









# Conditionals and Booleans

# comparisons:
# equal:                  ==
# not equal:              !=
# greater than:           >
# less than:              <
# greater or equal:       >=
# less or equal:          <=
# object identity:        is



# if True:
#     print('Conditional was True')
# if False:
#     print('something')

# language = 'python'
# language = 'java'
# language = 'c'



# if language == 'python':
#     print('language is python')
# elif language =='java':
#     print('language is java')
# elif language == 'javascript':
#     print('language is javascript')
# else:
#     print('no match')



# user = 'admin'
# logged_in = True
# logged_in = False


# if user == 'admin' and logged_in:
#     print('admin page')
# else:
#     print('insufficient credentials')


# if not logged_in:
#     print('please log in')
# else:
#     print('welcome')



# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# print(id(c))
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
# print(id(a) is id(c))



# False Values:
    # False
    # None
    # zero of any numeric type
    # any empty sequence. for example, '', (), [].
    # any empty mapping. for example, {}.

# condition = ''
# if condition:
#     print('evaluated as true')
# else:
#     print('evaluated as false')









# Loops and Iterations



# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     if num == 3:
#         print('found!')
#         # break
#         continue
#     print(num)

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)



# for i in range(10):
# for i in range(1,11):

#     print(i)



# x = 0

# # while x < 10:
# while True:
#     # if x == 5:
#     #    break
#     print(x)
#     x += 1

# ctrl + C  breaks out of infinite loop









# Functions



# def hello_func():
#     # pass
#     # print('hello')
#     return 'hello'

# # hello_func()
# print(hello_func().upper())



# def hello_func(greeting):
#     return '{} function.'.format(greeting)

# print(hello_func('hi'))



# def hello_func(greeting, name = 'you'):
#     return '{}, {}.'.format(greeting, name)


# print(hello_func('hi', name = 'kalunga'))



# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# courses = ['math', 'art']
# info = {'name' : 'john' , 'age' : 22}

# # student_info('math', 'art', name = 'john', age = 22)
# student_info(*courses, **info)




# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def is_leap(year):
#     return year % 4 == 0  and  (year % 100 != 0 or year % 400 == 0)

# def days_in_month(year, month):
#     if not 1 <= month <= 12:
#         return 'invalid month'
    
#     if month == 2 and is_leap(year):
#         return 29
    
#     return month_days[month]

# print(days_in_month(2017, 2))