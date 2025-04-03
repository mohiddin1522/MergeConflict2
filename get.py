# def get():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     address = input("Enter your address: ")
#     return name, age, address

# li = list(get())
# print(li)

# def display(li):
#     print("Name:", li[0])
#     print("Age:", li[1])
#     print("Address:", li[2])
# display(li)

def greet(name="Guest"):
    print("Hello", name)
greet()
greet("chotu")

def addall(*numbers):
    return sum(numbers)

print(addall(1, 2, 3, 4, 5))

print(sum({2,3}))

def info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

info(name="John", age=30, city="New York")