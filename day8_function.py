# 👇 Function definition
def greet():
    print("Hello, Himanshu!")

# 👇 Function call
greet()


def greet(name):
    print(f"Hello, {name}!")

greet("Himanshu")


def square(x):
    return x*x

result = square(7)
print(result)


def greet(name="Friend"):
    print(f"Hello, {name}!")

greet()            # Hello, Friend
greet("Himanshu")  # Hello, Himanshu


def add(a, b):
    return a + b

print(add(3, 7))


def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")

intro(age=21, name="Himanshu")
