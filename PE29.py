# MIS 207 PE29
#
#

data = {
        "00111": {
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
        }
    }


def print_dictionary(dict):
    header = (f"{'Key': <10}{'Description': <18}{'Price': ^8}{'Quantity': >8}")
    print(header)
    print('-' * len(header))
    for key in dict:
        print(f"{key: <10}{dict[key]['description']: <18}{dict[key]['price']: ^8}{dict[key]['quantity']: >8}")

print_dictionary(data)
#print(data.items())