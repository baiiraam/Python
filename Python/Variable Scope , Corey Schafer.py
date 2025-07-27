# Variable Scope , Corey Schafer

# x = 'global x'

# def outer():
    # x = 'outer x'

    # def inner():
        # nonlocal x
        # x = 'inner x'
#         print(x)

#     inner()
#     print(x)

# outer()
# print(x)





# import builtins

# print(dir(builtins))

# def my_min():
#     pass


# m = min([1,2,3,4,5])
# print(m)


# def test(z):
    # global x
    # y = 'local y'
    # x = 'local x'
    # print(y)
    # print(x)
    # print(z)

# test('local z')
# print(x)
# print(z)