###   PYTHON CRASH COURSE


### Changing Case in a String with Methods



# name = 'mike ohearn'
# tt = name.title()         uppercase first strings in words
# print(tt)
# print(name.title())


# name = 'Darko Brevic'     
# print(name.upper())       uppercase whole string
# print(name.lower())       lowercase all string
# upp = name.upper()
# loww = name.lower()
# print(upp)
# print(loww)



### Combining or Concatenating Strings



# first_name = 'mike'
# last_name = 'ross'
# full_name = first_name + ' ' + last_name
# print(full_name)
# print(full_name.title())

# message = 'Hello, ' + full_name.title() + '!'
# print(message)



# Adding Whitespace to Strings with Tabs or Newlines



# print("hello")
# print("\thello")            # add tab to your text


# print("languages:\nPython\nC\nJavaScript")          # add a newline in a string
# print("Languages:\n\tPython\n\tC\n\tJavaScript")



### Stripping Whitespace



# favorite_language = 'python '
# print(favorite_language.rstrip() + '42')            # removes blank space
# fav_lang = favorite_language.rstrip()
# print(fav_lang + '42')


# fav_lang = ' python '
# fav_lang.lstrip() -- 'python '
# fav_lang.rstrip() -- ' python'
# fav_lang.strip() -- 'python'
# fav_lang = fav_lang.strip()
# print('42' + fav_lang + '42')



### Numbers



#   +   add
#   -   substract
#   *   multiply
#   /   divide
#   **  exponent


# age = 23
# message = 'Happy' + str(age) + 'rd Birthday'        # 23 is an integer. Code must interpret it as a string. str() function helps number -- string
# print(message)


# import this



### Lists, I guess



# list = ['ame', 'bato', 'cera', 'diqe']
# print(list)
# print(list[0])
# print(list[0].title())          # capitalizing first letter
# print(list[1])
# print(list[3])
# print(list[-1])

# message = 'Wow, I did not know that you were a ' + list[1].title() + '.'
# print(message)

# moto = ['yamaha', 'suzuki', 'honda']
# print(moto)

# moto[0] = 'brbrpatapim'
# print(moto)


# moto.append('saturnosaturnita')
# print(moto)


# new_list = []
# new_list.append('siiiiiuuuu')
# new_list.append('ronaldooooo')      # add as last index to the list
# print(new_list)


# new_list.insert(0, 'portugal')
# new_list.insert(2, 'suxarik')       # insert to specific index
# print(new_list)


# del new_list[0]                     # delete an item
# print(new_list)


# cars = ['merc', 'bmw', 'audi', 'porsche', 'opel']
# cars_special = cars.pop()           # popped item
# print(cars)                         # item popped, new list BRRRR
# print(cars_special)


# aze_cars = ['Mercedes - Benz', 'BMW', 'Opel']
# last_owned = aze_cars.pop()
# print('The last car I owned was ' + last_owned.title() + '.')


# first_owned = aze_cars.pop(0)       # pop specified item
# print('My first car was ' + first_owned.title() + '.')


# list_1 = ['item', 'one', 'specific', 'history', 'math', 'art']
# list_1.remove('item')
# print(list_1)


# some_index = 'specific'
# list_1.remove('specific')
# print(list_1)
# print('\n' + some_index.title() + ' is an item of the list')




### Organizing a List


# cars = ['audi', 'bmw', 'mercedes', 'opel', 'subaru']
# cars.sort()
# print(cars)


# cars.sort(reverse = True)
# print(cars)


# print('Original List is: ')
# print(cars)


# print('\nSorted List: ')
# print(sorted(cars))                 # sorted() function present list in sorted order but does not affect the actual order of the list


# print('\nAgain original List: ')
# print(cars)
# print('\n')


# cars.reverse()
# print(cars)
# print('\n')


# print('length of the list is : ' + str(len(cars)))




### Looping Through an Entire List


# list = ['this', 'is', 'a', 'list']
# for element in list :
#     print(element)
# for i in list:
#     print(i)


# magicians = ['alice', 'david', 'carolina'] 
# for magician in magicians:
#     print(magician.title() + ', that was great!')
#     print('I cannot wait to see your next trick, ' + magician.title() + '.\n')
# print('Thank you, everyone. That was a great magic show!')    





### Making Numerical Lists



# for value in range(1,5):
#     print(value)
# for i in range(1,9):
#     print(i)


# numb = list(range(1,6))
# print(numb)


# even_numb = list(range(2,11,2))
# print(even_numb)


# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)


# squares =[]
# for value in range(1,11):
#     squares.append(value ** 2)
# print(squares)



# digits = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 0]
# print(min(digits), max(digits), sum(digits), 'aha')
# print(max(digits))
# print(sum(digits))



