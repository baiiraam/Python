### variables, assigning variable to smth that we will use, updating the variable

#character_name = "John Doe"
#character_age = "31"
#character_name_bruh = "Candice"
#print (character_name + " is " + character_age + " years old ")
#print (character_name + " does not know who is " + character_name_bruh )
#print ("O_O bruhhhh")

#character_name = "Mike O Hearn"
#character_age = "69"
#character_name_bruh = "Deez"

#print (character_name + " came and said :")
#print ("I am " + character_age + " years old. You should let the hostage go, " + character_name_bruh)
#print ("evil laugh came from the sky, as he said " + character_name_bruh)





### string is "xxx" (inside quotation mark), number is 50 without quotation mark, statements are True and False





# string = "haha, 31, 59.3169"
# number = 100
# is_male = True
# is_female = False





# new line inside string    \n

#print ("smth\nsomeone")
# escape character
#print ("smth\"someone")
#phrase = "3169 don pollo"
#print (phrase)





# lowercase, uppercase

#phrase = "KVJBSKLJASBLKAJBLKAJBDA"
#abc = "ksdjnskjksjnfd"
#print(phrase.lower())
#print(abc.upper())





# check if lower(upper)case

#abc = "dsjkakjk"
#print(abc.isupper())
#str = "kajnakjsna"
#print(str.islower())

#abc = "sajknasjn"
#print(abc.upper().isupper())





# length 

#str = "skjfnkjnalkfnlanlsdknla"
#print(len(str))



#str = "fjdkfjfjkdfndjskmvnfdjkm"
#sss = "0123456789..."
#print(str[0])





# finding the index of a string, replace

#str = "cguhvhjijbnjkl"
#print(str.index("l"))
#abc = "banmin heyetindeki turbanin yanindaki winston compact boz"
#print(abc.index("boz"))
#print(abc.replace("turbanin", "zibilliyin"))





# numbers

#print(31 * 69 + 420)

#print(10%3)   # remainder
#num = 31
#print(num)
#print(str(num))

#print(str(num) + " is my favorite number")   # if you want to use number alongside string

#mynum = -69
#print(abs(mynum))   # absolute value

#print(pow(5, 5))   # power

#print(max(1, 9))   # returns higher value

#print(min(2, 7))   # returns lower value

#print(round(3.5))   # round function





#to use (complex) math functions :

#from math import *

#num = 5.69
#print(floor(3.9))    # 3.9 ---> 3     lower closest integer

#print(ceil(2.001))   # 2.001 ---> 3   higher closest integer

#print(sqrt(1024))   # square root





### input from user

#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " + name + " !")
#print(name + ", You are " + age + " years old!")





### building a basic calculator

# input from user will be converted to string by default !!!

#num1 = input("Enter first number: ")   # it is a string !

#num2 = input("Enter second number: ")   # it is a string !

#result = num1 + num2   # result is a string !

#resultnew = int(num1) + int(num2)   # converting to integer, decimals will cause error

#resultnewnew = float(num1) + float(num2)   # converting to number, decimals will be accepted, no error

#print(resultnewnew)





### mad libs game

#color = input("Enter a color: ")
#pluralnoun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")

#print("roses are " + color)
#print(pluralnoun + " are blue")
#print("I love " + celebrity)





### lists

#friends = ["Tony", "Paulie", "Carl", "Niko", "Michael", "Vito"]

#friends[1] = "Gotti"

#print(friends)

#print(friends[3])   # Tony = 0 , Paulie = 1, Carl = 2, ...

#print(friends[-3])   # Tony = 0, Vito = -1, ...

#print(friends[1:])   # elements after [1]

#print(friends[1:5])   # [1] to [5], [5] not included





### List functions

#lst = ["lcsklsd", "ajcnajcs", "apodjoiaj", "dfoikodkm", "oqidck", "eoiunkac"]
#nmb = [1, 2, 3, 4, 5, 6, 7, 8]
#nmb.append(1)
#nmb.append(1)

#nmb2=nmb.copy()   # copies the list

#nmb.reverse()   # reverses the order, reads backwards

#lst.sort()   # sorts strings in alphabetical, and numbers in ascending order

#lst.extend(nmb)   # extend function

#lst.append("Ezio")   # append function

#lst.insert(2, "Corleone")   # insert function

#nmb.remove(5)   # remove function

#lst.clear()   # clear the list

#lst.pop()   # removes last element from list

#print(nmb.index(5))   # returns the index of an element inside the list

#print(nmb.count(1))   # counts how many times an element is showed up in list
#print(nmb)





### tuples          Tuples cannot be modified.

#coordinates = (2, 8)   # creating a tuple

#print(coordinates[0])   # accessing an element inside tuple

#crd = [(12, 54), (43, 78), (65, 98)]   # list of tuples
#print(crd[1])   





### functions

#def sayhi():   # defining function
#    print("hey user !")

#sayhi()   # calling our function

#def say_hi(name, age):   
#    print("hey " + name + " , you are " + age + " years old")

#say_hi("Bruh", "31")

#say_hi("Don Pollo", "69")

#def random(name):
#    print(name)
#random("hey")





### return statement

# function for 3rd power

#def cube(num):
#    return num * num * num


#print(cube(3))

#def fourth(num):
#    return num*num*num*num

#result = fourth(4)
#print(result)

#print(fourth(3))



### if statements  ,  or ---> one of statements True  ,  and ---> both of statements True

#is_male = False
#is_tall = True

#if is_male or is_tall:       # if statement returns or equals True, code is executed. Otherwise, else condition should be included. if True ---> code execution(without else)
#    print("you are a male or tall or both bruh fr fr fr")
#else:                        # code is executed if "if" statement is False.
#    print("you are a female and short")
#if is_male and is_tall:
#    print("you are a tall male")
#elif is_male and not(is_tall):
#    print("you are a short male")
#elif not(is_male) and is_tall:
#    print("you are a tall female")
#else:
#    print("you are either not male or not tall")





### if statements and comparisons

#def max_num(num1, num2, num3):
#    if num1 >= num2 and num1 >=num3:
#        return num1
#    elif num2 >= num1 and num2>=num3:
#        return num2
#    else:
#        return num3
    
#print(max_num(12, 34, -31))

# != --- not equal





### building a better calculator

#num1 = float(input("first number: "))
#op = input("operator: ")
#num2 = float(input("second number: "))

#if op == "+":
#    print(num1 + num2)
#elif op == "-":
#    print(num1 - num2)
#elif op == "*":
#    print(num1 * num2)
#elif op =="/":
#    print(num1 / num2)
#else:
#    print("invalid operator")