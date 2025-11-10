from data import clothing_data

#vytvoreni tridy Clothing - obecny popis - DNA
class Clothing:
    # konstruktor třídy
    def __init__(self, name, color, size, material):
        self.name = name
        self.color = color
        self.size = size
        self.material = material

# vytvoreni instance = objektu tridy Clothing - "porod"
# q_1 = Clothing("Tricko", "bile", "M", "bavlna")
# q_2 = Clothing("Kalhoty", "modre", "L", "denim")


clothing_list = []
for one_item in clothing_data:       # bere data z Dictionary = clothing_data a uklada je do Listu = clothing_list
    name = (one_item["name"]) 
    color = (one_item["color"])
    size = (one_item["size"])
    material = (one_item["material"]) 
    new_item = Clothing(name, color, size, material)
    clothing_list.append(new_item)

print(clothing_list[0])  # vypise prvni objekt z listu clothing_list = name + color + size + material
print(clothing_list[0].name)  # vypise jen name prvniho oblečení z listu clothing_list
print(clothing_list[0].color)  # vypise jen color prvniho oblečení z listu clothing_list
print(clothing_list[0].size)  # vypise jen size prvniho oblečení z listu clothing_list
print(clothing_list[0].material)  # vypise jen material prvniho oblečení z listu clothing_list
print(clothing_list)
