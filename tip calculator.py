print("Welcome to the tip calculator!")
bill=float(input ("What was the total bill? INR"))
tip=int(input("what amount of tip would you like to give?"))
people=int(input("How many people to split the bill?"))
bill_with_tip=tip/100*bill+bill
total_amount=bill_with_tip/people
final_amount=round(total_amount, 2)
print(f"Each person should pay :INR {final_amount}")

