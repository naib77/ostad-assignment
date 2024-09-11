import sys
import ast


def find_min(nums):
    left, right = 0, len(nums) - 1

    if nums[left] < nums[right]:
        return nums[left]

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


def main():
    # Reading input from stdin
    input_data = sys.stdin.read().strip()

    input_data = input_data.replace('nums = ', '')
    nums = ast.literal_eval(input_data)

    result = find_min(nums)

    print(result)


if __name__ == "__main__":
    main()
