print("welcome to tip calculator")
total_bill=float(input("what was the total bill?:"))

percentage_tip=int(input("how much tip would you like to give? : "))

number_of_people=int(input("how many people are spliting the bill? : "))

payment_per_person=(round(float(((percentage_tip/100+1)* total_bill)/number_of_people), 2))

print(f"each person owes:₹{payment_per_person}")
