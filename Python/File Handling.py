## FILE HANDLING

# ## dosya islemleri

# f = open('C:/Users/Bayram/Desktop/beginning of the end/subject.txt', 'r')        # subject.txt yerine dosyanin konumu da yazilabilirdi. Dosyayi aciyor, 'r' modu sadece okuma icin, 'w' modu yazmak icin, 'r+' modu hem okumaya hem yazmaya yarar, 'a', 'b' modlari da mevcut.
# icerik = f.read()                                  # dosyayi okuyor
# print(icerik)
# f.close()                                          # dosyayi kapatiyor. Dosyayla isin bittiyse, dosyayi kapat, aksi takdirde yer kapliyor.

# icerik2 = f.read()      # will give an error, because you cannot read a closed file

# with open('C:/Users/Bayram/Desktop/beginning of the end/subject.txt', 'r') as f:
#     icerik = f.read()
#     print(icerik)
# icerik2 = f.read()      # Will give an error. Because, '''with open''' method closes file automatically.

# with open('C:/Users/Bayram/Desktop/beginning of the end/subject.txt') as f:
#     icerik = f.read()
#     print(icerik)

# If you do not write anything, (such as 'r', or 'w',...) python will assume it as 'r' as default.

# with open('C:/Users/Bayram/Desktop/beginning of the end/subject.txt') as f:
#     okunacak_miktar = 10
#     icerik = f.read(okunacak_miktar)
#     while len(icerik) > 0:
#         print(icerik, end = '')
#         icerik = f.read(okunacak_miktar)
    
#     icerik = f.read(10)         # read till 10th character
#     print(icerik, end = '')
#     icerik = f.read(10)         # read till the next 10th character ()
#     print(icerik, end = '')
#     icerik = f.read(10)         # read till the next 10th character
#     print(icerik, end = '')



#     satir = f.readline()
#     print(satir,end='')
#     satir = f.readline()
#     print(satir, end = '')
#     satir = f.readline()
#     print(satir, end = '')
#     satir = f.readline()
#     print(satir,end='')
#     satir = f.readline()
#     print(satir, end = '')
#     satir = f.readline()
#     print(satir, end = '')
#     pozisyon = f.tell()     # tells which character you are in
#     print(pozisyon)
#     f.seek(0)               # goes to that character and sets it to that value 
#     satir = f.readline()
#     print(satir,end='')





#     icerik = f.readlines()
#     print(icerik)
#     for satir in icerik:
#         print(satir,end='')
#     for satir in f:
#         print(satir, end ='')


# for i in range(10):
#     print(i,end=' ')


# with open('C:/Users/Bayram/Desktop/beginning of the end/subject2.txt', 'w') as f:
#     f.write('Python\n')
#     f.write('Hello, who is there ?')
    
# with open('C:/Users/Bayram/Desktop/beginning of the end/subject.txt') as okunacak:
#     with open('C:/Users/Bayram/Desktop/beginning of the end/subject2.txt', 'w') as yazilacak:
#         for satir in okunacak:
#             yazilacak.write(satir)
#         icerik = okunacak.readlines()
#         for satir in icerik:
#             yazilacak.write(satir)


# with open('C:/Users/Bayram/Desktop/bootcamp    noooooo/### bootcamp starting.py', 'rb') as okunacak:        # rb can understood as reading in binary, wb - writing in binary. If information is not in text format, (can be a movie, photo, etc.), it can be used. rb and wb, b stands for binary.
#     with open('C:/Users/Bayram/Desktop/bootcamp    noooooo/python2.py', 'wb') as yazilacak:
#         okunacak_miktar = 1024
#         icerik = okunacak.read(okunacak_miktar)
#         while len(icerik) > 0:
#             yazilacak.write(icerik)
#             icerik = okunacak.read(okunacak_miktar)


# with open('C:/Users/Bayram/Desktop/bootcamp    noooooo/### bootcamp starting.py', 'rb') as okunacak:
#     with open('C:/Users/Bayram/Desktop/bootcamp    noooooo/python3.py', 'wb') as yazilacak:
#         for satir in okunacak:
#             yazilacak.write(satir)



