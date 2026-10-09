#Welcome Message
print("Welcome to the tip calculator!")
# User inputs total bill cost
bill = float(input("What was the total bill? $"))
# Users inputs tip percentage
tip = int(input("What percentage tip would you like to give? 10% 12% 15% "))
# User inputs how many people to divide the cost
people = int(input("How many people to split the bill? "))
# Tip conversion to get actual percentage
tip_percentage = tip / 100
# Final calculation (Bill x percentage + bill divided by total people)
final_bill = round(((tip_percentage * bill) + bill) / people)
#Final output
print(f"Each person should pay ${final_bill:.2f}")