#even odd program.
a=int(input("enter the number:"))
if (a%2==0):
    print(f"{a} is an even number")

else:
    print (f"{a} is an odd number")
    
print("*******************************************************************")
#Sum of Integers from 1 to 50 Using a Loop.
total= 0
for i in range(1,51):
    total+=i
print("the sum of integer from 1 to 50 is",total)
