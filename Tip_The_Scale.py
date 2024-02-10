     
#  Description: This program is a game where each player inputs a number from 0 - 100.
#               The game number is 80% of the average of all the numbers.
#               The player with the closest number to the game number wins the round.
#               Each player loses 1 point except the winner.
#               If a player has -10 points, they are out of the game.
#               The player with the most points at the end of the game wins.
#               The game ends when there is only one player left.
#               The player with the most points at the end of the game wins.


# Game Logic

from os import system
import time

system('cls')
def run_game(inputs):
    sum = 0
    for i in range(len(inputs)):
        sum += inputs[i] 
    avg = sum / len(inputs)
    game = avg*0.8


    print("The game number is: ", game , "\n")
    #  find the closest number to the game


    winner_index = [False]*len(inputs)
    
    closest = inputs[0]
    for i in range(len(inputs)):
        if abs(inputs[i]-game) < abs(closest-game):
            closest = inputs[i]
    

    print("The closest number to the game is: ", closest)    
    for i in range(len(inputs)):
        if inputs[i] == closest:
            winner_index[i] = True
            
    print("\n")        
    return winner_index

# Game Rules
def game_rules():
    print("\nGame Rules: \n")
    print("Each player inputs a number from 0 - 100")
    print("The game number is 80%% of the average of all the numbers.")
    print("The player with the closest number to the game number wins the round.")
    print("Each player loses 1 point except the winner.")
    print("If a player has -5 points, they are out of the game. ")
    print("The game ends when there is only one player left.")


############### 
# Main Program

while True:
    try:
        print("Welcome to Tip The Scale\n") 
        numberOfPlayers = int(input("Enter the number of players: "))
        
        if 4 <= numberOfPlayers <= 10:
            break   
        else:
            print("Please enter no of players between 4 and 10.")
            time.sleep(1.5)
            system('cls')    
    except ValueError:
        print("Please enter no of players between 4 and 10.")
        time.sleep(1.5)
        system('cls')    
        
player_name = []
player_score = [0]*numberOfPlayers
player_inputs = [0]*numberOfPlayers

print("\n")
time.sleep(1)
for i in range(numberOfPlayers):
    name = input("Enter player " + str(i+1) + " name: ")
    player_name.append(name)
    time.sleep(.5)

time.sleep(1.5)
system('cls')


################
# print the rules of the game 
game_rules()

time.sleep(3)
# ready to Start Confirmation 
input("\nAre you ready to start the game? ( Player 1 press Enter to start )")
time.sleep(1.5)
system('cls')


################
# Loop of the Game

while len(player_name) > 1:
    print("\n")
    for i in range(len(player_inputs)):
        while True:
            try:
                player_inputs[i] = int(input("\n\n\nPlayer " + player_name[i] + " enter a number: "))
                if 0 <= player_inputs[i] <= 100:
                    break
                else:
                    print("Please enter any number between 0 and 100.")
            except ValueError:
                print("Please enter any number between 0 and 100.")
        system('cls')
    
    winners = run_game(player_inputs)
    if winners.count(True) == len(player_name):
        print("No one wins this round")
    else:
        for i in range(len(winners)):
            if winners[i]:
                print("The winner is: ", player_name[i])
            else:
                player_score[i] -= 1
    time.sleep(3)
    
        
    ######## not working ########
    # for i in range(len(player_score)):
    #     if i != winner:
    #         player_score[i] -= 1
    
    #print player score and names
    # for i in range(len(player_score)):
    #     if player_score[i] == -3:
    #         print(player_name[i], "is out of the game")
    #         player_name.pop(i)
    #         player_score.pop(i)
    #         player_inputs.pop(i)
    
    print("\nPlayer Scores")
    count = 0
    while count < len(player_score):
        if player_score[count] == -5:
            print(player_name[count], "is out of the game")
            player_name.pop(count)
            player_score.pop(count)
            player_inputs.pop(count)
        else:
            print(player_name[count], ": ", player_score[count]) 
            count += 1
    
    time.sleep(2)
    input(f'\n\nPlayer {player_name[0]} Press Enter to Continue.')
    time.sleep(1)
    system('cls')
    
############
# End of game

print("\nThe Ultimate Winner is: ") 
time.sleep(3)
print(player_name[0])  
# name = input("Please Enter your Ticket Number:  ")
# store_winners(name)
    