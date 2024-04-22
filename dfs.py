from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
 
     
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
 
 
# Driver's code
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Depth First Traversal (starting from vertex 2)")
     
    # Function call
    g.DFS(2)
 
# This code is contributed by Neelam Yadav

# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
    
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
    
#     def DFSUtil(self, v, visited):
#         visited.add(v)
#         print(v, end=' ')
#         for neighbour in self.graph[v]:
#             if neighbour not in visited:
#                 self.DFSUtil(neighbour, visited)
    
#     def DFS(self, v):
#         visited = set()
#         self.DFSUtil(v, visited)

# if __name__ == "__main__":
#     g = Graph()
#     while True:
#         try:
#             u, v = map(int, input("Enter edge (u v), or type 'done' to finish: ").split())
#             g.addEdge(u, v)
#         except ValueError:
#             break
#     start_vertex = int(input("Enter the starting vertex for DFS traversal: "))

#     print("Following is Depth First Traversal (starting from vertex {})".format(start_vertex))
#     g.DFS(start_vertex)