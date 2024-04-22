def minimax(node, depth, maximizingPlayer):
    if depth == 0 or node_is_terminal(node):
        return static_evaluation(node)

    if maximizingPlayer:
        maxEva = float('-inf')
        for child in generate_children(node):
            eva = minimax(child, depth - 1, False)
            maxEva = max(maxEva, eva)
        return maxEva
    else:
        minEva = float('inf')
        for child in generate_children(node):
            eva = minimax(child, depth - 1, True)
            minEva = min(minEva, eva)
        return minEva

def node_is_terminal(node):
    return node.depth == 0 

def static_evaluation(node):
    return node.value

def generate_children(node):
    return node.children

class Node:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth
        self.children = []

def build_tree(depth):
    value = int(input("Enter value for node: "))
    root = Node(value, depth)
    if depth > 0:
        num_children = int(input("Enter number of children for node: "))
        for _ in range(num_children):
            child = build_tree(depth - 1)
            root.children.append(child)
    return root

if __name__ == "__main__":
    depth = int(input("Enter the depth for Minimax algorithm: "))
    root = build_tree(depth)
    maximizingPlayer = True 
    result = minimax(root, depth, maximizingPlayer)
    print("Result of Minimax:", result)
