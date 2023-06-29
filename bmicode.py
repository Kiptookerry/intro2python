weight = float(input("Enter weight in kgs"))
height = float(input("Enter height in metres"))


result = weight / (height**2)
print("your bmi is", result)

if result <= 18:
    print("underweight")
elif result <= 29:
    print("normal weight")
elif result <= 34:
    print("overweight")
else:
    print("obese")

