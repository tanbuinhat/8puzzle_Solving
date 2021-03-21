import numpy as np
from utils import PriorityQueue

def generateSuccessors(puzzle):
    blank = np.where(puzzle == -1) # blank[0] is row, blank[1] is column
    successors = []
    # row - 1
    if blank[0] > 0:
        tmp_puzzle = np.copy(puzzle)
        tmp_puzzle[blank[0], blank[1]] = puzzle[blank[0]-1, blank[1]]
        tmp_puzzle[blank[0]-1, blank[1]] = -1
        successors.append(tmp_puzzle)
    # row + 1
    if blank[0] < x-1:
        tmp_puzzle = np.copy(puzzle)
        tmp_puzzle[blank[0], blank[1]] = puzzle[blank[0]+1, blank[1]]
        tmp_puzzle[blank[0]+1, blank[1]] = -1
        successors.append(tmp_puzzle)
    # column - 1
    if blank[1] > 0:
        tmp_puzzle = np.copy(puzzle)
        tmp_puzzle[blank[0], blank[1]] = puzzle[blank[0], blank[1]-1]
        tmp_puzzle[blank[0], blank[1]-1] = -1
        successors.append(tmp_puzzle)
    # column + 1
    if blank[1] < y-1:
        tmp_puzzle = np.copy(puzzle)
        tmp_puzzle[blank[0], blank[1]] = puzzle[blank[0], blank[1]+1]
        tmp_puzzle[blank[0], blank[1]+1] = -1
        successors.append(tmp_puzzle)
    return successors

def heuristic(start, goal): # manhanttan distance
    h = 0
    for i in range(1, 9):
        ih, iw = np.where(start==i)
        goah_h, goal_w = np.where(goal == i)
        h += abs(ih-goah_h) + abs(iw-goal_w)
    return h

def puzzleExistence(puzzle, closed_lst): # check goal
    for i in closed_lst:
        if heuristic(puzzle, i) == 0:
            return False
    return True
                       

f = open("input.txt", "r") # read file input

x, y = [int(i) for i in f.readline().strip().split(" ")]
puzzle = np.zeros((3,3))
for ih in range(x):
    iw = 0
    it = [i for i in f.readline().strip().split(" ")]
    for i in it:
        if i == "_":
            i = -1       
        puzzle[ih][iw] = int(i)
        iw += 1
f.close()
 

result = np.zeros((x,y))

f = open("goal.txt", "r") # read file output

for ih in range(x):
    iw = 0
    it = [i for i in f.readline().strip().split(" ")]
    for i in it:
        if i == "_":
            i = -1       
        result[ih][iw] = int(i)
        iw += 1
f.close()

current_h = heuristic(puzzle, result)
pq = PriorityQueue()
pq.push(puzzle, current_h)
closed_lst = []
cost = 0

print("Step by step to return result\n")    
def path_list(it): # this function is used to change -1 to _ again
    String = ""
    for i in it:
        for j in i:
            j = int(j)
            if j == -1:
                j = "_"     
            j = str(j) 
            String += j + " "
        String += "\n"    
    print(String)



while not pq.isEmpty():
    pri, it = pq.pop()   
    path_list(it)  
    if pri == 0:
        print("Cost path:",cost)
        break
    closed_lst.append(it)
    successors = generateSuccessors(it)
    for successor in successors:
        if puzzleExistence(successor, closed_lst) or pq.checkExistence(successor) == False:
            successor_h = heuristic(successor, result)
            pq.update(successor, successor_h)  
    cost += 1   





    
        
