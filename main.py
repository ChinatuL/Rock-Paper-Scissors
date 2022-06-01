import random


print("Let's play Rock Paper Scissors \n")

options_list = ["'R' for 'rock'", "'P' for 'paper'", "'S' for 'scissors'", "\n"]
for option in options_list:
    print(option)

game_options = ["R", "P", "S"]
while True: 
    user = input("Pick an option between 'R', 'P' or 'S': ").upper()
    CPU = random.choice(game_options)
    if user not in game_options:
        print("Invalid option") 
        continue       
    
    if user == "R":
        if CPU == "P":
            print("\nUser(Rock)" + " : " + "CPU(Paper)\n")
            print("Oops, You lose. \n\nGame over")
            break
        if CPU == "S":
            print("\nUser(Rock)" + " : " + "CPU(Scissors)\n")
            print("Yay! You win! \n\nGame over")
            break
        if CPU == "R":
            print("\nUser(Rock)" + " : " + "CPU(Rock)\n")
            print("A tie")
            continue      

    elif user == "S":
        if CPU == "R":
            print("\nUser(Scissors)" + " : " + "CPU(Rock)\n")
            print("Oops, You lose. \n\nGame over")   
            break        
        if CPU == "P":
            print("\nUser(Scissors)" + " : " + "CPU(Paper)\n")
            print("Yay! You win! \n\nGame over")
            break
        if CPU == "S":
            print("\nUser(Scissors)" + " : " + "CPU(Scissors)\n")
            print("A tie")
            continue
            
    elif user == "P":
        if CPU == "S":
            print("\nUser(Paper)" + " : " + "CPU(Scissors)\n")
            print("Oops, You lose. \n\nGame over")
            break
        if CPU == "R":
            print("\nUser(Paper)" + " : " + "CPU(Rock)\n")
            print("Yay! You win! \n\nGame over")
            break
        if CPU == "P":
            print("\nUser(Paper)" + " : " + "CPU(Paper)\n")
            print("A tie")
            continue
                


        
        
        

        