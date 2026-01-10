def say_hi():
    print("hi!")  

def area(radius):
    return 3.14 * radius * radius

def volume(radius, height):
    return area(radius) * height   # area function recall

def greet(name="no name"):
    print(f"hello, {name}!")

def get_info():
    name = "damla"
    age = 23
    return name, age

x = say_hi()  
print(type(x))  
print("\n")

n, a = get_info()
print(n, a)
print("\n")

greet()          
greet("damla")  
print("\n")

x = 10  # global

def test():
    x = 5   # local
    print("Inside:", x)

test()
print("Outside:", x)
print("\n")

def shout(msg):
    print(msg.upper())

def whisper(msg):
    print(msg.lower())

def speak(style, text):
    style(text)

speak(shout, "Hello!")   # HELLO!
speak(whisper, "Hello!") # hello!

print("\n")
name = "dino"
age = 55
print("hello " + name + " you are " + str(age) + " years old")
print("hello", name, "you are" , str(age) , "years old")
print(f"hello {name} you are {age} years old.")
greet(name)