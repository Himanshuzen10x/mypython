nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]
# Applies a function to each item in an iterable (like list).


nums = [1, 2, 3, 4, 5, 6]
# Filters items for which the function returns True.
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]