# squares = [value ** 2 for value in range(1, 11)]
# print(squares)




### Working with Part of a List



# players = ['miguel', 'carlos', 'jumirez', 'suarez', 'taco']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])

# print('First three players on the team are: ')
# for player in players[0:3]:
#     print(player.title())



# my_foods = ['gabagool', 'pizza', 'cake']
# friend_foods = my_foods[:]
# print('My favorite foods are: ')
# print(my_foods)

# print('\nMy friends favorite foods are: ')
# print(friend_foods, '\n')

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print('My favorite foods are: ')
# print(my_foods)

# print('\nMy friends favorite foods are: ')
# print(friend_foods)




### Tuples



# dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[1])
# print(dimensions)
# print('Original dimensions: ')
# for dimension in dimensions:
#     print(dimension)
# dimensions = (400,100)
# print('\nModified dimensions: ')
# for dimension in dimensions:
#     print(dimension)




### IF Statements


# cars = ['bmw', 'audi', 'mercedes', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# variable = 'audi'
# print(variable == 'audi', variable == 'Audi', variable == 'anything other than audi with lowercase')

# requested_topping = 'mushrooms'
# if requested_topping != 'anchoives':
#     print('Hold the anchoives!')


# age = 18
# print(age == 18, age == 42)


# answer = 17
# if answer != 42:
#     print('That is not the correct answer. Please try again! ')


# age = 20
# print(age < 21, age < 20, age >= 20, age > 21, age == 20)


# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 21)
# age_1 = 22
# print(age_0 >= 21 and age_1 >= 21)


# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 or age_1 >= 21)
# age_0 = 18
# print(age_0 >= 21 or age_1 >= 21)


# requested_toppings = ['mushrooms', 'onions', 'sausage']
# print('mushrooms' in requested_toppings)
# print('pepperoni' in requested_toppings)


# banned_users = ['andrew', 'gabriel', 'simba']
# user = 'john'
# print(user not in banned_users)
# if user not in banned_users:
#     print(user.title() + ', you can post a response if you wish.')



# age = 19
# if age >= 18:
#     print('You are old enough to vote!')
#     print('Have you registered to vote yet?')
# else:
#     print('Sorry, you are too young to vote.\nPlease register to vote as soon as you turn 18!')



# age = 12
# if age < 4:
#     print('Your admission cost is $0.')
# elif age  < 18:
#     print('Your admission cost is $5.')
# else:
#     print('Your admission cost is $10.')



# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# else:
#     price = 5
# print('Your admission cost is $' + str(price) + '.')



# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 65:
#     price = 5
# print('Your admission cost is $' + str(price) + '.')



# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms.\n')
# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni.\n')
# if 'extra cheese' in requested_toppings:
#     print('Adding extra cheese.\n')
# print('Finished making your pizza!')




### Using If Statement With Lists


# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'pepperoni']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('Sorry, we are out of green peppers.')
#     else:
#         print('Adding ' + requested_topping + '.')

# print('\nYour pizza is ready!')



# req_toppings = []
# if req_toppings:                    # when name of a list is used in if statement, if that list has at least one item, it returns True. IF not, it returns False.
#     for req_topping in req_toppings:
#         print('Adding ' + req_topping + '.')
#     print('\nYour pizza is ready.')
# else:
#     print('Are you sure you want a plain pizza???')




# available_toppings = ['mushrooms', 'olives' , 'green peppers', 
#                       'pepperoni', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print('Adding ' + requested_topping + '.')
#     else:
#         print('Sorry, we do not have ' + requested_topping + '.')
# print('\nFinished making your pizza!')




### Dictionaries

# alien_0 = {'color' : 'green', 'points' : 5}
# print(alien_0['color'])
# print(alien_0['points'])


# new_points = alien_0['points']
# print('You just earned ' + str(new_points) + ' points!')


# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)


# alien_0 = {'color' : 'green'}
# print('The alien is ' + alien_0['color'] + '.')

# alien_0['color'] = 'yellow'
# print('The alien is now ' + alien_0['color'] +'.')


# alien_0 = {'x_position' : 0 , 'y_position' : 25 , 'speed' : 'medium'}
# alien_0['speed'] = 'fast'
# print('Original x_position: ' + str(alien_0['x_position']))
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] =='medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print('New x_position: ' + str(alien_0['x_position']))



# alien_0 = {'color' : 'green', 'points' : 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)



# favorite_languages = {'jen' : 'python', 'sarah' : 'c', 'edward' : 'ruby',
#                       'phil' : 'python'}
# print("Sarah's favorite language is " + favorite_languages['sarah'].title()
#       + '.')




