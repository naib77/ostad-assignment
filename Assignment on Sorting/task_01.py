import sys
import random


def quickselect(nums, left, right, k):
    if left <= right:
        pivot_index = random.randint(left, right)
        pivot_index = partition(nums, left, right, pivot_index)

        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index < k:
            return quickselect(nums, pivot_index + 1, right, k)
        else:
            return quickselect(nums, left, pivot_index - 1, k)

    return None


def partition(nums, left, right, pivot_index):
    pivot_value = nums[pivot_index]

    # Move pivot to the end
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

    store_index = left
    for i in range(left, right):
        if nums[i] < pivot_value:  # '<' for ascending order, to get kth largest
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1

    # Move pivot to its final place
    nums[right], nums[store_index] = nums[store_index], nums[right]

    return store_index


def find_kth_largest(nums, k):
    # We need the (len(nums) - k)th smallest element in 0-indexed array
    return quickselect(nums, 0, len(nums) - 1, len(nums) - k)


def main():
    input_data = sys.stdin.read().strip()

    # Extract the nums array and k from the input
    nums_str = input_data[input_data.find('['):input_data.find(']') + 1]
    nums = eval(nums_str)
    k_str = input_data[input_data.find('k = ') + 4:].strip()
    k = int(k_str)

    print(find_kth_largest(nums, k))


if __name__ == "__main__":
    main()


'''
Time Complexity:
    In the average case, Quickselect has a time complexity of O(n), but since we aim for O(n log n) to fit the worst-case scenario, this modified version with random pivoting is efficient.

Space Complexity:
    The space complexity is O(1) apart from the recursive stack, which is minimal.
'''