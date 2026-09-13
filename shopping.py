price = float(input("Enter the price of the item: "))
quantity = int(input("How many do you want to buy? "))
discount = input("Do you have a discount coupon? (True/False): ")
total_price = price * quantity
if discount == "True":
    total_price = total_price * 0.90
else:
    total_price = total_price

print("Final price:", total_price)