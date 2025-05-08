squares = [ x**2 for x in range(1,6)]
print(squares)
# List comprehensions are a concise way to create lists using a single line of code.

list = [1,4,6,8,7,3,77,66]
even = [x for x in list if  x%2==0 ]
print(even)

# without list comprhensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Original list

evens = []  # Empty list to store even numbers

for x in nums:
    if x % 2 == 0:       # Check if the number is even
        evens.append(x)  # Add even number to the list

print("Even numbers:", evens)
