import sys


def remove_duplicates(s):
    stack = []

    # Functional approach using a loop
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


# Read input
s = sys.stdin.read().strip()

# Output the result
print(remove_duplicates(s))

'''
time complexity: O(n)
space complexity: O(n)
'''