# ## Lists of methods of data types. Kind of mini project

# list_methods = []
# for method in dir(list):
#     if method.startswith('__'):
#         continue
#     list_methods.append(method)

# # print(list_methods)     # all methods, even advanced (class) ones will be returned if The IF block in this code is not there.


# set_methods = []
# for method in dir(set):
#     if method.startswith('__'):
#         continue
#     set_methods.append(method)


# string_methods = []
# for method in dir(str):
#     if method.startswith('__'):
#         continue
#     string_methods.append(method)


# tuple_methods = []
# for method in dir(tuple):
#     if method.startswith('__'):
#         continue
#     tuple_methods.append(method)


# dict_methods = []
# for method in dir(dict):
#     if method.startswith('__'):
#         continue
#     dict_methods.append(method)


# basliklar = ['List Methods', 'Set Methods', 'String Methods', 'Tuple Methods', 'Dictionary Methods']
# classes = [list_methods, set_methods, string_methods, tuple_methods, dict_methods]


# max_len = 0
# for class_ in classes:
#     if len(class_) > max_len:
#         max_len = len(class_)

# with open('C:/Users/Bayram/Desktop/Methods.txt', 'w') as f:
#     for baslik in basliklar:
#         print(baslik, end = '')
#         print(' ' * (30 - len(baslik)), end = '')
#         f.write(baslik)
#         f.write(' ' * (30 - len(baslik)))



#     for i in range(max_len):
#         print()
#         f.write('\n')
#         for class_ in classes:
#             if i >= len(class_):
#                 print('-------', end = '')
#                 print(' ' * 23, end = '')
#                 f.write('-------')
#                 f.write(' ' * 23)
#             else:
#                 print(class_[i], end = '')
#                 print(' ' * (30 - len(class_[i])), end = '')
#                 f.write(class_[i])
#                 f.write(' ' * (30 - len(class_[i])))









# ## Python project. File Handling

# There is a list of students. Names, Surnames, results of 
# first and second exams, and final exams. Condition for
# passing is at least 70 on final, and 30% of exams + 40%
# of final is to be at least 70. Those who pass will be 
# represented in a text file as well as those who did not pass.


# with open('C:/Users/Bayram/Desktop/text_for_project.txt') as t:
#     with open('C:/Users/Bayram/Desktop/Passing_Students.txt', 'w') as p:
#         with open('C:/Users/Bayram/Desktop/Failed_Students.txt', 'w') as f:
#             content = t.readlines()
#             m = 0
#             for row in content:
#                 if m == 0:
#                     m += 1
#                     continue
#                 row = row.replace('\n', '')
#                 space_count = 0
#                 space_indexes = []
#                 index = 0
#                 for character in row:
#                     if character == ' ':
#                         space_count += 1
#                         space_indexes.append(index)
#                     index += 1
#                 name_surname = row[:space_indexes[0]]
#                 surname = name_surname.split('-')[-1]
#                 name = name_surname[:name_surname.index(surname) - 1].replace('-', ' ')
#                 notes = row.split(' ')[-1]
#                 notes = notes.split('/')
#                 first_exam = int(notes[0])
#                 second_exam = int(notes[1])
#                 final = int(notes[2])
#                 average = first_exam * 0.3 + second_exam * 0.3 + final * 0.4
#                 major = row[(space_indexes[0] + 1):space_indexes[-1]]
#                 if average >= 70 and final >= 70:
#                     p.write(name)
#                     p.write(' ' * (25 - len(name)))
#                     p.write(surname)
#                     p.write(' ' * (25 - len(surname)))
#                     p.write(major)
#                     p.write(' ' * (25 - len(major)))
#                     p.write(str(round(average, 1)))
#                     p.write(' ' * 21)
#                     p.write('Passed')
#                     p.write('\n')
#                 else:
#                     f.write(name)
#                     f.write(' ' * (25 - len(name)))
#                     f.write(surname)
#                     f.write(' ' * (25 - len(surname)))
#                     f.write(major)
#                     f.write(' ' * (25 - len(major)))
#                     f.write(str(round(average, 1)))
#                     f.write(' ' * 21)
#                     f.write('Failed')
#                     f.write('\n')