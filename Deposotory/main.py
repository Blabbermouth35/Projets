
inventory = [
    "Lock",
    "Lockpick",
    "Rusty sword",
]
i = len(inventory)
chest = [
    "Rusty shield",
    "Not rusty sword",
    "Mana Potion",
]
def adding_to_inventory(x):
    inventory.append(x)
    chest.remove(x)
    return inventory, chest

def chest_check(x):
    choice_list = {a: chest[0], b: chest[1], c: chest[2]}
    question_list = {chest[0]: "Rusty Shield(a) or ", chest[1]: "Not Rusty Sword (b) or ", chest[2]: "Mana Potion"}
    try:
        chest.remove(x)
        chest.append(x)
        question_list.remove(choice_list[x])
    except:
        print("The chest does not contain this item")

while i < 5:
    a = "Rusty shield"
    b = "Not rusty shield"
    c = "Mana Potion"
    d = eval(input("Rusty Shield (a) or Not Rusty Sword (b) or Mana Potion(c):"))
    try:
        adding_to_inventory(d)
        i = len(inventory)
        chest_check(d)
        e = eval(input(question_list))

    except:
        print("Please enter one of the inputs that are inside of parentheses")
print(inventory)