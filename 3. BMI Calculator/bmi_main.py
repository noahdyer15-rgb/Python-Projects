height = input("Enter your height in Meters: ")
weight = input("Enter your weight in KG: ")

height_int = float(height)
weight_int = float(weight)

bmi = weight_int / (height_int * height_int)

print(round(bmi))