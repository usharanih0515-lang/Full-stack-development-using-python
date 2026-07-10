# ############class object########
# class student:#class name
#     name="usha" #attributes
#     def study(self):#represent current object
#         print("usha is studying")
# s1=student() #s1 is object
# print(s1.name) #accessing attributes
# s1.study()#study 


# class student:
#     def details(self):
#         print("had breakfast")
# s1=student()
# s1.details()
    
# student.details(s1)

##########constructor is a special method which is automatically called when an object of class is created

# class student:
#     def __init__(self,name,age): #initial is a constructor,self represents the current object
#         self.name=name
#         self.age=age
# s1=student("usha",20)
# s2=student("vyshu",21)
# s3=student("hemanth",22)
# print(s1.name,s2.name,s3.name)
# print(s1.age,s2.age,s3.age)

# class bank: ### ther eare 2 methods balance and check_balance
#     def __init__(self,balance):
#         self.balance=balance
#     def check_balance(self):
#         print(self.balance)
# account1=bank(1000)
# account1.check_balance()

class user:
    def __init__(self,name):
        self.name=name
    def login(self):
        print(self.name,"is logged in")
u1=user("usha")
u2=user("vyshu")
u1.login()
u2.login()