### Looping Through a Dictionary

# user_0 = {'username' : 'efermi',
#           'first' : 'enrico',
#            'last' : 'fermi' }
# for key, value in user_0.items():
#     print('\nKey: ' + key)
#     print('Value: ' + value)



# favorite_languages = {'jen' : 'python', 'sarah' : 'c', 'edward' : 'ruby',
#                       'phil' : 'python'}
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(' Hi ' + name.title() +
#               ', I see your favorite language is ' +
#               favorite_languages[name].title() + '!')
        

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ', thank you for taking the poll.\n')


# print('The following languages have been mentioned: ')
# for language in favorite_languages.values():
#     print(language.title())
# for language in set(favorite_languages.values()):
#     print(language.title())


# if 'erin' not in favorite_languages.keys():
#     print('Erin, take our poll!')



# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + '.')
# for name in favorite_languages.keys():
#     print(name.title())
# for name in favorite_languages:
#     print(name.title())




### Nesting

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)



# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     if alien['color'] == 'yellow':          # difference between if and elif
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15

# for alien in aliens[:5]:
#     print(alien)
# print('...')

# print('Total number of aliens: ' + str(len(aliens)))



# pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}
# print('You ordered a ' + pizza['crust'] + '-crust pizza' + 
#       ' with the following toppings:')
# for  topping in pizza['toppings']:
#     print('\t' + topping)



# favorite_languages = {'jen': ['python', 'ruby'],
#                       'sarah': ['c'],
#                       'edward': ['ruby', 'go'],
#                       'phil': ['python', 'haskell']}

# for name, languages in favorite_languages.items():
#     print('\n' + name.title() + "'s favorite languages are: ")
#     for language in languages:
#         print('\t' + language.title())



# users = {
#     'aeinstein': {
#                 'first': 'albert',
#                 'last': 'einstein',
#                 'location': 'princeton'
#                  },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris'
#               }
#         }

# for username, user_info in users.items():
#     print('\nUsername: ' + username)
#     full_name = user_info['first'] + ' ' + user_info['last']
#     location = user_info['location']
#     print('\tFull name: ' + full_name.title())
#     print('\tLocation: ' + location.title())




### User Input and While Loops

# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)


# name = input('Please enter your name: ')
# print('Hello, ' + name + "!")


# prompt = 'If you tell us who you are, we can personalize the messages you see.'
# prompt += "\nWhat is your first name?"

# name = input(prompt)
# print('\nHello, ' + name + "!")



# age = input("How old are you? ")
# age = int(age)
# print(age >= 18)


# height = input('How tall are you, in meters? ')
# height = float(height)              # int() turns into integer, float() turns to float

# if height >= 1.80:
#     print("You are tall enough to ride!")
# else:
#     print('\n You will ride when you are taller.')


# num = input('Enter an integer number: ')
# num = int(num)

# if num % 2 == 0:
#     print('\nThe number ' + str(num) + ' is even.')
# else:
#     print('\nThe number ' + str(num) + ' is odd.')




### Introducing While Loops

# num = 1
# while num <= 5:
#     print(num)
#     num += 1



# prompt = '\nTell me something, and I will repeat it back to you: '
# prompt += "\nEnter 'quit' to end the program."

# message = ''
# while message != 'quit':
#     message = input(prompt)
#     # if message != 'quit':
#         print(message)



# prompt = '\nTell me something, and I will repeat it back to you: '
# prompt += "\nEnter 'quit' to end the program."

# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)



# prompt = '\nPlease enter the name of a city you have visited below :'
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print("I would love to go to " + city.title() + '!')



# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         continue
#     print(num)



# x = 1
# while x<= 5:
#     print(x)
#     x+=1                # when infinte loop, you can ctrl-C




### Using a while Loop with Lists and Dictionaries



# unconfirmed_users = ['alice', 'brian' ,'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print('Verifying user: ' + current_user.title())
#     confirmed_users.append(current_user)

# print('\nThe following users have been confirmed:')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())



# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)



# responses = {}

# polling_active = True

# while polling_active:
#     name = input('\nWhat is your name? ')
#     response = input('Which mountain would you like to climb someday? ')
#     responses[name] = response
#     repeat = input('Would you like to let another person respond? (yes/ no) ')
#     if repeat == 'no':
#         polling_active = False

# print('\n--- Poll Results ---')
# for name,response in responses.items():
#     print(name + ' would like to climb ' + response + '.')




### Functions

# def greet_user():
#     print('Hello!')
# greet_user()



# def greet_user(username):
#     print('Hello, ' + username.title()+ '!')
# greet_user('jack')



### Passing Arguments

