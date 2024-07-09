import sys


def find_substring_existance(haystack, needle):
    n, m = len(haystack), len(needle)
    if m > n:
        return -1
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i


def main():
    input = sys.stdin.read
    data1, data2 = input().strip().split(',', 1)
    haystack = data1[12:-1]
    needle = data2[11:-1]

    index = find_substring_existance(haystack, needle)
    print(index)


if __name__ == "__main__":
    main()


'''
01. Time Complexity: O(n * m), where n is the length of the haystack and m is the length of the needle. This is because, 
    in the worst case, we need to check each position in the haystack.
02. Space Complexity: O(1) as we are not using any additional data structures that grow with the input size.
'''