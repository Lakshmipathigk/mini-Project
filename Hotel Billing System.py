menu = {
    "Masala Dosa": [60,True],
    "Puri": [30,True],
    "Edalli": [30,True],
    "Besibellibath": [25,True],
    "Full Mills": [80,True],
    "Half Mills": [40,False],
    "Pani puri": [25,True],
    "Coffe": [10,False],
    "Samosa": [20,True],
    "Lassi": [30,True],
    "Pizza": [160,True],
    "Masala Puri": [30,False],
    "Goobi": [45,False]
}
tables = list(range(1,11))

print("Welcome to the Hotel Billing System")
print("Available Tables",tables)
table_number = int(input("Enter the Table number: "))

if table_number not in tables:
    print("Table Number Invalid")
else:
    print(f"---Table number: {table_number} Menu---")
    total_bill=0
    ordered_items={}

for item, (price,available) in menu.items():
    status = "Available" if available else "Not Available"
    print(f"{item} : ${price} - {status}")

print("Place your order (type 'done' to finish):")

while True:
    item_name=input("Enter the item name: ").strip()
    if item_name.lower()=='done':
        break
    if item_name not in menu:
        print("Item not in menu")
        continue

    price,available = menu[item_name]
    if not available:
        print("Sorry, item as been closed")
        continue
    try:
        quantity=int(input(f"Mention the quantity {item_name}: "))
        item_total=price * quantity
        ordered_items[item_name]=(quantity,item_total)
        total_bill += item_total
    except ValueError:
        print("Not mentioned quantity,Please Mention the quantity")

print(f"---Bill for Table {table_number}---")
for item, (qty,total) in ordered_items.items():
    print(f"{item} x {qty} = ${total}")
print(f"Total Bill: ${total_bill}")
print("Thank you for dining with us!")