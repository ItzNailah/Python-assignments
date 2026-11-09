print("welcome to CATUC POS")
num_items = int(input("please enter how many items purchased:"))

#Create empty lists
items_name = []
items_quantity = []
items_price = []
items_cost = []

for item in range(1,num_items+1):
    name = input("please enter name of item: ")
    quantity = int(input("please enter quantity: "))
    price = float(input("please enter cost of item (FCFA): "))
    cost = quantity*price
#store the info in the list
    items_name.append(name)
    items_quantity.append(quantity)
    items_price.append(price)
    items_cost.append(cost)

items_cost_total = sum(items_cost)

print("\nS/N Description quantity unit price total price")
for item in range(num_items):
    print(f"{item+1} {items_name[item]} {items_quantity[item]} FCFA {items_price[item]:,.2f} FCFA {items_cost[item]:,.2f}")
# to calculate discount
if items_cost_total>5000:
    discount=0.30*items_cost_total
    total_cost = items_cost_total - discount
    print(f"Discount = FCFA {discount:,.2f}")
    
elif (len(items_cost) >5) and items_cost_total >4000:
    discount = 0.15 * items_cost_total
    total_cost= items_cost_total-discount
    print(f"Discount = FCFA {discount:,.2f}")
elif items_cost_total >1000:
    discount=0.10*items_cost_total
    total_cost = items_cost_total - discount
    print(f"Discount = FCFA {discount:,.2f}")
else:
    total_cost = items_cost_total
    print("No discount")

print(f"Total expenditure= FCFA {items_cost_total:,.2f}")
print(f"Total purchase = FCFA {total_cost:,.2f}")
print(" Thank you")

    
