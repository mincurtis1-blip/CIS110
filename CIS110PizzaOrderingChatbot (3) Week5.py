#CIS110
#Curtis Min
#Week 5 Pizza Chatbot
print("Hello, my name is Alex, your virutal assisstant. I will help you order your pizza.")
print("I'm going to ask you a few questions. Please hit the enter key after each answer.")
userName = input("\nEnter your name:  ")
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name:   ")
if userName.lower() == "curtis":
    print(f"\nWelcome back {userName}, It is a pleasure to serve you!")
else:
    print(f"\nHello {userName}, nice to meet you!")
size = input("\nWhat size would you like? Please enter small, medium or large:      ")
while size.lower() not in ["small", "medium", "large"]:
    size = input("\nInvalid input! Please select small, medium, or large:     ")
while len(size) == 0:
    size = input("Size cannot be blank! Please enter your size:"   )
flavor = input("\nWhat flavor of pizza would you like? Please enter cheese, pepperoni, or veggie:      ")
while len(flavor) == 0:
    flavor = input("Flavor cannot be blank! Please select your flavor:   ")
crustType = input("\nWould you like traditional crust, NY style, or deep dish?              ")
while len(crustType) == 0:
    crustType = input("Crust cannot be blank! Please select your crust:    ")
quantity = input("\nHow many would you like? Please enter a number:    ")
while not quantity.isdigit():
    quantity = input("\nValue not recognized. Please enter a numeric value:   ")
quantity = int(quantity)
method = input("\nPlease select delivery or carryout:             ").lower()
while method not in ["carryout", "delivery"]:
    method = input("\nInvalid entry! Please select delivery or carryout:    ")
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0    
salesTax = 1.1 
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() =="large":
    pizzaCost = 17.99        
total = (pizzaCost * quantity) * salesTax + deliveryFee
print("-" * 10)
print(f"Thank you for your order, {userName}! ")
if total >= 50:
    print("\nCongratulations! You've been awarded a $10 off coupon for your next order.")
else: 
    print("\nOrders over $50 will receive a $10 off coupon on your next order.")
print("-" * 10)    
print(f"Your {quantity} {size} {crustType} {flavor} pizza(s) will be ${total:,.2f}.")
