# MIS 207 PE28
#

medals = {
    'Canada': {"Gold":3, "Silver":3, "Bronze":4},
    'China': {"Gold": 13, "Silver": 14, "Bronze": 18},
    'United States': {"Gold": 23, "Silver": 28, "Bronze":
32},
    'Japan': {"Gold": 10, "Silver": 9, "Bronze": 2}
}



def medals_list_creation(dictionary):
    medals_list = []
    for country, keys in medals.items():
        for values in keys.values():
            medals_list.append(values)
    return medals_list

def print_dictionary():
    print(f"{' ':<15}{'Gold':^8}{'Silver':^8}{'Bronze':^8}")
    s = 0
    f = 3
    for country in medals.keys():
        print(f"{country: <15}", end='')
        for num_medals in medals_list_creation(medals)[s:f]:
            print(f'{num_medals: ^8}', end='')
        s += 3
        f += 3
        print()

print_dictionary()


