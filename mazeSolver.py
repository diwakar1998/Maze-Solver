"""
Modify the maze to see if it works
maze represented using 
"#"-for wall
" "-for path
"o"-for starting point
"""
maze=[]
maze.append(['#','#','#',' ','#'])
maze.append(['#',' ','o',' ','#'])
maze.append([' ',' ','#',' ','#'])
maze.append(['#',' ','#','#',' '])

mazeCord={}

#max values of (row,columns)-1 since list indices start form 0
#row value
p=3
#column value
q=4

#just for printing maze
def printMaze(maze):
    #prints normal maze
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j],end=" ")
        print()
    #prints maze with coords
    # for i in range(len(maze)):
    #     for j in range(len(maze[i])):
    #         print(i,j,maze[i][j],end="  ")
    #     print()

#checks if the starting point is at an edge
def edgeCheck(coord):
    if(coord[1]>q):
        return True
    if(coord[1]<0):
        return True
    if(coord[0]>p):
        return True
    if(coord[0]<0):
        return True
    else:
        return False

#check method takes and give values at top,bottom,right,left tiles  
def check(coOrd,searchVal):
    upCord = coOrd[0]-1,coOrd[1]
    downCord = coOrd[0]+1,coOrd[1]
    rightCord = coOrd[0],coOrd[1]+1
    leftCord = coOrd[0],coOrd[1]-1

    if(not edgeCheck(upCord) and searchVal == "U"):
        val = mazeCord[upCord]
        return val,upCord
    
    if(not edgeCheck(downCord) and searchVal == "D"):
        val = mazeCord[downCord]
        return val,downCord
    
    if(not edgeCheck(rightCord) and searchVal == "L"):    
        val = mazeCord[rightCord]
        return val,rightCord

    if(not edgeCheck(leftCord) and searchVal == "R"):
        val = mazeCord[leftCord]
        return val,leftCord

    return "i",(-1,-1)

#another edge checker 
def simpleCheck(coOrd):
    upCord = coOrd[0]-1,coOrd[1]
    downCord = coOrd[0]+1,coOrd[1]
    rightCord = coOrd[0],coOrd[1]+1
    leftCord = coOrd[0],coOrd[1]-1

    if(edgeCheck(upCord)):
        return True
    if(edgeCheck(downCord)):
        return True
    if(edgeCheck(leftCord)):
        return True
    if(edgeCheck(rightCord)):
        return True
    else:
        return False

#backTracking algorithm
def backTrackAlg(destCords):
    paths=[]
    for value in destCords:
        #some high value initialized into the smallest variable
        #temp list for storing current path to starting point
        temp = []
        temp.append(value)
        #loops untill the origin found
        while(value != startCord):
            #tries the code and works only for destcords that are connected to the starting point through a path
            try:
                value = backTrack[value]
                value = value
                temp.append(value)
            #removes the invlaid destcords which is not connected to the path via all four directions
            except:
                temp.remove(value)           
                break
        if(len(temp)>0):
            paths.append(temp)
    #returns all the paths to the edges  
    return paths

def messageformatter(path):
    #clear the message from x
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if(maze[i][j] == "x"):
                maze[i][j] = " "
            
    message = ""
    while(len(path) != 0):
        popcord = path.pop()
        message = message+ str(popcord)+ "->"
        if(maze[int(popcord[0])][int(popcord[1])] != "o"):
            maze[int(popcord[0])][int(popcord[1])] = "x"
        if(len(path)==0):
            message = message[:-2]
    return maze,message

#CODE STARTS HERE
#variables initialization
startCord = (0,0)
#destination co-ordinates
destCords = []

#assigns co-ordinates to the maze
for i in range(len(maze)):
    for j in range(len(maze[i])):
        mazeCord[(i,j)]=maze[i][j]
        if(maze[i][j] == "o"):
            startCord=(i,j)
        #destcords obtained here
        if(simpleCheck((i,j)) and maze[i][j] == " "):
                destCords.append((i,j))

#check if the starting point is at edge
if(simpleCheck(startCord)):
    print("u are at the boundary of the floor")
    exit()

#required variables
frontier=[]
visited=[]
current = (0,0)
backTrack = {}

####BFS algorithm
#here all the path are searched and the previous cell of each and every cell is recorded
#step1
frontier.append(startCord)
#step2
while(len(frontier) > 0):
    #step3
    current=frontier[0]
    #checking steps
    #step4 checks cell up
    value,cordCheck= check(current,"U")
    if((value == " ") and (cordCheck not in visited)):
        frontier.append(cordCheck)
        #previous values of the current cell is added into the dictionary
        backTrack[cordCheck]=current
    #step5 checks cell down
    value,cordCheck= check(current,"D")
    if((value == " ") and (cordCheck not in visited))  :
        frontier.append(cordCheck)
        backTrack[cordCheck]=current
    #step6 checks cell left
    value,cordCheck= check(current,"L")
    if(value == " ") and (cordCheck not in visited) :
        frontier.append(cordCheck)
        backTrack[cordCheck]=current
    #step7 checks cell right
    value,cordCheck= check(current,"R")
    if(value == " ") and (cordCheck not in visited):
        frontier.append(cordCheck)
        backTrack[cordCheck]=current
    #step 8 appends current cell to visited this can be used to validate if all the valid paths are covered
    visited.append(current)
    #since the cell is explored we pop it from the frontier queue
    frontier.pop(0)



steps=0
#calls the backtrack method and send the destination co-ordinate to the method
paths = backTrackAlg(destCords)
smallest =len(paths[0])

smallestpaths = []
#finds the smallest length of path
for each in paths:
    if(len(each) <= smallest):
        smallest = len(each)
#selects all the possible paths of smallest length
for each in paths:
    if(len(each) <= smallest):
        smallestpaths.append(each)

print("Maze unsolved  ")
printMaze(maze)

##formats the message and prints the message accordin to all the available paths
for path in smallestpaths:
    solvedMaze,message = messageformatter(path)
    print("Solved maze  ")
    printMaze(solvedMaze)
    print("the smallest path available to reach the boundary is", message,"and steps required is ",smallest-1)


input("press enter to quit")
