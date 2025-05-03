students = [("Himanshu", 85), ("Khare", 92), ("Aman", 78)]
students.sort(key=lambda x: x[1])  # Sort by marks
print(students)


product = products = [("Laptop", 55000), ("Mouse", 500), ("Keyboard", 1200), ("Monitor", 15000)]
product.sort(key=lambda x: x[1], reverse=True)
# reverse=True
print(product)

employees = [("Raj", 3), ("Sneha", 5), ("Amit", 2), ("Neha", 4)]
employees.sort(key=lambda x: x[1])
print(employees)