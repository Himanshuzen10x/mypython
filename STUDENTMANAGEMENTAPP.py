print('Welcome to Student Management System')

Students = []

while True:
    try:
        name = input("Enter name: ").capitalize()
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
        student = {'name': name, 'age': age, 'marks': marks}
        Students.append(student)
    except Exception as e:
        print("Error occurred:", e)
    choice = input("Add another student? (yes/no): ").lower()
    if choice != "yes":
        break
print("\nAll Students")
print(student)

avg = sum(s["marks"] for s in Students)/len(Students)
print(f'Average Mark:  {avg}')

names  = sorted([s["name"] for s in Students])
print("sorted Names : ", names)

with open("students.txt", 'w') as f:
    for s in Students:
        f.write(f"{s['name']}, {s['age']}, {s['marks']}")
        # f.write(f"{s['name']}, {s['age']}, {s['marks']}\n")