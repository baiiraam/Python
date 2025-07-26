### python'a giris

# OS module

# import os

# print(os.getcwd())

# os.chdir('C:/Users/Bayram/Desktop/python_learning/beginning_of_the_end')

# print(os.getcwd())

# print(os.listdir())

# print(os.listdir('C:\Program Files\Google\Drive'))

# for file in os.listdir():
#     print(file)

# print(os.listdir('C:/Users/Bayram/Desktop/python_learning/beginning_of_the_end'))

# os.mkdir('Mayday_Mayday')

# print(os.listdir())

# mkdir creates a file , makedirs creates file within a file within a file... , rmdir removes a file

# os.makedirs('mayday1/mayday2/mayday3')

# os.rmdir('Mayday Mayday')

# os.removedirs('mayday1/mayday2/mayday3')

# os.chdir('C:/Users/Bayram/Mayday_Mayday')

# print(os.getcwd())
# print(os.listdir())

# minutes 10-20

# os.removedirs('C:/Users/Bayram/Desktop/mirtafayl/fayl1/fayl2/fayl3')

# os.chdir('C:/Users/Bayram/Desktop/mirtafayl')

# os.getcwd()

# os.makedirs('fayl1/fayl2/fayl3')

# os.rmdir('C:/Users/Bayram/Desktop/mirtafayl/fayl1/fayl2')   DIRECTORY NOT EMPTY

# print(os.listdir())

# will_be_deleted = os.listdir()[0]
# print(will_be_deleted)

# os.remove('C:/Users/Bayram/Desktop/mirtafayl/fayl1')   # whyyy , hmmm

# print(os.listdir())

# os.remove(os.listdir()[2])

# os.rmdir('faylsinaq')



# os.rename('yenefaylsinaq', 'YENEFAYLSINAQ')
# os.rename('mirtatext1.txt', 'MIRTATEXT1.txt')
# os.rename('newexcel.xlsx', 'NEWEXCEL.xlsx')


# from datetime import datetime



# os.rename('NEWEXCEL.xlsx', 'C:/Users/Bayram/Desktop/mama zaevlenie/New_Excel.xlsx')
# os.chdir('C:/Users/Bayram/Desktop/mirtafayl')

# os.rename('Fayl1', 'fayl1')
# os.rename('YENEFAYLSINAQ', 'yenefaylsinaq')

# for gecerli_klasor, icindeki_klasorler, icindeki_dosyalar in os.walk('C:/Users/Bayram/Desktop/mirtafayl'):
#     print('gecerli klasor: ', gecerli_klasor)
#     print('icindeki klasorler: ', icindeki_klasorler)
#     print('icindeki dosyalar: ', icindeki_dosyalar)
#     print()


# print(os.path.join('fayl1', 'fayl2', '/fayl3'))       don't know what this does

# print(os.path.isfile('C:/Users/Bayram/Desktop/mirtafayl/text1.txt'))
# print(os.path.isfile('C:/Users/Bayram/Desktop/mirtafayl/fayl1'))
# print(os.path.isdir('C:/Users/Bayram/Desktop/mirtafayl/fayl1'))       also look at them bruh


# print(os.path.splitext('C:/Users/Bayram/Desktop/mirtafayl/text1.txt'))


# print(os.stat("yoxlamafayli").st_atime)
# zaman = datetime.fromtimestamp(os.stat('yoxlamafayli').st_atime)
# print(zaman)

# print(os.stat('yoxlamafayli').st_size)
# print(datetime.fromtimestamp(os.stat('yoxlamafayli').st_mtime))



# os.rename('bayram.docx', 'Bayram.docx')

# print(os.stat('baravida.rtf').st_atime)









### python'a giris, video 16



# import os

# def duzenle():
#     klasor = input('Duzenlenecek klasor: ')
#     dosyalar = []   # dosyalar depolanacak
#     uzantilar = []  # uzantilar depolanacak
#     def list_dir():
#         for dosya in os.listdir(klasor):
#             if os.path.isdir(os.path.join(klasor, dosya)):  # dosyamiz klasor mu?
#                 continue
#             if dosya.startswith('.'):   # dosyamiz gizli dosya mi?
#                 continue
#             else:
#                 dosyalar.append(dosya)
#     list_dir()
#     # uzantilari alma
#     for dosya in dosyalar:
#         uzanti = dosya.split('.')[-1]
#         if uzanti in uzantilar:     # uzanti daha once eklendi mi?
#             continue
#         else:
#             uzantilar.append(uzanti)
#     for uzanti in uzantilar:        # klasorler olusturuluyor
#         if os.path.isdir(os.path.join(klasor, uzanti)):
#             continue
#         else:
#             os.mkdir(os.path.join(klasor, uzanti))
#     for dosya in dosyalar:
#         uzanti = dosya.split('.')[-1]
#         os.rename(os.path.join(klasor, dosya), os.path.join(klasor, uzanti, dosya))

# if __name__ == '__main__':
#     duzenle()



# import math
# print(math.sqrt(64))

# from math import sqrt
# print(sqrt(64))






### tarihlere gore dosyalari ayirma

# import os
# from datetime import datetime

# def duzenle():
#     klasor = input('Duzenlenecek klasor: ')
#     dosyalar = []   # dosyalar depolanacak
#     tarihler = []  # tarihler depolanacak
#     def list_dir():
#         for dosya in os.listdir(klasor):
#             if os.path.isdir(os.path.join(klasor, dosya)):  # dosyamiz klasor mu?
#                 continue
#             if dosya.startswith('.'):   # dosyamiz gizli dosya mi?
#                 continue
#             else:
#                 dosyalar.append(dosya)
#     list_dir()
#     # tarihleri alma
#     for dosya in dosyalar:
#         tarih_damgasi = os.stat(os.path.join(klasor, dosya)).st_mtime
#         tarih = datetime.fromtimestamp(tarih_damgasi).strftime('%d-%m-%Y')
#         if tarih in tarihler:
#             continue
#         else:
#             tarihler.append(tarih)

#     for tarih in tarihler:        # klasorler olusturuluyor
#         if os.path.isdir(os.path.join(klasor, tarih)):
#             continue
#         else:
#             os.mkdir(os.path.join(klasor, tarih))
#     for dosya in dosyalar:
#         tarih_damgasi = os.stat(os.path.join(klasor, dosya)).st_mtime
#         tarih = datetime.fromtimestamp(tarih_damgasi).strftime('%d-%m-%Y')

#         os.rename(os.path.join(klasor, dosya), os.path.join(klasor, tarih, dosya))

# if __name__ == '__main__':
#     duzenle()





# import os
# os.rename('C:/Users/Bayram/Desktop/modules in python.py', 'Modules in Python.py')




# with open('C:/Users/Bayram/Desktop/try-except blocks.py', 'w') as t:
#     t.write('salam')