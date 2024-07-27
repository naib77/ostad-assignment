import sys


def is_palindrome(input, start, end):
    if start >= end:
        return True
    if input[start] == input[end]:
        return is_palindrome(input, start + 1, end - 1)
    else:
        return False


def main():
    input = sys.stdin.read().strip()[5:-1]  # Read input from the console and strip any whitespace
    result = is_palindrome(input, 0, len(input) - 1)  # Check if the input string is a palindrome
    print(result)  # Print the result


if __name__ == "__main__":
    main()

'''

    Time Complexity: O(n)
    Space Complexity: O(n)
    
    
    
    Example 1:
        Input: s = "madam"
        s1 = m, e5 = m
        s2 = a, e4 = a
        s3 = d, e3 = d

        Output: true
'''
