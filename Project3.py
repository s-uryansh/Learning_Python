print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
choice1 = input()
# choice 1 just changing to lowercase
choice11 = choice1.lower()
if choice11 != "left":
    print("Fall into a hole.\nGame Over.")
else:
    print("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swin across. ")

    choice2 = input()
        # choice 2 just changing to lowercase
    choice22 = choice2.lower()
    if choice22 !="wait":
        print("Attacked by trout.\nGame Over.")
    else:
        print("You arrive at a island unharmed. There are 3 door one red, one blue and one yellow. Which colour do you choose.")
        door = input()
        doorColor = door.lower()
        if doorColor == "red":
            print("Burned by fire.\nGame Over")
        elif doorColor == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif doorColor == "yellow":
            print("You Win!")




