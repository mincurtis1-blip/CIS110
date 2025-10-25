#CIS110
#Curtis Min
#Week 3 Pizza Chatbot
print("Hello, my name is Alex, your virutal assisstant. I will help you order your pizza.")
print("I'm going to ask you a few questions. Please hit the enter key after each answer.")
userName = input("\nEnter your name:  ")
print(f"\nHello {userName}. Nice to meet you!")
size = input("\nWhat size would you like? Please enter small, medium or large:      ")
flavor = input("\nWhat flavor of pizza would you like? Please enter cheese, pepporni, or veggie:      ")
crustType = input("\nWould you like traditional crust, NY style, or deep dish?              ")
quantity = input("\nHow many would you like? Please enter a number:    ")
quantity = int(quantity)
method = input("\nPlease select delivery or carry out:             ")
salesTax = 1.1 
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax
print("-" * 10)
print(f"Thank you for your order, {userName}! ")
print(f"Your {quantity} {size} {crustType} {flavor} pizza(s) will be ${total:,.2f}.")
