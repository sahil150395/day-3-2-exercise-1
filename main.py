# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / (height ** 2))
bmiStatement = ""

if BMI < 18.5:
    bmiStatement = "you are underweight"
elif BMI < 25:
    bmiStatement = "you have a normal weight"
elif BMI < 30:
    bmiStatement = "you are slightly overweight"
else:
    bmiStatement = "you are clinically obese"

print(f"Your BMI is {BMI}, {bmiStatement}.")




