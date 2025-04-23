
#ASSIGNMENT 4:
#Module 5: Files, Exceptions, and Errors in Python


#Task 1: Read a File and Handle Errors


try:
    with open("sample.txt", 'r') as file:
        for num, line in enumerate(file, 1):
            line = line.strip()
            print(f"line {num}: {line}")

except FileNotFoundError:
    print("ERROR:The file " 'sample.txt' " not found. ")




#Task 2: Write and Append Data to a File



file_name="sample.txt"
with open("sample.txt", "w" ) as file:
    first_entry=input("Enter text to write to the file: ")
    file.write(first_entry +"\n")
    print("Data successfully written to " ,file_name, ".")

with open("sample.txt", "a") as file:
    next_line=input("Enter additional text to append:")
    file.write(next_line)
    print("Data successfully appended.")

with open("sample.txt" , "r") as file  :
    print("Final content of ", file_name,":")
    r = file.read()
    print(r)


