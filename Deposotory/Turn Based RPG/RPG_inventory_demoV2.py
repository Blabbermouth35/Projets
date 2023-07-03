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
        Final = eval(input(question_list))
        return Final
    elif x == b:
        del(question_list[1])
        Final = eval(input(question_list))
        return Final
    elif x == c:
        del(question_list[2])
        Final = eval(input(question_list))
        return Final

#while i < 5:
d = eval(input("Rusty shield (a) or Not Rusty Sword (b) or Mana Potion (c):"))
adding_to_inventory(d)
e = value_of_d(d)
adding_to_inventory(e)
print("your inventory:")
print(inventory)
print("Remaining items in chest:")
print(chest)