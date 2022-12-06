#definition of the graph and its cost (G_cost)for every node
graph={

    'A':[('B',6),('F',3)],
    'B':[('C',3),('D',2)],
    'F':[('G',1),('H',7)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 8)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
    'E':[('G',5)],
    'J': []

}
#dicthionary for H_cost
H_table={
    'A':10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0

}
#function to find total cost in every path and return that cost and last node ended by
def calc_path_cost(path):
    g_cost=0
    for(node ,cost) in path :
        g_cost+=cost
    last_node =path[-1][0]
    h_cost =H_table[last_node]
    f_cost=g_cost+h_cost
    return f_cost, last_node

def star_search(graph,start,goal):
    visited =[] #initialized empty
    queue=[[(start,0)]]#initialized with fist (start_node)node
    while queue:#while list is not empty
        queue.sort(key=calc_path_cost)#sorting by total cost if equal sort by alphaitically(nodes name)
        path =queue.pop(0)#choose least cost add to path
        node =path[-1][0]#path[-1]---->last element in path (node and cost) , path[-1][0]---->node on graph only 'C' for example
        if node in visited:
            continue #if node in visited skip it and go to next node
        visited.append(node)#if node not in visited add it to visited
        if node ==goal:
            return path #we find the goal then return path
        else :
            new_nodes=graph.get(node,[])# get adjacent nodes if we don't find goal
            for (node2,cost) in new_nodes:#looping on adjacent nodes to add it to the queue
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)

# Driver Code
print("Following is the A* Search")
star_result=star_search(graph, 'A', 'J')# function calling
print(star_result)
print(calc_path_cost(star_result)[0])