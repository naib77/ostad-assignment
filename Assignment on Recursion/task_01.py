import sys


def is_palindrome_recursive(s, start, end):
    # Base case: If the string is empty or has one character, it is a palindrome
    if start >= end:
        return True

    # Recursive case: If the first and last characters match, check the substring
    if s[start] == s[end]:
        return is_palindrome_recursive(s, start + 1, end - 1)
    else:
        return False


def is_palindrome(s):
    return is_palindrome_recursive(s, 0, len(s) - 1)


def main():
    input = sys.stdin.read().strip()  # Read input from the console and strip any whitespace
    result = is_palindrome(input)  # Check if the input string is a palindrome
    print(result)  # Print the result


if __name__ == "__main__":
    main()
