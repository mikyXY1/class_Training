import pytest
from wardrobe import ClothingItem, Skirt, Wardrobe


def test_clothing_item_init_and_print_info(capsys):
    item = ClothingItem("T-shirt", "blue", "M", "cotton")
    assert item.name == "T-shirt"
    assert item.color == "blue"
    assert item.size == "M"
    assert item.material == "cotton"
    item.print_info()
    captured = capsys.readouterr()
    assert "Name: T-shirt" in captured.out


def test_skirt_inherits_and_length(capsys):
    skirt = Skirt("Mini Skirt", "pink", "S", "silk", length=40)
    assert skirt.name == "Mini Skirt"
    assert skirt.color == "pink"
    assert skirt.size == "S"
    assert skirt.material == "silk"
    assert skirt.length == 40
    skirt.print_info()
    captured = capsys.readouterr()
    assert "Length: 40" in captured.out


def test_wardrobe_add_and_print_items(capsys):
    w = Wardrobe()
    t = ClothingItem("T-shirt", "blue", "M", "cotton")
    s = Skirt("Long Skirt", "black", "L", "linen", length=90)
    w.add_item(t)
    w.add_item(s)
    w.print_items()
    captured = capsys.readouterr()
    assert "T-shirt" in captured.out
    assert "Long Skirt" in captured.out
    assert "Length: 90" in captured.out


def test_color_is_string_not_number():
    # color should be a string; reject numeric colors
    ci = ClothingItem("Hat", "red", "M", "wool")
    assert isinstance(ci.color, str)

    # also ensure numeric values are not accepted as a valid color type
    with pytest.raises(TypeError):
        ClothingItem("Scarf", 123, "L", "cotton")
