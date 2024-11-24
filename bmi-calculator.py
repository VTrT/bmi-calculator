weight = float(input("Your weight in kilograms (kg): "))
height = float(
            input("Your height in meters (m): ").replace(",",".")
        )

bmi = round(weight / (height ** 2), 2)

print(f"\nYour BMI: {bmi}")
if bmi < 18.5:
    print("Underweight")

if 18.5 <= bmi < 24.9:
    print("Normal weight")

if 25 <= bmi < 29.9:
    print("Overweight")

if bmi >= 29.9:
    print("Obesity")