# ############single inheritance
# class father:
#     def house(self):
#         print("father has a house")
# class son(father): #inheritance
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.house()
# s.bike()

# ###########multi level inheritance
# class grandfather:
#     def house(self):
#         print("grandfather has a house")
# class father(grandfather):
#     def car(self):
#         print("father has a car")
# class son(father):
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.house()
# s.car()
# s.bike()

# # class thatta:
#     def land(self):
#         print("thatta's land")
# class appa(thatta):
#     def house(self):
#         print("appa's house")
# class maga(appa):
#     def bike(self):
#         print("maga's bike")
# obj=maga()
# obj.house()
# obj.land()
# obj.bike()

# # ####multiple inheritance
# class father:
#     def house(self):
#         print("father has a house")
# class mother:
#     def car(self):
#         print("mother has a car")
# class child(father,mother):
#     def bike(self):
#         print("child has a bike")
# obj=child()
# obj.house()
# obj.car()
# obj.bike()

#################hierarchical inheritance
class father:
    def house(self):
        print("father has a house")
class son(father):
    def bike(self):
        print("son has a bike")
class daughter(father):
    def doll(self):
        print("daughter has a doll")
obj1=son()
obj1.house()
obj1.bike()
obj2=daughter()
obj2.house()
obj2.doll()