# MIS 207 HW08 Q2
#
# Calculate the total value of the inventory from the given output

data = {
    "00111":
        {
        "description": "Hockey Stick",
        "price": 12.23,
        "quantity": 23
    },
    "00223": {
        "description": "Baseball",
        "price": 8.78,
        "quantity": 32
    },
    "00451": {
        "description": "Basketball",
        "price": 29.63,
        "quantity": 19
    },
    "04022": {
        "description": "Puck",
        "price": 2.87,
        "quantity": 22
    },
    "90001": {
        "description": "Football",
        "price": 32.99,
        "quantity": 16
    },
    "08001": {
        "description": "Tennis Ball",
        "price": 2.23,
        "quantity": 19
    },
    "00701": {
        "description": "Tennis Racket",
        "price": 11.23,
        "quantity": 44
    },
    "06601": {
        "description": "Baseball Bat",
        "price": 22.23,
        "quantity": 13
    }
}


total_inventory = 0
for key in data:
    price = float(data[key]['price'])
    quantity = float(data[key]['quantity'])
    total_inventory += price * quantity

print(f'The total value of the inventory is: ${total_inventory:.2f}.')