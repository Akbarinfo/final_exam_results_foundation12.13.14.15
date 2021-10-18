# [1-13, 15-29] Javoblar: Abdug'ani Toshmuhammedov dan ko'chirildi
# [14]          Javob:    Ravshan Rohmanberdiyev dan ko'chirildi
# [30]          Javob:    Nosirbek Hakimov dan ko'chirildi


# from json import dumps, loads


# 1 - masala
# def check(sentence_1: str, sentence_2: str) -> bool:
#     """2-string 1-string ichida bor/yo'qligini tekshiruvchi function"""
#     return True if sentence_2 in sentence_1 else False
#
#
# str1 = input("1 - string >> ")             # "I hate exams"
# str2 = input("2 - string >> ")             # "ex"
# print(f"Output: {check(str1, str2)}")      # Output: True


# 2 - masala
# info = input("Example: alibek 24 oshpaz\n>> ").split()      # -> ["alibek", "24", "oshpaz"]
# if info[1].isnumeric():
#     file = open("info.txt", "a")
#     file.write(f"ismi={info[0]}\nyoshi={info[1]}\nkasbi={info[2]}\n")
# else:
#     print("Invalid input")


# 3 - masala
# def check_word(file_name: str, word: str) -> bool:
#     """Biror faylda kiritilgan so'z bor/yo'qligini tekshiruvchi function"""
#     file = open(file_name)
#     text = file.read()
#     file.close()
#     return True if word in text else False
#
#
# print(f"Output: {check_word('text.txt', 'good')}")   # Output: True


# 4 - masala
# Papka ichiga kirish                                -> cd <folder_name>
# Papkadan chiqish                                   -> cd ../
# Barcha papkalardan chiqish va root path'ga qaytish -> cd
# Ichi bo'sh papkani o'chirish                       -> rmdir <folder_name>
# Ichida nimadir bor papkani o'chirish               -> rm -r <folder_name>
# Fayl'ni o'chirib yuborish                          -> rm <file_name>
# Barcha fayl'larni o'chirib yuborish                -> rm *


# 5 - masala
# Inheritance - bu biror class'dan vorislik olish
#       Example:
#               class Parent():
#                   pass
#
#               class Child(Parent):
#                   pass


# 6 - masala
# Encapsulations - bu class ichidagi ba'zi o'zgaruvchilarni yashirish: Private -> self.__budget
#       Example:                                                       Protected -> self._budget
#                 class Test():                                        Public -> self.budget
#                     def __init__(self):
#                         self.__budget = None


# 7 - masala
# Polymorphism - bu turli class'larda bir xil method'larga ega bo'lishi.
#       Example:
#                 class Parent():
#                     def shoot(self):
#                         print("Hello")
#
#                 class Child(Parent):
#                     def shoot(self):
#                         print("World")
#
#                 parent = Parent()
#                 parent.shoot()        -> Output: Hello
#                 child = Child()
#                 child.shoot()         -> Output: World


# 8 - masala
# Abstraction - bu voris olingan class'dagi ba'zi method'larni majburiy qilib qo'yish.
# Majburiy qilib qo'yilgan methodlar abstractmethod deb ataladi.
# Uni qo'llash uchun parent class'ga ABC class'dan voris olish kerak.
#        Example:
#                 from abc import ABC, abstractmethod
#                 class Shoot(ABC):
#                     @abstractmethod
#                     def dang(self):
#                         pass
#
#                 class test(Shoot):
#                     def dang(self):
#                         pass


# 9 - masala
# Function va Method orasidagi farq:
# functions'lar class'lardan tashqarida,
# method'lar esa class'lar ichida va class'ning bir qismi sifatida belgilanadi.
#       Example:
#               class dang():
#                   def shoot(self):    -> bu method
#                       pass
#
#                 def nothing():          -> bu esa function
#                     pass


# 10 - masala
# Variable va property orasidagi farq:
# Variable - bu oddiy o'zgaruvchi
# Property - esa class'ga tegishli bo'lgan o'zgaruvchi


