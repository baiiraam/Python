# exercises


### AVERAGE OF N NUMBERS


num = int(input('how many numbers ? '))
total = 0

for n in range(num):
    enter_num = int(input('enter a number : '))
    total += enter_num

avg = total/num
print('average of numbers is: ', avg)






### SUM OF FIRST N POSITIVE INTEGERS

while True:
    num = input('enter the N : ')
    sum = 0
    if num == 'quit':
        break

    for n in range(int(num)):
        sum += n

    print(sum)






### CURRENT USERNAME


import getpass
print(getpass.getuser())







### PYTHON VERSION OF MINE


import sys
print(sys.version)







### DATE AND TIME NOW


import datetime
now = datetime.datetime.now()
print('current date and time is: ')
print(now.strftime('%y - %m - %d  %H : %M : %S'))





### TRIANGLE PATTERN?


for i in range(7):
    print('*'*i)


print(3, end = '')
print(4, end = '')
print(5, '\n')
print(6, '\n')


def right_pyramid(n):
    for row in range(1, n+1):
        start_index = n-row
        print(' '*start_index, end='')
        for star in range(row):
            print('*', end='')

        print('')

right_pyramid(6)







def star_pyramid(n):
    for row in range(1, n+1):
        start_index = n - row
        print(' ' * start_index, end = '')
        for star in range(row + row - 1):
            if star % 2 == 0:
                print('*', end = '')

            else:
                print(' ', end = '')
        print(' ')

star_pyramid(7)







### DATES, TIME


import datetime
print(datetime.datetime.now())


today = datetime.datetime.now()
print(today - datetime.timedelta(days = 1))


for i in range(7):
    print(today - datetime.timedelta(days = i))







### DUPLICATES


a = [7, 7, 7, 4, 4, 8, 8, 'the', 1, 2, 3, 4, 5, 6, 7]

from collections import Counter
print([element for element, count in Counter(a).items() if count > 1])





### polindrome


def if_polindrome(abc):
    if abc == abc[::-1]:
        print( 'polindrome')
    else:
        print( 'not polindrome')

if_polindrome('level')
if_polindrome('levels')





### number of vowels

while True:
    char = input('enter a sentence: ')
    vowel_list = ['e', 'u', 'i', 'o', 'a']
    count = 0

    if char == 'quit':
        break
    for i in char:
        if i in vowel_list:
            count += 1

    print('number of vowels: ', count)






### Prime or not


while True:
    count = 0
    num = input('enter a number: ')
    if num =='quit':
        break
    for i in range(1, int(num)):
        if int(num) % i == 0:
            count += 1
    if count == 1:
        print('it is a prime number')
    else:
        print('it is not a prime number')






# Factorial

while True:
    num = input('enter a number: ')
    final = 1
    if num == 'quit':
        print('...finishing operation...')
        break

    for i in range(1, int(num) + 1):
        final *= i

    print(num, ' factorial is ', final)





# Split ?

values = input('print some numbers separated with a comma: ')

list = values.split(',')
tuple = tuple(list)

print(list)
print(tuple)








# Project Euler 1, Python'a giris

# if we sum the numbers below 10 that are multiplies of either 3 or 5, it will be 3 + 5 + 6 + 9 = 23.
# What is the sum for all numbers below 1000 ?


def check(x):
    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False

sum = 0

for i in range(1, 1000):
    if check(i) == True:
        sum += i

print(sum)







# Fibonacci sequence is given as:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...   Starting with 1 and 2, add previous 2 terms to get the next one
# find the sum of even fibonacci numbers below 4 million

fibonacci = []
fibonacci.append(1)
fibonacci.append(2)

i = 2

while True:
    if fibonacci[i-1] + fibonacci[i-2] < 4000000:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        i += 1
    else:
        break
sum = 0
for i in fibonacci:
    if i % 2 == 0:
        sum += i

print(sum)
print(len(fibonacci))
for i in fibonacci:
    print(i, end = ', \t')







# a = 1
# b = 2

# sum = 2

# while True:
#     c = a + b
#     a = b
#     b = c

#     if c % 2 == 0:
#         sum += c
#     if c > 4000000:
#         break

# print(sum)






# the prime factors of 13195 are 5, 7, 13, and 29.
# what is the largest prime factor of number 600851475143 ?


# check for prime
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def highest_prime_factor(number):
#     highest_prime = 1

#     while number % 2 == 0:
#         highest_prime = 2
#         number //= 2

#     for i in range(3, int(number ** 0.5) + 1):
#         while number % i == 0:
#             highest_prime = i
#             number //= i

#     if number > 2:
#         highest_prime = number

#     return highest_prime

# print(highest_prime_factor(13195))





# import math

# def prime_check(x):
#     is_prime = True

#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             is_prime = False
#             continue
#     return is_prime

# number = 600851475143

# biggest_prime = 1

# for i in range(2, int(math.sqrt(number))):
#     if number % i == 0 and prime_check(i):
#         biggest_prime = i

# print(biggest_prime)






# def check_polindrome(x):
#     str_num = str(x)
#     reverse_num = str_num[::-1]
#     if str_num == reverse_num:
#         return True
#     else:
#         return False

# a = 0
# b = 0
# big_polindrome = 0
# for i in range(100,1000):
#     for j in range(100,1000):
#         if check_polindrome(i*j) and i*j > big_polindrome:
#             a = i
#             b = j
#             big_polindrome = i*j

# print(big_polindrome, a, b, end = ' ')







### Greatest Common Divisor and Least Common Multiple


# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# def lcm(a, b):
#     return a * b // gcd(a, b)







# Least Common Multiple,    functools

# import math
# import functools

# def gcd(x, y):
#     return math.gcd(x, y)

# def lcm(x, y):
#     return x*y // gcd(x, y)

# list = range(1, 21)

# result = functools.reduce(lcm, list)

# print(result)







# Sum Square Difference

# sum_of_squares = 0
# square_of_sum = 0

# sum = 0

# for i in range(1, 101):
#     sum += i
#     sum_of_squares += i*i

# result = sum*sum - sum_of_squares
# print(result)







# 10001st Prime    BRUH MOMENT HAPPENED

# import math

# def prime_check(x):
#     is_prime = True
#     if x == 2:
#         return True
#     else:
#         for i in range(2, int(math.sqrt(x)) + 1):
#             if x % i == 0:
#                 is_prime = False
#                 break
#             return is_prime

# i = 2
# prime_count = 0

# while True:
#     if prime_check(i):
#         prime_count += 1
#     if prime_count == 10001:
#         print(i)
#         break
#     i += 1






# Largest product in a series







# Special Pythagorean Triplet

# for a in range(1, 1000):
#     for b in range(1, 1000 - a):
#         c = 1000 - a - b
#         if a*a + b*b == c*c and a < b < c:
#             print(a*b*c)
#             print(a, b, c)







# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)








# Summation of Primes

# def prime_check(x):
#     is_prime = True
#     if x == 2:
#         return True
#     if x % 2 == 0:
#         return False
#     for i in range(3, int(x ** 0.5) + 1, 2):
#         if x % i == 0:
#             is_prime = False
#             break
#     return is_prime

# n = 2
# sum = 0

# while True:
#     if n == 2000000:
#         break
#     else:
#         if prime_check(n):
#             sum += n
#     n += 1

# print(sum)
























# prime_list = []
# prime_list.append(2)
# num = 3

# while True:
#     prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             prime = False
#             break
#         if prime:
#             prime_list.append(num)
#             if len(prime_list) == 10001:
#                 break
#     num += 1

#     print(prime_list[10000])