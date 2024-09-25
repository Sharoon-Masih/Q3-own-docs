import random
print("Welcome to Snake, Gun, Water game"); 

def showWeapon():
    weapons = ['snake','gun','water']
    for weapon in weapons:
        print(weapon)

showWeapon(); 
userInput = input("select your weapon from above list: ")

randomNum = random.randint(0,2); 

# 0 = snake
# 1 = water
# 2 = gun
if (userInput == "snake" and randomNum == 0):
    print('Game Draw!');
    print('you selected snake'); 
    print('computer selected snake');
elif (userInput == 'snake' and randomNum == 1):
    print('You have win!');
    print('you selected snake'); 
    print('computer selected water');
elif (userInput == 'snake' and randomNum == 2):
    print('You have loose!');
    print('you selected snake'); 
    print('computer selected gun');
elif (userInput == 'gun' and randomNum == 0):
    print('You have win!');
    print('you selected gun'); 
    print('computer selected snake');
elif (userInput == 'gun' and randomNum == 1):
    print('You have loose!');
    print('you selected gun'); 
    print('computer selected water');
elif (userInput == 'gun' and randomNum == 2):
    print('Game Draw!');
    print('you selected gun'); 
    print('computer selected gun');
elif (userInput == 'water' and randomNum == 0):
    print('you have loose!');
    print('you selected water'); 
    print('computer selected snake');
elif (userInput == 'water' and randomNum == 1):
    print('you have loose!');
    print('you selected water'); 
    print('computer selected water');
elif (userInput == 'water' and randomNum == 2):
    print('you have win!');
    print('you selected water'); 
    print('computer selected gun');
else:
    print("invalid input")