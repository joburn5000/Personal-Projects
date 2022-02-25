/*
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. 
Return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.


Completed: September 24
*/


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[" "]*3 for i in range(3)]
        player_turn = "A"
        winner = "Pending"
        moves_played = 0
        
        
        # create board
        for move in moves: # A is even indeces, B is odd
            board[move[0]][move[1]] = player_turn
            # print("x: " + str(move[1]) + ", y: " + str(move[0]) + " = " + player_turn)
            if player_turn == "A":
                player_turn = "B"
            else:
                player_turn = "A"
            moves_played += 1
        
        # check collumns
        for x in range(3):
            player_move = board[0][x]
            streak = "intact"
            if player_move == " ": continue
            for y in range(1,3):
                if board[y][x] != player_move:
                    streak = "broken"
                    break
            if streak == "intact":
                winner = player_move
                break
        
        # check rows
        if winner == "Pending":
            for y in range(3):
                player_move = board[y][0]
                streak = "intact"
                if player_move == " ": continue
                for x in range(1,3):
                    if board[y][x] != player_move:
                        streak = "broken"
                        break
                if streak == "intact":
                    winner = player_move
                    break
        
        # check [0,0] to [2,2] diagonal
        if winner == "Pending":
            player_move = board[0][0]
            streak = "intact"
            if player_move == " ":
                streak = "broken"
            for x in range(1,3):
                if board[x][x] != player_move:
                    streak = "broken"
                    break   
            if streak == "intact":
                winner = player_move
        
        # check [0,2] to [2,0] diagonal
        if winner == "Pending":
            player_move = board[0][2]
            streak = "intact"
            if player_move == " ":
                streak = "broken"
            for x in range(1,3):
                if board[x][2-x] != player_move:
                    streak = "broken"
                    break   
            if streak == "intact":
                winner = player_move
        
        if winner == "Pending" and moves_played == 9:
            return "Draw"
        return winner
        
