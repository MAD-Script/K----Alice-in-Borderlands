     
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

# Program Variables , subject to change
player_name = ["A","B","C","D","E"]
player_score = [0,0,0,0,0]
player_inputs = [0,0,0,0,0]

# Game Rules
    # each player inputs a number to store in player_inputs
    # run game until all players except one have -10 score,
    # each player loses 1 point except the winner 
    # if a player has -10 score, they are out of the game


############### 
# Main Program
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
        
# End of game
print("\nThe Ultimate Winner is: ", player_name[0])    
    