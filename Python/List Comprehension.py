# List Comprehension

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# create a list that contains the numbers in the list above
# list2 = []
# for number in numbers:
#     list2.append(number)
# print(list2)


# list3 = [number for number in numbers]
# print(list3)


# create a list that contains the square values of the list above

# list2 = []
# for number in numbers:
#     list2.append(number*number)
# print(list2)


# list3 = [number*number for number in numbers]
# print(list3)


# even numbers

# list2 = []
# for number in numbers:
#     if number % 2 == 0:
#         list2.append(number)
# print(list2)

# list3 = [number for number in numbers if number % 2 == 0]
# print(list3)


# squares of even numbers

# list2 = []
# for number in numbers:
#     if number % 2 == 0:
#         list2.append(number * number)
# print(list2)


# list3 = [number * number for number in numbers if number % 2 == 0]
# print(list3)


# squares of even numbers which are greater than 4

# list2 = []
# for number in numbers:
#     if number > 4 and number % 2 == 0:
#         list2.append(number * number)
# print(list2)


# list3 = [number * number for number in numbers if number > 4 and number % 2 == 0]
# print(list3)


# 1,a  1,b  1,c  1,d  2,a  ... 4,d 
# numbers = [1, 2, 3, 4]
# letters = 'abcd'

# list2 = []
# for number in numbers:
#     for letter in letters:
#         list2.append((number, letter))
# print(list2)


# list3 = [(number, letter) for number in numbers for letter in letters]
# print(list3)


# squares of numbers that are in 1st list but not in 2nd list

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [2,3,6,9,5]

# list3 = []
# for i in list1:
#     if i not in list2:
#         list3.append(i * i)
# print(list3)

# list4 = [i * i for i in list1 if i not in list2]
# print(list4)


# create a list in shape [1,2,3,4,5,6,7,8,9,10,11,12]

# list_ = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]
# list2 = []
# for i in list_:
#     for j in i:
#         list2.append(j)
# print(list2)

# list3 = [j for i in list_ for j in i]
# print(list3)


# hm

# list_methods = []
# # print(dir(list))        # functions that are in list, dir(list)
# for method in dir(list):
#     if method.startswith('__'):
#         continue
#     list_methods.append(method)
# print(list_methods)

# list1 = [method for method in dir(list) if not method.startswith('__')]
# print(list1)