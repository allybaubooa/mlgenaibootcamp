# import datetime
# class Student:
#     # self is not counted as parameter
#     def __init__(self, first_name,last_name, address, year_of_birth=2000): # first function to run when creating a student
#         self.first_name = first_name # attributes
#         self.last_name = last_name
#         self.address = address
#         self.full_name = f"{self.first_name} {self.last_name}"
#         self.year_of_birth = year_of_birth
#         self.age = datetime.date.today().year - self.year_of_birth
    
# student_1 = Student("Abraham","Smith","Floreal", 2010) # 2
# print(f"{student_1.full_name} aged {student_1.age} lives at {student_1.address}")

# student_2 = Student("Anjelina","Jolie","Curepipe", 2023)
# print(f"{student_2.full_name} aged {student_2.age} lives at {student_2.address}")

# student_3 = Student("Ally","Baubooa","Goodlands", 1998)
# print(f"{student_3.full_name} aged {student_3.age} lives at {student_3.address}")

# class Car:
#     def __init__(self,make,model,color): # constructor: runs everytime we create a car
#         self.make = make
#         self.model = model
#         self.color = color
#         self.fuel_level = 50
#         self.engine_status = "OFF"
#         self.speed = 0

# nayar_car = Car("VW","Polo","grey")
# abraham_car = Car("BMW","316","red")

# print(f"{nayar_car.make} {nayar_car.model} is driving at {nayar_car.speed} km/h")
# print(f"{abraham_car.make} {abraham_car.model} is driving at {abraham_car.speed} km/h")

# class BankAccount: # by convention, class names are Capital
#     # constructor method
#     def __init__(self, customer,acc_number):
#         self.balance = 0
#         self.customer = customer
#         self.acc_number = acc_number # normally autogerated. 

#     def deposit(self,amount):
#         self.balance = self.balance + amount

#     def withdraw(self,amount):
#         if(self.balance >=  amount):
#             self.balance = self.balance - amount
#         else:
#             print("Insufficient Balance")

#     def show_balance(self):
#         print(f"You currently have Rs {self.balance}")

# nayar_acc = BankAccount("Nayar Joolfoo","00001")
# nayar_acc.show_balance()
# # nayar deposits Rs 2000
# nayar_acc.deposit(2000)
# nayar_acc.deposit(1000)
# nayar_acc.show_balance()
# nayar_acc.withdraw(500)
# nayar_acc.show_balance()
# nayar_acc.withdraw(6000)
# nayar_acc.show_balance()

class Car:
    def __init__(self,colour="white"):
        self.mileage = 0
        self.colour = colour
        print(f"Creating a {colour} car with mileage {self.mileage} km")
    
    def crash(self, othercar):
        print(f"{self.colour} car has crashed with {othercar.colour} car")

class PoliceCar(Car):
    def __init__(self, colour="blue"):
        super().__init__(colour)

# we want police cars to be blue by default
zaynahcar = Car()
policecar1 = PoliceCar()
policecar2 = PoliceCar()