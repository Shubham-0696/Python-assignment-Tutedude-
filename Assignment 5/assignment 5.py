#ASSIGNMENT 5:
#Module 6: Data Structures and Strings in Python

#Task 1: Create a Dictionary of Student Marks


student_marks={"shubham":"87","Alice":"67","nina":"97","mina":"85","rin":"81","rohit":"91"}
name=str(input("enter the name of the student:"))
low_name=name.lower()
print(low_name)
lower_key={}
for key, value in student_marks.items():
    lowkey=key.lower()
    lower_key={lowkey:value}
    print(lower_key)

if low_name in lower_key:
    mark = lower_key[low_name]
    print(f"{low_name} marks are:{mark}")

else:
    print("student not found")

#Task 2: Demonstrate List Slicing

list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
list2=list1[0:5]
print(list2)
rev=list(reversed(list2))
print(rev)