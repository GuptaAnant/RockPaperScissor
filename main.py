import random

def game(comp, you):
    if comp == "stone":
        if you == "stone":
            print("Draw")
        elif you == "paper":
            print("You won")
        elif you == "scissor":
            print("You lose")
        else:
            print("Enter valid value")

    if comp == "paper":
        if you == "stone":
            print("You lose")
        elif you == "paper":
            print("Draw")
        elif you == "scissor":
            print("You won")
        else:
            print("Enter valid value")

    if comp == "scissor":
        if you == "stone":
            print("You won")
        elif you == "paper":
            print("You lose")
        elif you == "scissor":
            print("Draw")
        else:
            print("Enter valid value")

randNum = random.randint(1, 3)
# print(randNum)

comp = print("Comp's turn")

if randNum == 1:
    comp = "stone"
elif randNum == 2:
    comp = "paper"
else:
    comp = "scissor"

you = input("User's turn Stone(stone), Paper(paper), Scissor(scissor)?")

print(f"You chose {you}")
print(f"Computer chose {comp}")

game(comp, you) 