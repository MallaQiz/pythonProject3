import math

# surname = input("yormatova")
# title = input("bugun kod yozishni urgandim")
# title.title()
# age = 23
# if age < 18:
#  print("voyaga yetmagan")
# else:
# print("voyaga yetgan")
# name = input("ismingizni yozing")
# name = Gulirano
# if name = gulirano:
#  print("salom guli")
# if 34 in nums:
#   print("ha")
# else:
#   print("yoq")

# yearNumber = int(input("Yil kiriting: "))
#
# muchalRaqami = int(yearNumber + 9) % 12

# print("Bu muchal raqami: " + str(muchalRaqami))


# muchalNomi = ["Sichqon", "Sigir", "Yo'lbars", "Quyon", "Baliq", "Ilon", "Ot", "Qo'y", "Maymun", "Tovuq", "It", "To'ng'iz",]

# print(muchalNomi[muchalRaqami - 1])

#
# muchalNomi = {
#    '1': "Sichqon",
#    '2': "Sigir",
#    '3': "Yo\'lbars",
#    '4': "Quyon",
#    '5': "Baliq",
#    '6': "Ilon",
#    '7': "Ot",
#    '8': "Qo\'y",
#    '9': "Maymun",
#    '10': "Tovuq",
#    '11': "It",
#    '12': "To'ngiz",
# }
#
#
# print(muchalNomi.get(str(muchalRaqami)))

#
# year = int(input("yilni kiriting"))
# if year % 4 == 0:
#    print("leap year")
# else:
# #    print("not leap year")
# while input("rozimisiz") == "yo'q":
# #    print("rozi emas")
# i = 0
# while i < 29:
#    print(i)
# #    i += 3
# S = int(input("Yuza = "))
# h = int(input("Balandlik = "))
# a = S*2/h
# print("Asos =", a)
# #p = int(input("p = "))
# p = math.pi
# r = int(input("radius= " ) )
# S = p * r * r
# # print("Yuza= ", S)
# nums = [2, 5, 7, 8, ]
# for num in nums:
# #    print(num)
# for char in "Umidim":
# #    print(char)
# students = ["Guli", "Madina", "Munisa"]
# for student in students:
#    print(student)
# for i, student in enumerate(students):
#    print (student, i)
#
# for student in reversed(students):
#       print(student)
#
# for student in sorted(students):
#    print (student)
#
# for i in range(1, 13):
# #    print (i)
# nums = list(range(200))
# print(nums [20:30])


nums = int(input("sonni kiriting:"))

if nums % 3 == 0 and nums % 5 == 0:
    print("fizbuz")
elif nums % 5 == 0:
    print("fiz")
elif nums % 3 == 0:
    print("buz")
else:
    print(nums)
