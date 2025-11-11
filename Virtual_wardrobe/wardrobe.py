
class ClothingItem:  # hlavní třída pro oblečení
    def __init__(self, name, color, size, material):
        self.name = name
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self.color = color
        self.size = size
        self.material = material
    
    def print_info(self): # metoda pro výpis informací o oblečení
        print(f"Name: {self.name}, Color: {self.color}, Size: {self.size}, Material: {self.material}")

    def get_color(self): # získání barvy oblečení
        return self.color  


class Skirt(ClothingItem): # podtřída pro sukně, dědí z ClothingItem
    def __init__(self, name, color, size, material, length):  # konstruktor podtřídy
        super().__init__(name, color, size, material)   # volání konstruktoru rodičovské třídy
        self.length = length  # délka sukně v cm
    
    def print_info(self): # přepsaná metoda pro výpis informací o sukni
        print(f"Name: {self.name}, Color: {self.color}, Size: {self.size}, Material: {self.material}, Length: {self.length}")


class Wardrobe: # třída pro šatník, obsahuje seznam oblečení
    def __init__(self):  # konstruktor třídy Wardrobe
        self.clothing_items = []    # seznam položek oblečení

    def add_item(self, item: ClothingItem):  #přidání oblečení do šatníku
        self.clothing_items.append(item)  # přidání položky do seznamu

    def print_items(self):          # výpis všech položek v šatníku
        for item in self.clothing_items:
            item.print_info()

    def get_items_by_color(self, color):   # získání položek podle barvy
        return [item for item in self.clothing_items if item.get_color().lower() == color.lower()]

def main():
    wardrobe = Wardrobe()   # vytvoření instance šatníku

    item1 = ClothingItem("T-shirt", "blue", "M", "cotton")  # vytvoření několika položek oblečení
    item2 = ClothingItem("Jeans", "black", "L", "denim")
    item3 = ClothingItem("Jacket", "red", "S", "leather")

    item4 = Skirt("Summer Skirt", "yellow", "M", "linen", "knee-length")  # vytvoření sukně jako instance podtřídy Skirt   

    wardrobe.add_item(item1)   # přidání položek do šatníku
    wardrobe.add_item(item2)
    wardrobe.add_item(item3)
    wardrobe.add_item(item4)

    # wardrobe.add_item(ClothingItem("T-shirt", "blue", "M", "cotton"))
    # wardrobe.add_item(ClothingItem("Jeans", "black", "L", "denim"))
    # wardrobe.add_item(ClothingItem("Jacket", "red", "S", "leather"))
    # wardrobe.add_item(Skirt("Summer Skirt", "yellow", "M", "linen", "knee-length"))

    print("Wardrobe contents:")   # výpis všech položek v šatníku
    wardrobe.print_items()

    print("\nItems with color 'red':")   # výpis položek podle barvy
    red_items = wardrobe.get_items_by_color("red")
    for item in red_items:
        item.print_info()
    
    # tisk položek podle barvy definované uživatelem
    print("\nItems with color defined by user input:")
    user_color = input("Enter a color to search for: ")
    user_color_items = wardrobe.get_items_by_color(user_color)
    for item in user_color_items:
        item.print_info()

if __name__ == "__main__":   # spuštění hlavní funkce
    main()

