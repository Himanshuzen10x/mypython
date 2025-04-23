file = open ("demo.txt", 'a',)
file.write("\nyou are awesom")
file.close()

# file = open ("demo.txt", 'r',)

# print(file.read())
with open("demo.txt", "r") as f:
    # f.seek(5)        # Move pointer to index 5
    print(f.read())  # Read from there
