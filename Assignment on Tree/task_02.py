import sys
from collections import deque


# Define the TreeNode structure for the binary tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to build the tree from a list representation.
def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while i < len(nodes):
        current = queue.popleft()
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root


# Function to search for a node with a specific value in a binary search tree.
def search_bst(root, val):
    if root is None or root.val == val:
        return root

    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)


# Function to convert the subtree rooted at a given node into a list (for output).
def subtree_to_list(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values to match the output format
    while result and result[-1] is None:
        result.pop()

    return result


# Reading input from standard input
if __name__ == "__main__":
    input_data = sys.stdin.read().strip()

    # Split the input into the tree list and the value to search for.
    input_data = input_data.replace("tree =", "").strip()  # Remove `root =` part if present
    input_data = input_data.split(", val =")

    tree_list = eval(input_data[0].replace("null", "None").strip())  # Convert to list
    val = int(input_data[1].strip())  # Extract the value to search for

    # Build the tree from the input list
    root = build_tree(tree_list)

    # Search for the node with the specified value in the binary search tree
    found_node = search_bst(root, val)

    # Output the subtree rooted at the found node as a list
    output = subtree_to_list(found_node)

    print(output)
