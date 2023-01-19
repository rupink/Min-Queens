import numpy as np
### WARNING: DO NOT CHANGE THE NAME OF THIS FILE, ITS FUNCTION SIGNATURE OR IMPORT STATEMENTS


def initialize_greedy_n_queens(N: int) -> list:
    """
    This function takes an integer N and produces an initial assignment that greedily (in terms of minimizing conflicts)
    assigns the row for each successive column. Note that if placing the i-th column's queen in multiple row positions j
    produces the same minimal number of conflicts, then you must break the tie RANDOMLY! This strongly affects the
    algorithm's performance!

    Example:
    Input N = 4 might produce greedy_init = np.array([0, 3, 1, 2]), which represents the following "chessboard":

     _ _ _ _
    |Q|_|_|_|
    |_|_|Q|_|
    |_|_|_|Q|
    |_|Q|_|_|

    which has one diagonal conflict between its two rightmost columns.

    You many only use numpy, which is imported as np, for this question. Access all functions needed via this name (np)
    as any additional import statements will be removed by the autograder.

    :param N: integer representing the size of the NxN chessboard
    :return: numpy array of shape (N,) containing an initial solution using greedy min-conflicts (this may contain
    conflicts). The i-th entry's value j represents the row  given as 0 <= j < N.
    """
    greedy_init = np.zeros(N, dtype=int)
    
    for i in range(N):
            greedy_init[i] = np.random.randint(0, N)

    
    for column in range(N):
        best_score = {}
        for entry in range(N):
            best_score[entry] = 0
            
            for enemy_q in range(N):
                #if enemy_q == greedy_init[column]:
                 #   continue
                
                if entry == greedy_init[enemy_q]:
                    #increment the total conflicts
                    best_score[entry]+=1
                
                if(column > enemy_q):
                    if (greedy_init[column] - greedy_init[enemy_q] == column - enemy_q):
                        best_score[entry]+=1
                    elif (greedy_init[enemy_q] - greedy_init[column] == column - enemy_q):
                        best_score[entry]+=1
                if (column < enemy_q):
                    if (greedy_init[column] - greedy_init[enemy_q] == enemy_q - column):
                        best_score[entry] +=1
                    elif (greedy_init[enemy_q] - greedy_init[column] == enemy_q - column):
                        best_score[entry] +=1
            '''
            temp_col = column
            temp_row = entry
            while True:
                temp_col-=1
                temp_row+=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N:
                    break
                
                if greedy_init[temp_col] == temp_row:
                    best_score[entry]+=1
                    
            temp_col = column
            temp_row = entry
            while True:
                temp_col+=1
                temp_row+=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N:
                    break
                
                if greedy_init[temp_col] == temp_row:
                    best_score[entry]+=1

            temp_col = column
            temp_row = entry
            while True:
                temp_col+=1
                temp_row-=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N:
                    break
                
                if greedy_init[temp_col] == temp_row:
                    best_score[entry]+=1
            ## Goes in direction down left
                    
            temp_col = column
            temp_row = entry
            while True:
                temp_col-=1
                temp_row-=1
                                                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N:
                    break
                
                if greedy_init[temp_col] == temp_row:
                    best_score[entry]+=1'''
                    
        best_score = dict(sorted(best_score.items(), key=lambda item: item[1]))
        
        temp = min(best_score.values())
        mins = [key for key in best_score if best_score[key] == temp]
        
        poten_move = np.random.randint(len(mins))
    
        greedy_init[column] = mins[poten_move]

    return greedy_init


if __name__ == '__main__':
    # You can test your code here
    final = initialize_greedy_n_queens(6)
