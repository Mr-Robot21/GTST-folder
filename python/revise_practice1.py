# Introduction to Python Exercises
'''
gtst = "Day 7"
print (f"Hello Today is our {gtst} course")

even = [0 , 2 , 4]
print("The first Even number is :" , even[0])
print(f"The second Even number is : {even[1]}")
print("The third Even number is :" , even[2])

fruits = {"apple" : 10, "banana" : 15, "pineapple" : 20}
choice = "apple"
print(f"The value of {choice} is : {fruits["apple"]}")
'''

# Core to Python Exercises
# Exercise 1
'''
users = ['Nathan',2313,'Geez','pass231','Abebe','092313133','Miki',"pl3s34D0n'tH4ckM3"]
print (f"The usernames are : {users[::2]}")
print (f"The passwords are : {users[1::2]}")

users = {'Nathan' : 2313,'Geez' : 'pass231','Abebe' : '092313133','Miki' : "pl3s34D0n'tH4ckM3"}
user = input("Enter your Username : ")
print (f"{user} your password is {users[user]}")

# Exercise 2
number = (input("Enter your number : "))
if number == "" :
    print ("Nothing inserted")
else :
    is_number = True
    for char in number :
        if char < '0' or char > '9'  :
            is_number = False
            break

    if is_number :
        number = int(number)
        if number % 2 == 0 :
            print ("The number is Even")
        else :
            print ("The number is Odd")
    else :
        print ("Please enter a number only")
'''

# further on Python
# Exercise 1
'''
def joel(x, y) :
    z = 2024 - y
    print(f"Your name is {x} and your age is {y}", f"while you are born in {z}")

name = input("Enter your name : ")
age = int(input("Enter your age : "))

joel(name,age)

def add(x, y) :
    return x + y

def sub(x,y) :
    return x - y

def multi(x,y) :
    return x * y 

def div(x,y) :
    return x / y

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("The sum of the two numbers is : " , add(num1,num2))
print("The difference of the two numbers is : " , sub(num1,num2))
print("The product of the two numbers is : " , multi(num1,num2))
print("The quotient of the two numbers is : " , div(num1,num2))
'''
'''
nums = [3,2,6,8,4,6,2,91]

evens = list(filter(lambda n:n % 2 == 0, nums))
doubles = list(map(lambda n : n *2 , evens))
print (evens)
print (doubles)
'''
'''
# Exercise 2
lists = []
print("Enter your numbers")
for i in range(10) :
    nums = int(input())
    lists.append(nums)
print(lists) 
evens = list(filter(lambda n : n % 2 == 0 , lists))
adds = list(map(lambda n : n + 15 , evens))
print (evens)
print (adds)
''' 
# Exercise 3
'''
class Human :
    name = ""
    age = ""
    grade = ""

    def run(self) :
        return "I can Run!"

    def dance(self) :
        return "I can dance"
    
    def eat(self) :
        return "I can eat"
    
human1 = Human()
human1.name = "Joel Mengstab"
human1.age = 25
human1.grade = "4"
print (f"My name is {human1.name}\n I am {human1.age} years old. \n I am grade {human1.grade} student")
print (f"My skills are : {Human.run(human1)} , {Human.dance(human1)} and {Human.eat(human1)}. \n Thank you.")
'''
'''
# Exercise 4
class Human :
    def __init__(self,name,age,grade) :
        self.name = name
        self.age = age
        self.grade = grade

    def run(self) :
        return "I can Run!" 

    def dance(self) :
        return "I can dance"
    
    def eat(self) :
        return "I can eat"
    
human1 = Human("Joel Mengstab" , 25 , 4)
print (f"My name is {human1.name}\n I am {human1.age} years old. \n I am grade {human1.grade} student")
print (f"My skills are : {human1.run()} , {human1.dance()} and {human1.eat()}. \n Thank you.")
'''

# Exam Question
'''
old_list = []

print("Enter you numbers : ")

for i in range(6) :
    num = int(input(f"Enter number {i + 1} : "))
    old_list.append(num)
print(old_list)

def evens(x) :
    return x % 2 == 0

def add5(x) :
    return x + 5

new_list1 = list(filter(evens , old_list))
new_list2 = list(map(add5 , new_list1))
print(new_list1)
print(new_list2)
'''