# Snake water gun game
import random
def gameWin(comp , you):
    if comp==you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
        
comp = input(" Computer Turn : Snake(s) , Gun(g) , Water(w)? ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "g"
elif randNo == 3:
    comp = "w"


you = input("your's Turn : Snake(s) , Gun(g) , Water(w)? ")
a = gameWin(comp , you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("This game is a Tie!")
elif a:
    print("You Win!")
else:
    
    print("You Lose!")