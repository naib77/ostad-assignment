import sys


def multiply_with_add_and_minus(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return b + multiply_with_add_and_minus(a - 1, b)


def main():
    input = sys.stdin.read  # Read input from the console and strip any whitespace
    data = input().strip().split(',', 1)  # Split the input data into two parts with the first '='
    # Extract the first part of the data and remove the prefix 'a = ' and the suffix ''
    a = int(data[0][4:])
    b = int(data[1][4:])  # Extract the second part of the data and remove the prefix 'b = ' and the suffix ''

    f = multiply_with_add_and_minus(a, b)  # Print the result
    print(f)


if __name__ == "__main__":
    main()

    '''
    

    Time Complexity: O(n)
    Space Complexity: O(n)
    
     a = 4, b = 5
     5+ m(3,5)
     5+5+ m(2,5)
     5+5+5+ m(1,5)
    '''
