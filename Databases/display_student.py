from database import student

students = student.select()
#use forloop to display
for user in students:
    print(user.name, user.phone, user.age, user.gender, user.studentcode)