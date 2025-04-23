s= {1,3,5,7,8,9,2}
s.add(80)
s.update([70,90])
s.remove(70)
s.discard(100)

r= {2,55,70,80,40,7}
print("*********")
print(s|r)#union
print(s&r) #intersection

print(s - r)   
print(s ^ r)   

print('***********')
print(s)
for iteam in s:
    print (iteam)
    # outube kabhi kabhi sort karke bhi de sakta hai
    
# Step 1: User se comma-separated numbers lo
# Step 2: Set banake unique values print karo

print("-------------------------------------------")
nums = input("Enter numbers separated by comma: ")
num_set = set(nums.split(","))
print("Unique values:", num_set)


