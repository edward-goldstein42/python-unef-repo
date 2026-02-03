#w04 Review coding challeng
menu = {
        "Lotus": 7.50,
        "Americano": 3.50,
        "Latte": 5,
        "Espresso": 6.25,
        }

receipt = {
    "Customer": 0.0,
    "Drink": 0.0,
    "Price": 0.0,
    }
customer = input("Enter customer name: ")
order = input("Please select your drink order:")
drink_price=menu[order]
receipt.update({"Customer": customer})
receipt.update({"Drink": order})
receipt.update({"Price": drink_price})
#debug
print(">>>>Jitters<<<<")
print(f"Customer: {receipt["Customer"]}")
print(f"Drink: {receipt["Drink"]}")
print(f"Total: ${receipt["Price"]}")