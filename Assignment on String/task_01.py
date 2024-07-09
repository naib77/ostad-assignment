import sys


def shuffle_the_string(given_string, arr):
    shuffuled = [''] * len(arr)
    for i, index in enumerate(arr):
        shuffuled[i] = given_string[index]

    return ''.join(shuffuled)


def main():
    input = sys.stdin.read
    # want to slice the input data into two parts with only  first comma
    data = input().strip().split(',', 1)
    given_string = data[0].strip()
    # Remove the prefix 's = "' and the suffix '"'
    if given_string.startswith('s = "') and given_string.endswith('"'):
        given_string = given_string[5:-1]
    given_arr_indecies = data[1].strip()
    arr = list(map(int, given_arr_indecies[given_arr_indecies.index('[') + 1:given_arr_indecies.index(']')].split(',')))

    shuffled_string = shuffle_the_string(given_string, arr)
    print(f"\"{shuffled_string}\"")


if __name__ == "__main__":
    main()
    """
    This is a multi-line string that spans
    multiple lines and can be used as a 
    multi-line comment.
    """
"""
1. Time Complexity: O(n), where n is the length of the string. This is because we are iterating through the string and
                     placing each character in its correct position. Space Complexity: O(n), where n is the length of the string. This
2. is because we are using an additional list to store the shuffled string.
"""
