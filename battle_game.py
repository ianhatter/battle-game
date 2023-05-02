wizard = "Wizard"
elf = "elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:

    wizard = "Wizard"
    elf = "elf"
    human = "Human"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20

    dragon_hp = 300
    dragon_damage = 50

    print("1. Wizard")
    print("2. Elf")
    print("3. Human")

    character = input("choose your character:")
    if character == "1":
        print("Wizard")
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break

    elif character == "2":
        print("Elf")
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break

    elif character == "3":
        print("Human")
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break

    else:
        print("Unknown Charecter.")

print("You have choosen: " + character)
print("HP "+str(my_hp) + " damage " + str(my_damage))

while True:
    dragon_hp = dragon_hp - my_damage
    my_hp = my_hp - dragon_damage

    print(" The ", character, " damaged the Dragon! " +
          " The Dragons hit points are now " + str(dragon_hp))

    if dragon_hp <= 0:
        print("The dragon has lost the battle")
        break
    else:
        dragon_hp <= 1
        print("The Dragon strikes back at: " + character + " The ",
              character, " hit points are now: " + str(my_hp))
    if my_hp <= 0:
        print("The ", character, " has lost the battle")
        break
