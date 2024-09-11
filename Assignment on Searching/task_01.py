import sys
import ast


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids overflow

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


input_data = sys.stdin.read().strip()

input_data = input_data.replace('nums = ', '').replace('target = ', '')
nums_str, target_str = input_data.split(', ')
nums = ast.literal_eval(nums_str)
target = int(target_str)

result = search(nums, target)
print(result)
