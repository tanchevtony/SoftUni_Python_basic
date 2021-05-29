name_one = input("What is your name?\n")
height_one = float(input("What is your height in m?\n"))
weight_one = float(input("What is your weight in kg?\n"))


def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)
    print("bmi: ")
    print(f"{bmi:.2f}")
    if bmi <= 18.5:
        return name + " you are underweight"
    elif 18.5 < bmi <= 25:
        return name + " you are normal weight"
    elif 25 < bmi < 29.9:
        return name + " you are obesity"

result = bmi_calculator(name_one, height_one, weight_one)
print(result)