import sys


def merge(nums1, m, nums2, n):
    # Start merging from the last elements of nums1 and nums2
    last = m + n - 1

    # Pointers for nums1 and nums2
    i = m - 1
    j = n - 1

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
        last -= 1

    # Fill nums1 with remaining elements from nums2 if any
    while j >= 0:
        nums1[last] = nums2[j]
        j -= 1
        last -= 1


def main():
    input_data = sys.stdin.read().strip()

    # Extract nums1, m, nums2, and n from the input
    nums1_str = input_data[input_data.find('['):input_data.find(']') + 1]
    nums1 = eval(nums1_str)

    m_str = input_data[input_data.find('m = ') + 4:].split(',')[0]
    m = int(m_str)

    nums2_str = input_data[input_data.rfind('['):input_data.rfind(']') + 1]
    nums2 = eval(nums2_str)

    n_str = input_data[input_data.find('n = ') + 4:].strip()
    n = int(n_str)

    merge(nums1, m, nums2, n)

    # Output the merged array
    print(nums1)


if __name__ == "__main__":
    main()

'''
Time Complexity: 
        O(m + n), where m and n are the lengths of nums1 and nums2 respectively.
         We iterate through each element exactly once.
Space Complexity:
        O(1), as we are not using any extra space and are modifying nums1 in place.
'''