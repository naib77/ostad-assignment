import sys


def is_valid_brackets(s):
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    # Functional approach using a for loop
    for char in s:
        if char in bracket_map:  # If it's a closing bracket
            # Pop the topmost element from the stack if it exists, otherwise use a dummy value '#'
            top_element = stack.pop() if stack else '#'

            # If the mapped value of the closing bracket does not match the popped value, return False
            if bracket_map[char] != top_element:
                return False
        else:  # If it's an opening bracket, push onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were closed properly
    return not stack


# Read input
s = sys.stdin.read().strip()

# Output the result
print(is_valid_brackets(s))

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''