ticket_price = 10
num_tikcets = int(input("How many tickets would you like to purchase: "))

status = input("Provide your membership status: Silver or Gold or no-membership: ")

total_value = ticket_price * num_tikcets

if status == "Gold":
    total_value = total_value * 0.7

elif status == 'Silver':
    total_value = total_value * 0.85

else:
    total_value = total_value

print("Total value is:  ", total_value)