# 11 - masala
# class Mavjudodlar():
#     def __init__(self, nomi: str, mavjud=True) -> None:
#         self.mavjud = mavjud
#         self.nomi = nomi
#
#
# class Sut_emizuvchilar(Mavjudodlar):
#     def __init__(self, nomi, oyoqlari_soni: int, shoxi: bool) -> None:
#         self.oyoqlari_soni = oyoqlari_soni
#         self.shoxi = shoxi
#         super().__init__(nomi)
#
#     def tovush_chiqarish(self):
#         pass
#
#     def yugurish(self):
#         pass
#
#
# class Baliqlar(Mavjudodlar):
#     def __init__(self, nomi, ogirligi: float, tangachali: bool) -> None:
#         self.ogirligi = ogirligi
#         self.tangachali = tangachali
#         super().__init__(nomi)
#
#     def suzish(self):
#         pass
#
#     def nafas_olish(self):
#         pass
#
#
# class Qushlar(Mavjudodlar):
#     def __init__(self, nomi, ovqati: str, ucha_oladi=True) -> None:
#         self.ucha_oladi = ucha_oladi
#         self.ovqati = ovqati
#         super().__init__(nomi)
#
#     def uchish(self):
#         pass
#
#     def qonish(self):
#         pass
#
#
# kenguru = Sut_emizuvchilar("Kenguru", 2, False)
# quyon = Sut_emizuvchilar("Quyon", 2, False)
#
# farel = Baliqlar("Farel", 4.4, True)
# som = Baliqlar("Som", 5.5, True)
#
# burgut = Qushlar("Burgut", "Go'sht")
# chumchuq = Qushlar("Chumchuq", "Bilmiman")


# 13 - masala
# Static method - Statik usul - bu class'ning ob'ekti emas, balki class'ga bog'liq bo'lgan method.
#       Example:
#               class Hello():
#               @staticmethod
#               def gun():
#                   print(True)


# 14 - masala : super () methodi - Neshtadur ota class bo`lsa ,
# agar bittasini ichida boshqasi nechi marttadur initlar chaqirilgan bo`lsa
# shuni 1 martta chaqiradi


# 15 - masala
# Public property - bu class ichida ham, classdan olingan obyekt orqali ham,
# voris olingan classda ham ishlatilishi mumkin bo'lgan o'zgaruvchi
# Example: self.budget = 100


# 16 - masala
# Private property - bu faqatgina o'ziga tegishli bo'lgan class'da ishlatish mumkin bo'lgan o'zgaruvchi
# Example: self.__budget = 100


# 17 - masala
# Protected property - bu o'ziga tegishli classda va voris olingan classda ishlatsa bo'ladigan o'zgaruvchi
# Example: self._budget = 100


# 18 - masala
# class Odam():
#     def __init__(self, ism: str) -> None:
#         self.ism = ism
#
#     def baqirish(self) -> None:
#         print("A-a-a-a-a")
#
#
# class Kuchuk():
#     def __init__(self, laqab: str) -> None:
#         self.laqab = laqab
#
#     def tishlash(self, odam_object) -> None:
#         print("Tishlandi")
#         odam_object.baqirish()
#
#
# odam = Odam("Ali")
# kuchuk = Kuchuk("Bobik")    # Output: Tishlandi
# kuchuk.tishlash(odam)       #         A-a-a-a-a


# 19 - masala
# class Player():
#     def __init__(self, qurol: str, jon=100):
#         self.__jon = jon
#         self.qurol = qurol
#
#     def otish(self, player_object, soni=1):
#         player_object.reduce_life(soni)
#
#     def reduce_life(self, soni):
#         self.__jon -= soni * 10
#
#     def show_health(self) -> None:
#         print(f"\nQurol: {self.qurol}\tJon: {self.__jon}")
#
#
# counter = Player("akm")
# terror = Player("m416")
# counter.otish(terror, 2)
# terror.otish(counter)
# terror.show_health()
# counter.show_health()


# 20 - masala
# USE <database_name>;

# Example:
# USE mini_project;


# 21 - masala
# CREATE TABLE <table_name> (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL, job VARCHAR(30) NOT NULL);

# Example:
# CREATE TABLE users (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL, job VARCHAR(30) NOT NULL);


# 22 - masala
# INSERT INTO <table_name> (name, job) VALUES (<value_1>, <value_2>);

# Example:
# INSERT INTO users (name, job) VALUES ("John", "Doctor");


# 23 - masala
# DELETE FROM <table_name> [WHERE <condition>];
# Example:
# DELETE FROM users WHERE name="John";


# 24 - masala
# UPDATE <table_name> SET <clumn_name1> = <value> WHERE <condition>;

# Example
# UPDATE users SET job = "Architect" WHERE name="John";


# 25 - masala
# DROP TABLE <table_name>;

# Example:
# DROP TABLE user;


# 26 - masala
# DROP DATABASE <database_name>;

# Example:
# DROP DATABASE mini_project;


# 27 - masala
# SELECT login, age FROM <table_name> WHERE age<30


# 28 - masala
# SELECT * FROM <table_name> WHERE age=(SELECT MAX(age) FROM <table_name>)


# 29 - masala
# ALTER TABLE <table_name> ADD job VARCHAR(20) AFTER name;


# 30 - masala: -> Credit for Nosirbek Hakimov
# b = input("Enter :")
# if b.isnumeric():
#     b = int(b)
#     for i in range(1, 2*b):
#         for j in range(1, 2*b):
#             if abs(b-j)+1 >= abs(b-i)+1:
#                 print(abs(b-j)+1, end=' ')
#             else:
#                 print(abs(b-i)+1, end=' ')
#         print()