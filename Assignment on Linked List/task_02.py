class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)  # Dummy node to simplify edge cases
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If any nodes remain in either list, append them
    current.next = list1 if list1 else list2

    return dummy.next  # The merged list starts after the dummy node


# Helper function to create a linked list from a list and return the head
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert a linked list back to a Python list for easy output
def linked_list_to_list(head: ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Example Usage
if __name__ == "__main__":
    import sys

    input_data = sys.stdin.read().strip()

    # Extract list1 and list2 from the input format
    list1_str = input_data.split("list1 = ")[1].split(", list2 = ")[0].strip()
    list2_str = input_data.split("list2 = ")[1].strip()

    # Convert the strings to lists of integers
    if list1_str == "[]":
        list1_values = []
    else:
        list1_values = list(map(int, list1_str.strip("[]").split(',')))

    if list2_str == "[]":
        list2_values = []
    else:
        list2_values = list(map(int, list2_str.strip("[]").split(',')))

    # Create linked lists
    list1_head = create_linked_list(list1_values)
    list2_head = create_linked_list(list2_values)

    # Merge the two sorted linked lists
    merged_head = merge_two_sorted_lists(list1_head, list2_head)

    # Convert the merged list back to a Python list and print
    output_list = linked_list_to_list(merged_head)

    print(output_list)

# Time Complexity: O(n + m)
#   -   The function iterates through all the nodes of both linked lists,
#       where n is the number of nodes in list1 and m is the number of nodes in list2.
# Space Complexity: O(1)
