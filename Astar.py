import heapq

# Function to reconstruct the path from start to goal node
def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0, current)  # Insert at the beginning to maintain order
    return total_path

# A* search algorithm implementation
def A_Star(start, goal, h, graph):
    openSet = [(h(start), start)]  # Priority queue with heuristic value and start node
    cameFrom = {}  # Dictionary to store the path
    
    # Initialization of gScore and fScore
    gScore = {node: float('inf') for node in graph}  # Initialize with infinity for all nodes
    gScore[start] = 0  # Cost from start to start is 0
    fScore = {node: float('inf') for node in graph}  # Initialize with infinity for all nodes
    fScore[start] = h(start)  # fScore = gScore + heuristic for start node
    
    while openSet:
        _, current = heapq.heappop(openSet)  # Get node with smallest fScore from openSet
        if current == goal:
            return reconstruct_path(cameFrom, current)  # Path found, reconstruct and return
        
        # Explore neighbors
        for neighbor in graph[current]:
            tentative_gScore = gScore[current] + graph[current][neighbor]  # Tentative gScore for neighbor
            if tentative_gScore < gScore[neighbor]:
                # Update scores and path if better path found
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + h(neighbor)  # Update fScore for neighbor
                heapq.heappush(openSet, (fScore[neighbor], neighbor))  # Add neighbor to openSet
    
    return "failure"  # No path found

# Main function to handle user input and algorithm execution
def main():
    graph = {}  # Initialize empty graph
    while True:
        # Input edges until user types 'done'
        edge = input("Enter edge in the format 'node1 node2 weight' (or type 'done' to finish): ").split()
        if edge[0] == 'done':
            break
        node1, node2, weight = edge
        weight = int(weight)
        if node1 not in graph:
            graph[node1] = {}  # Initialize empty dictionary for node1 if not already present
        if node2 not in graph:
            graph[node2] = {}  # Initialize empty dictionary for node2 if not already present
        graph[node1][node2] = weight  # Add edge from node1 to node2 with specified weight
        graph[node2][node1] = weight  # Add edge from node2 to node1 with specified weight
    
    start = input("Enter the start node: ")  # Input start node
    goal = input("Enter the goal node: ")  # Input goal node
    
    heuristic_values = {}  # Dictionary to store heuristic values for nodes
    for node in graph:
        heuristic_values[node] = int(input(f"Enter heuristic value for node {node}: "))  # Input heuristic values
    
    def heuristic(node):
        return heuristic_values[node]  # Heuristic function to estimate cost to goal
    
    path = A_Star(start, goal, heuristic, graph)  # Run A* algorithm
    print("Path:", path)  # Print the optimal path

if __name__ == "__main__":
    main()  # Start the program execution
