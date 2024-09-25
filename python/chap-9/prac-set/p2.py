import random


def game():

    score = 0

    print("Welcome to Snake, Gun, Water game")

    def showWeapon():
        weapons = ["snake", "gun", "water"]
        for weapon in weapons:
            print(weapon)

    showWeapon()

    for i in range(3):

        print(f"\n {i+1} turn \n")
        userInput = input("select your weapon from above list: ")

        randomNum = random.randint(0, 2)
        # 0 = snake
        # 1 = water
        # 2 = gun
        if userInput == "snake" and randomNum == 0:
            print("Game Draw!")
            print("you selected snake")
            print("computer selected snake")
        elif userInput == "snake" and randomNum == 1:
            print("You have win!")
            print("you selected snake")
            print("computer selected water")
            score += 5
        elif userInput == "snake" and randomNum == 2:
            print("You have loose!")
            print("you selected snake")
            print("computer selected gun")
            score -= 5
        elif userInput == "gun" and randomNum == 0:
            print("You have win!")
            print("you selected gun")
            print("computer selected snake")
            score += 5
        elif userInput == "gun" and randomNum == 1:
            print("You have loose!")
            print("you selected gun")
            print("computer selected water")
            score -= 5
        elif userInput == "gun" and randomNum == 2:
            print("Game Draw!")
            print("you selected gun")
            print("computer selected gun")
        elif userInput == "water" and randomNum == 0:
            print("you have loose!")
            print("you selected water")
            print("computer selected snake")
            score -= 5
        elif userInput == "water" and randomNum == 1:
            print("Game draw!")
            print("you selected water")
            print("computer selected water")
        elif userInput == "water" and randomNum == 2:
            print("you have win!")
            print("you selected water")
            print("computer selected gun")
            score += 5
        else:
            print("something went wrong")
    print("\n your total score is:", score)

    # setting high score in HI-score file.
    with open("G:/python/chap-9/HI-score.txt") as f:
        highScore = f.read()
        if highScore != "":
            highScore = score # yeh file ma koi be changes nhi krega yeh srf yaha code ma check krnay kay liya humna pehla check kia kay agr file empty nhi hai toh highScore variable ko new score assign krdo.bcuz its obvious kay agr file empty nhi hai toh its mean that kay usme pehla koi score hoga.
        else:
            highScore = 0  # agr empty hai toh simply isko 0 assign krdo.
        if score > highScore: #ab mainly yaha par file ma changes hongay 
            with open("G:/python/chap-9/HI-score.txt", "w") as f1: # yaha ab jo score hai usko store krdeinga file may.
                f1.write(str(score))
            print("you have set a new high score")


game()
