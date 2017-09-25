class Node(object):

    def __init__(self, num):
        self.num = num
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class Graph(object):

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.num] = node

    def dfs(self, start, target):
        start = self.nodes[start]
        target = self.nodes[target]
        visited = {}
        return self.dfs_helper(start, target, visited)

    def dfs_helper(self, start, target, visited):
        print(start.num)
        if start in visited:
            return False
        visited[start] = True
        if start is target:
            return True
        for child in start.children:
            if self.dfs_helper(child, target, visited):
                return True
        return False


# Set up test instances
g = Graph()
n = []
num_nodes = 4

# Create an array of nodes
for i in range(0, num_nodes):
    n[i] = Node(i)

# Create relationships between the nodes
n[1].add_child(n[2])
n[2].add_child(n[3])
n[3].add_child(n[4])

# Populate graph with nodes from above
for i in range(0, num_nodes):
    g.add_node(n[i])

g.dfs(1, 10)
