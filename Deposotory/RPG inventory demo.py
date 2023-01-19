inventory = [
    "Lock",
    "Lockpick",
    "Rusty sword",
]
i = len(inventory)
chest = [
    "Rusty Shield",
    "Not Rusty Sword",
    "Mana Potion",
]
a = "Rusty Shield"
b = "Not Rusty Sword"
c = "Mana Potion"
def adding_to_inventory(x):
    inventory.append(x)
    chest.remove(x)
    return inventory, chest

def value_of_d(x):
    question_list = ["Rusty Shield (a) or ", "Not Rusty Sword (b) or ", "Mana Potion (c):"]
    if x == a:
        del(question_list[0])
        e = eval(input(question_list))
        return e
    elif x == b:
        del(question_list[1])
        e = eval(input(question_list))
        return e
    elif x == c:
        del(question_list[2])
        e = eval(input(question_list))
        return e

#while i < 5:
d = eval(input("Rusty shield (a) or Not Rusty Sword (b) or Mana Potion (c):"))
adding_to_inventory(d)
e = value_of_d(d)
adding_to_inventory(e)
print(inventory)
print(chest)