start = int(input('write your starting Number: '))
end = int(input('write your ending Number: '))

even = 0
odd = 0
for i in range (start,end+1):
    if i%2 == 0:
        print(f'Number {i} : Even')
        even = even + 1
        
        
    else:
        print(f'Number {i} : Odd')
        odd = odd + 1
    

print(f"Number of evens are :{even}" )
print(f"Number of odds are :{odd}" )