# def describe_pet(animal_type, pet_name):
#     print('\nI have a ' + animal_type + '.')
#     print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
# describe_pet('hamster', 'hamhamham')
# describe_pet('dog', 'alabay')

# describe_pet(animal_type = 'cat', pet_name = 'cupa')
# describe_pet(pet_name = 'qurdbasar', animal_type = 'dog')



# def describe_pet(pet_name, animal_type = 'dog'):
#     print('\nI have a ' + animal_type + '.')
#     print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
# describe_pet(pet_name = 'billie')

# describe_pet('billie')

# describe_pet(pet_name = 'qurdbasar', animal_type = 'dog')


# ## if you do : def describe_pet(pet_naame, animal_type = 'dog'):
# # all of the following calls would work for this function:
# # a dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name = 'willie')

# # a hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name = 'harry', animal_type = 'hamster')
# describe_pet(animal_type = 'hamster', pet_name = 'harry')




### Return Values

# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# def getformattedname(firstname, middlename, lastname):
#     fullname = firstname + ' ' + middlename + ' ' + lastname
#     return fullname.title()

# musician = getformattedname('john', 'lee', 'barista')
# print(musician)



# def getformattedname_1(firstname, lastname, middlename = ''):
#     if middlename:
#         fullname = firstname + ' ' + middlename + ' ' + lastname
#     else:
#         fullname = firstname + ' ' + lastname
#     return fullname.title()
# musician = getformattedname_1('jimi', 'hendrix')
# print(musician)
# musician = getformattedname_1('john', 'barista', 'lee')
# print(musician)



# def buildperson(firstname, lastname):
#     person = {'first' : firstname , 'last' : lastname}
#     return person
# musician = buildperson('jimi', 'hendrix')
# print(musician)



# def buildperson_1(firstname, lastname, age = ''):
#     person = {'first' : firstname , 'last' : lastname}
#     if age:
#         person['age'] = age
#     return person

# musician = buildperson_1('jimi', 'hendrix', age = 27)
# print(musician)



# def getformattedname_2(firstname, lastname):
#     fullname = firstname + ' ' + lastname
#     return fullname.title()

# while True:
#     print('\nTell me your name :')
#     print("(enter 'q' at any time to quit)")
#     f_name = input('first name: ')
#     if f_name == 'q':
#         break
#     l_name = input('last name: ')
#     if l_name =='q':
#         break


#     formattedname = getformattedname_2(f_name, l_name)
#     print('\nHello, ' + formattedname + '!')




###   Passing a List

# def greetusers(names):
#     for name in names:
#         msg = 'Hello ' + name.title() + '!'
#         print(msg)
# usernames = ['hannah', 'ty', 'margot']
# greetusers(usernames)



# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print('Printing model: ' + current_design)
#     completed_models.append(current_design)
# print('\nThe following models have been printed:\n ')
# for completed_model in completed_models:
#     print(completed_model)



# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print('Printing model: ' + current_design)
#         completed_models.append(current_design)
    
# def show_completed_models(completed_models):
#     print('\nThe following models have been printed: ')
#     for completed_model in completed_models:
#         print(completed_model)

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)



# function_name(list_name[:]) --- send a copy of the list to the function
# print_models(unprinted_designs[:], completed_models) --- can be done




### Passing an Arbitrary Number of Arguments

# def make_pizza(*toppings):      # * toppings --- python makes an empty tuple called toppings and pack whatever value it receives into this tuple
#     print('\nMaking a pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')



# def make_pizza_1(size, *toppings):
#     print('\nMaking a ' + str(size) + 
#           '-inch pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)

# make_pizza_1(16, 'pepperoni')
# make_pizza_1(12, 'mushrooms', 'green peppers', 'extra cheese')



# def build_profile(first, last, **user_info):        # **user_info --- python makes an empty dictionary called user_info and pack whatever name-value pairs it receives into the dictionary
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# user_profile = build_profile('albert', 'einstein',
#                              location = 'princeton',
#                              field = 'physics')
# print(user_profile)




### Storing Your Functions in Modules

# def make_pizza(size, *toppings):
#     print('\nMaking a ' + str(size) + 
#           '-inch pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)

# import ?
        


# module_name.function_name()



# from module_name import function_name
# from module_name import function_0, function_1, function_2


# You're gonna need to define these in another file(s) in the same directory
# from pizza import make_pizza as mp
# from module_name import function_name as fn
# import pizza as p
# import module_name as mn
# from pizza import *
# from module_name import *




### Styling Functions

# def function_name(parameter_0, parameter_1 = 'default value')
# function_0(value_0, parameter_1 = 'value')






# import random

# a = []
# for i in range(0, 10):
#     a.append(random.randint(10,100))

# print(a)