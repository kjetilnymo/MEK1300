def main():
    player1 = 'X'
    player2 = 'O'
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    char_list = ['_'] * 9

    draw_board(num_list)
    draw_board(char_list)

    #move = get_player_input(player1, char_list)
    #print(move)

    #place_char_on_board(player1, move, char_list)
    #draw_board(num_list)
    #draw_board(char_list)

    while True:
        #player1 turn
        move = get_player_input(player1, char_list)
        place_char_on_board(player1,  move, char_list)

        draw_board(num_list)
        draw_board(char_list)

        if is_winner(player1, char_list):
            print("\nPlayer1 wins!")
            break
        if '_' not in char_list:
            print("\nThe  game is a tie!")
            break

        move = get_player_input(player2, char_list)
        place_char_on_board(player2,  move, char_list)

        draw_board(num_list)
        draw_board(char_list)

        if is_winner(player2, char_list):
            print("\nPlayer2 wins!")
            break


#prints a gameboard;either a number board or a tic tac toe board
def draw_board(char_list):
    print("\n\tTic-Tac-Toe")
    
    print("\t+++++++++++++++++")
    print("\t|| " + char_list[0] + " || " + char_list[1] + " || " + char_list[2] + " || ")
    
    print("\t+++++++++++++++++")
    print("\t|| " + char_list[3] + " || " + char_list[4] + " || " + char_list[5] + " || ")
    
    print("\t+++++++++++++++++")
    print("\t|| " + char_list[6] + " || " + char_list[7] + " || " + char_list[8] + " || ")
    


# get a player move until it is valid
def get_player_input(player_char, char_list):
    while True:
        while True:
            user_input = input("\n" + player_char + ": Where would you like to place your piece (1-9)")
            if user_input.isdigit():

                player_move = int(user_input)
                break
            else:
                print("Invalid input")
        if player_move > 0 and player_move < 10:
            if char_list[player_move - 1] == "_":
                return player_move
            else:
                print("That spot is taken. Try again")
            
        else:
            print("That is not a spot on the board. Try again.")


# put a players character at the correct spot on the board
def place_char_on_board(player_char, player_move, char_list):
    char_list[player_move - 1] = player_char

# return a bool if the given playe is winner
def is_winner():
    pass

main()