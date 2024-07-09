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


'''
haystack = "sadbutsad", needle = "sad"
'''

if __name__ == "__main__":
    main()
