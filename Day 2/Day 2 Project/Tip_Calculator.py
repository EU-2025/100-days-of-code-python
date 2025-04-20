print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_porcentaje = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_per_person = (bill*(100 + tip_porcentaje)/100)/people
final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}") #Shows with two decimals but it depends on the las digits
print(f"Each person should pay: ${final_amount:.2f}") #Shows with two decimals but it will always shows the 2 last decimals
