# TRY - EXCEPT BLOCKS

# a = 5
# b = 0
# c = a / b
# print(a)
# print(b)
# print(c)



# try:
#     a = 5
#     b = 8
#     c = a / b

# except:
#     print('There is an error')

# print(a, b, c,sep='-')



# try:
#     a = 5
#     b = 8
#     c = a / b
#     d = x

# except:
#     print('There is an error')
#     print('Problem should be fixed.')


# print(a, b, c,sep='-')




# try:
#     a = 5
#     b = 8
#     c = a / b
#     d = x

# except Exception:
#     print('There is an error')
#     print('Problem should be fixed.')




# What if there is more than one error ?

# try:
#     a = 5
#     b = 2
    # if b == 0:
    #     raise ZeroDivisionError
    # c = a / b
    # x = 4
    # d = x
    # name = 'Adam'
    # character = name[3]
    # list_ = [1,2,3]
    # m = list_[5]
    
    


# except ZeroDivisionError as e:
    # print('Denominator cannot be 0.')
    # print(e)
# except NameError as e:
    # print('Variable is not defined.')
    # print(e)
# except IndexError as e:
    # print('Indexes are out of range.')
    # print(e)
# except Exception as e:
    # print('Unknown problem.')
    # print(e)

# except Exception: should be last.
    
# else:
    # print('Else block is working.')
    # print(character)

# if there is no error, else block will be working.
    
# finally:
    # print('Finally block is working.')

# if there is an error, else block will not work, but finally block will be working.
# finally block always works.



# import os
# os.chdir('C:/Users/Bayram/Desktop')
# os.rename('try-except blocks.py', 'Try-Except Blocks.py')

# For future reference, pathlib is better than os. Tend to use it more.