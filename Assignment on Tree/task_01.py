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


# Function to calculate the height of the binary tree.
def get_height(root):
    if not root:
        return 0
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return max(left_height, right_height) + 1


# Reading input from standard input
if __name__ == "__main__":
    input_data = sys.stdin.read().strip()

    # Strip out the `root =` part if it's present
    if input_data.startswith("root ="):
        input_data = input_data.replace("root =", "").strip()

    # Convert the list-like string to an actual list
    root_list = eval(input_data.replace("null", "None"))

    # Build the tree from the input list
    root = build_tree(root_list)

    # Output the height of the binary tree
    print(get_height(root))

'''
Time Complexity: O(n)
Space Complexity: O(h), where h is the height of the tree
'''