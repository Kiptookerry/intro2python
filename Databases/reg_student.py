from database import student

try:
    name = input("Enter Name\n")
    phone = input("Enter Phonenumber\n")
    age = input("Enter Age\n")
    gender = input("Enter gender\n")
    studentcode = input("Enter studentcode\n")


    print("Student Created Successfully")

except:
    print("Failed to create user")