# loops
for i in range(1,6):
    print(i)
    
    
# 👇 String ke characters pe loop
for ch in "Python":
    print(ch)

# 👇 List ke items pe loop
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

count = 1
while count <= 5:
    print(count)
    count += 1

# ✅ while loop tab chalta hai jab tak condition True ho

for i in range(1,7):
    if i == 3: 
        break
    print(i)
    
    
for i in range(1, 6):
    if i == 3:
        continue  #skip kar deya 3 ko print karna
    print(i)