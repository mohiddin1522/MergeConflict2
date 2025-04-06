import inspect


def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator 
def greet():
    print("Hello, World!")

greet()

print(inspect.signature(decorator))
