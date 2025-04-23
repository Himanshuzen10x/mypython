name = input("What is your good name, Sir: ")

# 👇 Step 1: Write to file
with open("demo2.txt", 'w') as f:
    f.write(f"Welcome, \n{name}")

# 👇 Step 2: Read from file using seek
with open("demo2.txt", "r") as f:
    f.seek(5)  # Move pointer to 5th character
    print(f.read())

with open("demo2.txt", "r") as f:
    print(f.tell())      # 👈 Position before reading
    content = f.read()
    print(f.tell())      # 👈 Position after reading

with open("demo2.txt", "r") as f:
    for line in f:
        print(line.strip())  # 👈 strip() removes newlines
