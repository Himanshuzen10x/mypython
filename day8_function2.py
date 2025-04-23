def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York