
class ClothingItem:
    def __init__(self, name, color, size, material):
        self.name = name
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self.color = color
        self.size = size
        self.material = material
    
    def print_info(self):
        print(f"Name: {self.name}, Color: {self.color}, Size: {self.size}, Material: {self.material}")

    def get_color(self):
        return self.color  


class Skirt(ClothingItem):
    def __init__(self, name, color, size, material, length):
        super().__init__(name, color, size, material)
        self.length = length
    
    def print_info(self):
        print(f"Name: {self.name}, Color: {self.color}, Size: {self.size}, Material: {self.material}, Length: {self.length}")


class Wardrobe:
    def __init__(self):
        self.clothing_items = []

    def add_item(self, item: ClothingItem):
        self.clothing_items.append(item)

    def print_items(self):
        for item in self.clothing_items:
            item.print_info()

    def get_items_by_color(self, color):
        return [item for item in self.clothing_items if item.get_color().lower() == color.lower()]

def main():
    wardrobe = Wardrobe()

    item1 = ClothingItem("T-shirt", "blue", "M", "cotton")
    item2 = ClothingItem("Jeans", "black", "L", "denim")
    item3 = ClothingItem("Jacket", "red", "S", "leather")

    item4 = Skirt("Summer Skirt", "yellow", "M", "linen", "knee-length")    

    wardrobe.add_item(item1)
    wardrobe.add_item(item2)
    wardrobe.add_item(item3)
    wardrobe.add_item(item4)

    # wardrobe.add_item(ClothingItem("T-shirt", "blue", "M", "cotton"))
    # wardrobe.add_item(ClothingItem("Jeans", "black", "L", "denim"))
    # wardrobe.add_item(ClothingItem("Jacket", "red", "S", "leather"))
    print("Wardrobe contents:")
    wardrobe.print_items()

    print("\nItems with color 'red':")
    red_items = wardrobe.get_items_by_color("red")
    for item in red_items:
        item.print_info()
    
    # print items by color defined by user input
    print("\nItems with color defined by user input:")
    user_color = input("Enter a color to search for: ")
    user_color_items = wardrobe.get_items_by_color(user_color)
    for item in user_color_items:
        item.print_info()

if __name__ == "__main__":
    main()

