def calculate_bmi():
    weight = float(input("Enter your weight"))
    height = float(input("Enter height"))

    BMI = weight / (height **2)
    print(f"your BMI is{BMI}")
calculate_bmi()
