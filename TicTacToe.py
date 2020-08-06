#In[]

from IPython.display import clear_output

#In[]
def display_board(board):
    
    print("{}  |  {}  |  {}".format(board[0], board[1],board[2]))
    print("---------------")
    print("{}  |  {}  |  {}".format(board[3], board[4],board[5]))
    print("---------------")
    print("{}  |  {}  |  {}".format(board[6], board[7],board[8]))
    
#In[]
def player_input():
    
    choice = 'wrong'
    marker = "NO MARKER ASSIGNED"
    global player1 # whenever player_input() changes player1's value, it changes the 
                   # original value of the player1
    global player2
    
    
    while choice not in ['X', 'O']:
        choice = input("Player 1: Do you want to be X or O: " )
        
        if choice == 'X':
            marker = 'X'
        elif choice == 'O':
            marker = 'O'
        else:
            clear_output()
            print("Sorry, Invalid Output!")
    
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    print("\nPlayer 1 will go first with " + player1)    
    return player1


#In[]
def place_marker(empty_test_board,marker,position):
    
    # Validate the position for the board
    acceptable_positions = ['1','2','3','4','5','6','7','8','9']
    
    while position not in acceptable_positions:
        position = input("Sorry, invalid position, re-enter (1-9): ")
        
        if position.isdigit() == False:
            print("Sorry, digits only (1-9)")
        else:
            pass
    
    position = int(position)
    
    # if that place is already occupied, then make the user chose another spot
    if space_check(empty_test_board,position) == False:
        
        while space_check(empty_test_board,position) == False:
            position = input("Please choose an empty spot (1-9): ")
            
            if position.isdigit() == False:
                while position.isdigit() == False:
                    position = input("Sorry, digits only. Choose an empty spot (1-9): ")
                    
            if position not in acceptable_positions:
                while position not in acceptable_positions:
                    position = input("Please choose an empty spot between [1-9]: ")
            else:
                position = int(position)
    
    
    print("Board before changing: ")
    display_board(empty_test_board)
    
    empty_test_board[position-1] = marker
    print("\n\nBoard after changing: ")
    display_board(empty_test_board)
    print("-----------------------------------")


#In[]
def win_check(board, mark):
    
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
    elif board[3] == mark and board[4] == mark and board[5] == mark:
        return True
    elif board[6] == mark and board[7] == mark and board[8] == mark:
        return True
    elif board[0] == mark and board[3] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[0] == mark and board[4] == mark and board[8] == mark:
        return True
    elif board[2] == mark and board[4] == mark and board[6] == mark:
        return True
    else:
        return False

#In[]
import random

#In[]
def choose_first():
    result = random.randint(1,2)
    
    if result == 1:
        print("Player 1 has been chosen to go first!")
        return player1
    else:
        print("Player 2 has been chosen to go first!")
        return player2


#In[]
def space_check(board, position):
    if board[position-1] == '' or board[position-1] == ' ':
        return True
    else:
        return False


#In[]
def full_board_check(board):
    
    boolVal = True
    
    for item in board:
        if item == ' ' or item == '':
            boolVal = False
            break
        else:
            pass
        
    return boolVal

#In[]
def player_choice(board):
    
    position = 'wrong'
    acceptable_values = ['1','2','3','4','5','6','7','8','9']
    
    while position not in acceptable_values:
        position = input("Enter the next position: ")
        
        if position.isdigit() == False or position not in acceptable_values:
            clear_output()
            print("Sorry, invalid output! Choose between (1-9): ")
            
    
    position = int(position)
    boolVal = space_check(board,position)
    
    if boolVal == True:
        return position # "Numpad" position
    else:
        print("Sorry, the spot is filled!")

#In[]
def replay():
    
    choice = 'wrong'
    
    while choice not in ["Y","N"]:
        choice = input("Do you want to play again? (Y or N): ")
        
        if choice not in ["Y","N"]:
            clear_output()
            print("Sorry, invalid output!")
        
    if choice == "Y":
        return True
        # Here, we should assign empty space to each element in the board again
    else:
        return False



#In[]
###########################################################
# GAME BEGINS
###########################################################

print("Welcome to Tic Tac Toe!")

gameon = True
empty_test_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player1 = 'No marker assigned!'
player2 = 'No marker assigned!'


# Step 1
display_board(empty_test_board)

# Step 2
player1 = player_input()
print("Player 1: " + player1)
print("Player 2: " + player2)

# Step 3
while gameon == True:
    while full_board_check(empty_test_board) == False:
        p1_pos = input("\n\nHey Player 1, where do you want to place " + player1 + "?: ")
        place_marker(empty_test_board,player1,p1_pos)

        boolVal = win_check(empty_test_board,player1)
        if boolVal == True:
            print("=======================================")
            print("Congratulations Player 1, you won!!!")
            print("=======================================")
            empty_test_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            break
        
        if full_board_check(empty_test_board) == True:
            print("\nBummer, Nobody won...\n")
            empty_test_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            break

        p2_pos = input("\n\nPlayer 2, where do you want to place " + player2 + "?: ")
        place_marker(empty_test_board,player2,p2_pos)

        boolVal_2 = win_check(empty_test_board,player2)
        if boolVal_2 == True:
            print("=======================================")
            print("\nCongratulations Player 2, you won!!!")
            print("=======================================")
            empty_test_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            break
            
        if full_board_check(empty_test_board) == True:
            print("\nBummer, Nobody won...\n")
            empty_test_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            break
            
     
    if gameon == True:
        choice = input("Do you want to play again? (Y or N): ")
        
        while choice not in ['Y','N']:
            choice = input("Sorry, I didn't understand. Please choose Y or N: ")
            
    if choice == 'N':
        gameon = False
        print("\n\n\n=============")
        print("=============")
        print("GOODBYE!")
        print("=============")
        print("=============")
    else:
        # Step 1
        display_board(empty_test_board)

        # Step 2
        player1 = player_input()
        print("Player 1: " + player1)
        print("Player 2: " + player2)
        
        gameon = True

        

# %%
