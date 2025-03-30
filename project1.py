# THIS PROJECT IS BASED ON THE GAME SNAKE WATER GUN

'''
1 for snake 
-1 for gun
0 for water
'''
import random

print("""Welcome to the game of Snake Water Gun
      Press "s" for snake
      Press "w" for water
      Press "g" for gun
      """)

# Randomly generate a number between 0 ,1, -1 for computer
comp = random.choice([0, 1, -1])


youstr = input("Enter your choice: ")

# Convert the input to lowercase to handle case insensitivity
youstr = youstr.lower()

# Dictionary to convert string to number
youdict = {
    "s": 1,
    "w": 0,
    "g": -1
}

# Dictionary to convert number to string for computer output
reversedict = {
    1: "s",
    0: "w",
    -1: "g"
}

you = youdict[youstr]# Convert the string to number using the dictionary

print(f"Computer choice: {reversedict[comp]}")
print(f"Your choice: {youstr}")

if ( comp == you ):
    print("It's a tie")
    
elif(comp == 1 and you == -1):
    print("You win")

elif(comp == 1 and you == 0):
    print("Computer wins")

elif(comp == 0 and you == 1):
        print("You win")

elif(comp == 0 and you == -1):
        print("Computer wins")

elif(comp == -1 and you == 1):
        print("Computer wins")  

else:
        print("You win")