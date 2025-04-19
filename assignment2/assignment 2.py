#task 1
'''
Check if a Number is Even or Odd
'''

a=int(input("enter a number"))
b=a%2
if b==0:
    print(a ,"is an even number")
else:
    print(a ,"is an odd number")

#task 2
'''
Sum of Integers from 1 to 50 Using a Loop

'''
a=int(0)
for i in range(1,51):
    a=a+i
print(a)