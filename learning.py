# def salom(name):
#     print("salom", name);
#
# def square(numb):
# #     return numb * numb;
# val = input()
#
#
# def absolute(num: int) -> int:
#     if num < 0:
#         return -1 * num
#     else:
#         return num
#
# #     print(absolute(val)
# nums = [2, 3, 4, 53, 54]
# result = []
#
# for num in nums:
#     if num > 3:
#         result.append(num)
#
#
# # print(result)
# nums = [2, 3, 4, 53, 54]
# min(nums)
# print(min(nums))
class Adress:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country
    @property
    def full_adress(self):
       return f"{self.street} {self.city} {self.country}"
#
adress2 = Adress('fffff', 'ggggg', "hhhh")
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def format (date, country = None):
        if country == "USA":
            return f"{date.month}-{date.day}-{date.year}"
        return f"{date.day}-{date.month}-{date.year}"



    # def set_month(self, new_month):
    #    if new_month > 12 or new_month <= 0:
    #        raise ValueError("Ivalid month")
    #    self.month = new_month

#date = Date(12, 10, 2024)

