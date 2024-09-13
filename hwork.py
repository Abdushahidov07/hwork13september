# Task 1
# class Person:
#     def __init__(self, name):
#         self.name=name
#     def hi_hello(self):
#         print(f"Hello, my name is {self.name}")
# per1=Person(input())
# per1.hi_hello()

# Task 2
# class Ploshad:
#     def __init__(self, a, b):
#         self.a=a
#         self.b=b
#     def ploshadkvadrata(self):
#         print(f"Площадь квадрата {self.a*self.b}")
# kvadrat = Ploshad(int(input()),int(input()))
# kvadrat.ploshadkvadrata()

# Task 3
# class ploshadfigur:
#     def __init__(self, r):
#         self.r=r
#         pass
#     def kryg(self):
#         print(f"Площадь круга: {3.14*(self.r**2) }")
# figyri =  ploshadfigur(int(input("r = ")))
# figyri.kryg()

# Task 4

# class Car:
#     total_car=0
#     def __init__(self):
#         Car.total_car+=1
#     @classmethod
#     def totalcar(cls):
#         return cls.total_car
# car1=Car()
# print(Car.totalcar())
