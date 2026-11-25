print("Welcome to the Pizza Delight !" .upper())
print("Please enter the size of pizza you want to order: S, M, or L")
size = input("Enter your choice: ")
if size == "S":
    price=150
    print("The price of small pizza is INR 150")
elif size == "M":
    price=200
    print("The price of medium pizza is INR 200")   
elif size == "L":
    price=250
    print("The price of large pizza is INR 250")
else:
    print("Invalid size selected.")
    exit()
pizza_price=price
cheese = input("Do you want to add extra cheese? Y or N\n")
if cheese == "Y":
    price += 50
    print("The price of extra cheese is INR 50.") 
elif cheese == "N":
    price += 0
    print("You have not added any extra cheese.")
else:
    print("Invalid input.")
    exit()
print("\n---------- FINAL BILL ----------")
print("Pizza price: INR", price )
print("Extra cheese price: INR", 50 if cheese == "Y" else 0   )
print("--------------------------------")
print("Your final bill is: INR", price)
print("--------------------------------")
print("Thank you for ordering!")