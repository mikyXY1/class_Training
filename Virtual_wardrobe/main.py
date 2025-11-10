#vytvoreni tridy Clothing - obecny popis - DNA
class Clothing:
    # konstruktor třídy
    def __init__(self, name, color, size, material):
        self.name = name
        self.color = color
        self.size = size
        self.material = material

# vytvoreni instance = objektu tridy Clothing - "porod"
q_1 = Clothing("Tricko", "bile", "M", "bavlna")
q_2 = Clothing("Kalhoty", "modre", "L", "denim")

