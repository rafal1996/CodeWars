# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = weight/pow(height, 2)
    if bmi <= 18.5:
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overweight"
    if bmi > 30:
        return "Obese"

print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(90, 1.80))
print(bmi(110, 1.80))
print(bmi(50, 1.50))
