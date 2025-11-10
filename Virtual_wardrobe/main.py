from data import clothing_data

#vytvoreni tridy Clothing - obecny popis - DNA
class Clothing:
    # konstruktor třídy
    def __init__(self, name, color, size, material):
        self.name = name
        self.color = color
        self.size = size
        self.material = material

    def find_color(color):   # metoda pro nalezeni barvy obleceni
        for item in clothing_list:
            if item.color.lower() == color.lower():
                print(f"Nalezene obleceni: {item.name}, Barva: {item.color}, Velikost: {item.size}, Material: {item.material}")

    def fce_add(name, color, size, material):   # metoda pro pridani noveho obleceni do seznamu
        new_item = Clothing(name, color, size, material)
        clothing_list.append(new_item)
        print(f"Pridano obleceni: {new_item.name}, Barva: {new_item.color}, Velikost: {new_item.size}, Material: {new_item.material}")

    
# vytvoreni instance = objektu tridy Clothing - "porod"
# q_1 = Clothing("Tricko", "bile", "M", "bavlna")

clothing_list = []
for one_item in clothing_data:       # bere data z Dictionary = clothing_data a uklada je do Listu = clothing_list
    name = (one_item["name"]) 
    color = (one_item["color"])
    size = (one_item["size"])
    material = (one_item["material"]) 
    new_item = Clothing(name, color, size, material)
    clothing_list.append(new_item)

user_answer = input(f"Jakou barvu obleceni hledate?: \n")   #metoda pro hledani barvy obleceni
Clothing.find_color(user_answer)

n_name = input(f"Co chces pridat? Zadej nazev obleceni: \n") #metoda pro pridani noveho obleceni do seznamu
n_color = input(f"zadej barvu: \n")
n_size = input(f"zadej size: \n")
n_material = input(f"zadej material: \n")
Clothing.fce_add(n_name, n_color, n_size, n_material)

# print(clothing_list[0])  # vypise prvni objekt z listu clothing_list = name + color + size + material
# print(clothing_list[0].name)  # vypise jen name prvniho oblečení z listu clothing_list
# print(clothing_list[0].color)  # vypise jen color prvniho oblečení z listu clothing_list
# print(clothing_list[0].size)  # vypise jen size prvniho oblečení z listu clothing_list
# print(clothing_list[0].material)  # vypise jen material prvniho oblečení z listu clothing_list
# print(clothing_list)
