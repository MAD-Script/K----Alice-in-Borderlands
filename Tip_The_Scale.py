     
#  Description: This program is a game where each player inputs a number from 0 - 100.
#               The game number is 80% of the average of all the numbers.
#               The player with the closest number to the game number wins the round.
#               Each player loses 1 point except the winner.
#               If a player has -10 points, they are out of the game.
#               The player with the most points at the end of the game wins.
#               The game ends when there is only one player left.
#               The player with the most points at the end of the game wins.


# Game Logic
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

print("Welcome to Tip The Scale\n")
numberOfPlayers = int(input("Enter the number of players: "))

player_name = []
player_score = [0]*numberOfPlayers
player_inputs = [0]*numberOfPlayers

for i in range(numberOfPlayers):
    name = input("Enter player " + str(i+1) + " name: ")
    player_name.append(name)


################
# print the rules of the game 
game_rules()


################
# Loop of the Game


# TODO - limit input to 0 - 100
#      - limit input to only numbers
#      - add more variables

while len(player_name) > 1:
    print("\n")
    for i in range(len(player_inputs)):
        player_inputs[i] = int(input("Player " + player_name[i] + " enter a number: "))
    
    winners = run_game(player_inputs)
    if winners.count(True) == len(player_name):
        print("No one wins this round")
    else:
        for i in range(len(winners)):
            if winners[i]:
                print("The winner is: ", player_name[i])
            else:
                player_score[i] -= 1
        
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
        
############
# End of game

print("\nThe Ultimate Winner is: ", player_name[0])    
    