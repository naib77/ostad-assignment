import sys


def two_sum(nums, target):
    nums_with_indices = [(num, index) for index, num in enumerate(nums)]
    nums_with_indices.sort()
    left, right = 0, len(nums_with_indices) - 1
    while left < right:
        current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
        if current_sum == target:
            return [nums_with_indices[left][1], nums_with_indices[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1


def main():
    input = sys.stdin.read
    data = input().strip()
    num_list = list(map(int, data[data.index('[') + 1:data.index(']')].split(',')))
    target = int(data[data.index('target = ') + 9:])
    result = two_sum(num_list, target)
    print(result)


if __name__ == "__main__":
    main()

# Total Time Complexity: O(NlogN)
# Total Space Complexity: O(N)
