import numpy as np
from initialize_greedy_n_queens import initialize_greedy_n_queens
from support import plot_n_queens_solution
### WARNING: DO NOT CHANGE THE NAME OF THIS FILE, ITS FUNCTION SIGNATURE OR IMPORT STATEMENTS


def min_conflicts_n_queens(initialization: list) -> (list, int):
    """
    Solve the N-queens problem with no conflicts (i.e. each row, column, and diagonal contains at most 1 queen).
    Given an initialization for the N-queens problem, which may contain conflicts, this function uses the min-conflicts
    heuristic(see AIMA, pg. 221) to produce a conflict-free solution.

    Be sure to break 'ties' (in terms of minimial conflicts produced by a placement in a row) randomly.
    You should have a hard limit of 1000 steps, as your algorithm should be able to find a solution in far fewer (this
    is assuming you implemented initialize_greedy_n_queens.py correctly).

    Return the solution and the number of steps taken as a tuple. You will only be graded on the solution, but the
    number of steps is useful for your debugging and learning. If this algorithm and your initialization algorithm are
    implemented correctly, you should only take an average of 50 steps for values of N up to 1e6.

    As usual, do not change the import statements at the top of the file. You may import your initialize_greedy_n_queens
    function for testing on your machine, but it will be removed on the autograder (our test script will import both of
    your functions).

    On failure to find a solution after 1000 steps, return the tuple ([], -1).

    :param initialization: numpy array of shape (N,) where the i-th entry is the row of the queen in the ith column (may
                           contain conflicts)

    :return: solution - numpy array of shape (N,) containing a-conflict free assignment of queens (i-th entry represents
    the row of the i-th column, indexed from 0 to N-1)
             num_steps - number of steps (i.e. reassignment of 1 queen's position) required to find the solution.
    """

    N = len(initialization)
    solution = initialization.copy()
    
    #check conflict
    
    
    num_steps = 0
    max_steps = 10000
    


    for idx in range(max_steps):
        num_steps+=1
        queen_conf = {}
        
            
        #Check if queen is in range or enemy queen
                    
        ## Checks the diagnols of each queen
        for queen in reversed(range(N)):
            queen_conf[queen] = False
            
            for enemy_q in reversed(range(N)):
                if queen == enemy_q:
                    continue
                
                elif solution[queen] == solution[enemy_q]:
                    #increment the total conflicts
                    queen_conf[queen]=True
                    break
                
                if (queen>enemy_q):
                    if (solution[queen] - solution[enemy_q] == queen - enemy_q):
                        queen_conf[queen]=True
                        break
                    elif (solution[enemy_q] - solution[queen] == queen - enemy_q):
                        queen_conf[queen]=True
                        break
                else:
                    if (solution[queen] - solution[enemy_q] == enemy_q - queen):
                        queen_conf[queen]=True
                        break
                    elif (solution[enemy_q] - solution[queen] == enemy_q - queen):
                        queen_conf[queen]=True
                        break
            ## Goes in direction up right
            '''temp_col = queen
            temp_row = solution[queen]
                        
            while True:
                temp_col+=1
                temp_row+=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N or queen_conf[queen] == True:
                    break
                
                if solution[temp_col] == temp_row:
                    queen_conf[queen] =True
        
            ## Goes in direction down right

            temp_col = queen
            temp_row = solution[queen]
            
            while True:
                temp_col+=1
                temp_row-=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N or queen_conf[queen] == True:
                    break
                
                if solution[temp_col] == temp_row:
                    queen_conf[queen] = True
                    
            
            ## Goes in direction up left
                    
            temp_col = queen
            temp_row = solution[queen]
            while True:
                temp_col-=1
                temp_row+=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N or queen_conf[queen] == True:
                    break
                
                if solution[temp_col] == temp_row:
                    queen_conf[queen]= True
                
            ## Goes in direction down left
                    
            temp_col = queen
            temp_row = solution[queen]
            while True:
                temp_col-=1
                temp_row-=1
                                                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N or queen_conf[queen] == True:
                    break
                
                if solution[temp_col] == temp_row:
                    queen_conf[queen] = True'''
                    
            

        if all(value == False for value in queen_conf.values()):
            return solution, num_steps
            
        rand_conf_list = []
        for key, item in queen_conf.items():
            if item == True:
                rand_conf_list.append(key)
        
        random_conf = np.random.choice(rand_conf_list)        
        #print (solution)
        
        #Keep a score of the best move
        
        best_score = {}
        
        for move in range(N):
            best_score[move] = 0
            # if move == solution[random_conf]:
            #     continue
            
            for enemy_q in range(N):
                #if solution[enemy_q] == solution[random_conf]:
                #    continue # Does this make sense?
                '''if solution[random_conf] == move:
                    continue'''
                
                if move == solution[enemy_q]:
                    #increment the total conflicts
                    #if enemy_q != random_conf:
                    best_score[move]+=1
                
                    
                if(random_conf > enemy_q):
                    if (move - solution[enemy_q] == random_conf - enemy_q):
                        best_score[move]+=1
                    elif (solution[enemy_q] - move == random_conf - enemy_q):
                        best_score[move]+=1
                if (random_conf < enemy_q):
                    if (move - solution[enemy_q] == enemy_q - random_conf):
                        best_score[move] +=1
                    elif (solution[enemy_q] - move == enemy_q - random_conf):
                        best_score[move] +=1
                
                    
                    
                    
                    '''if (move - solution[enemy_q] == solution[move] - enemy_q):
                        best_score[move]+=1
                    if (solution[enemy_q] - move == solution[move] - enemy_q):
                        best_score[move]+=1
                    if (move - solution[enemy_q] == enemy_q - solution[move]):
                        best_score[move] +=1
                    if (solution[enemy_q] - move == enemy_q - solution[move]):
                        best_score[move] +=1'''
                
            ## Goes in direction up right\
            
            '''temp_col = random_conf
            temp_row = move
            while True:
                temp_col+=1
                temp_row+=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N:
                    break
                
                if solution[temp_col] == temp_row:
                    best_score[move]+=1
                    
            ## Goes in direction down right
                    
            temp_col = random_conf
            temp_row = move
            
            while True:
                temp_col+=1
                temp_row-=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N:
                    break
                
                if solution[temp_col] == temp_row:
                    best_score[move]+=1
            
            ## Goes in direction up left
                
            temp_col = random_conf
            temp_row = move
            while True:
                temp_col-=1
                temp_row+=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N:
                    break
                
                if solution[temp_col] == temp_row:
                    best_score[move]+=1
                    
            ## Goes in direction down left
                    
            temp_col = random_conf
            temp_row = move
            while True:
                temp_col-=1
                temp_row-=1
                
                if temp_col < 0 or temp_col >= N or temp_row < 0 or temp_row >= N:
                    break
                
                if solution[temp_col] == temp_row:
                    best_score[move]+=1'''
                
        best_score = dict(sorted(best_score.items(), key=lambda item: item[1]))
        
        min_c = N+1
        best_pos = []
            
        temp = min(best_score.values())
        mins = [key for key in best_score if best_score[key] == temp]
        
        poten_move = np.random.randint(len(mins))
        
        solution[random_conf] = mins[poten_move]

    #print(solution)
    solution =[]
    num_steps = -1
    return solution, num_steps


if __name__ == '__main__':
    # Test your code here!

    N = 100
    t_ns = 0
    # Use this after implementing initialize_greedy_n_queens.py
    #for i in range(100):
    
    assignment_initial = initialize_greedy_n_queens(N)
    # Plot the initial greedy assignment
    #plot_n_queens_solution(assignment_initial)

    assignment_solved, n_steps = min_conflicts_n_queens(assignment_initial)
    #    t_ns+=n_steps
    
   # print(t_ns/100)
    # Plot the solution produced by your algorithm
    #plot_n_queens_solution(assignment_solved)
    print(n_steps)
