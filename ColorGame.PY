import random
colors =['red','blue','green', 'white', 'black' ]

print("Welcome to Color guessing Game...")
print("*"*30)
computer_choice =random.choice(colors)

while True:
    player_choice = input("\nEnter your favorite color :").strip().lower()
    print(f"Computers pick : {computer_choice}")
    
    if player_choice not in colors:
        print("Sorry, you have the folloing options to pick from..")

        for i,c in enumerate(colors, start=1):
            print(f"{i}-{c}")

    elif player_choice ==computer_choice:
        print("You Win ")
    else:
        print("Sorry better luck next time...")

    print("Do you want to restart ? (Yes/No)")
    choice = input().strip().lower()
    if choice not in ['yes', 'y']:
        exit()
