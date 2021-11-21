#Prims algorithm conditions
# 1 All veritces must be connected forming a tree
# has Minimum sum of weights 

# Iniialize the minimum spanning tree with a vertex of your choice 
# find the edges connected to unvisted vertices and adjacent to visited vertices and compare their weights,
#picking the one with the least weight.

#Graph represented by adjacency matrix

P = [[0,10, 0,0,0,25,0],
     [10,0,28,0,0,0,0],
     [0,28,0,16,0,0,14],
     [0,0,16,0,12,0,0],
     [0,0,0,12,0,22,18],
     [25,0,0,0,22,0,24],
     [0,0,14,0,18,24,0]]

#Number of vertices in graph
vertices = 7

# A number that no weight on the graph is bigger than 
bignumber = 100

# This keeps track of the visited vertices using 
# the index as a representation of the visited vertex (0-6)
chosen_vertex = [0,0,0,0,0,0,0]

#Intializing the first vertex as visited 
chosen_vertex[0] = True

# Monitors the number of edges visited 
number_edge = 0

#
total_mindist = 0 


# printing for edge and weight
print("Weights in MST\n")

#The while loop ensures number of edges is atmost 1 less than the total number of vertices 
#ensuring that the code ends when all vertices have been visited
while (number_edge < vertices - 1): 
    
    minimum = bignumber
    
    # These represent the coordinates of the various points in the matrix .
    c = 0
    d = 0
    
    #This loop traverses through the adjacency matrix 
    # This checks if the vertex has been visited and 
    # if there is an edge between the unvisited vertex and visted vertex it
    # then checks to see if the value is the smallest weight and adds it to the MST 
    for a in range(vertices):
        if chosen_vertex[a]:
            for b in range(vertices):
                if ((not chosen_vertex[b]) and P[a][b]):
                    if minimum > P[a][b]:
                        minimum = P[a][b]
                        c = a
                        d = b
    #the MST weight is chosen 
    print(str(P[c][d]))

    #total minum distance 
    total_mindist = total_mindist + P[c][d]
    #the current vertex is updated as true 
    chosen_vertex[d] = True
    #the number of edges in the mst is increased by one.
    number_edge += 1

print("the total minimum distance is : \n" + str(total_mindist))    