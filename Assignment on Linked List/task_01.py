class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the current node's pointer
        prev = current  # Move pointers one position ahead
        current = next_node

        # 1st loop
            # current = 1
            # next_node = 2
            # prev = None
            # current.next = None
            # prev = 1
            # current = 2
        # 2nd loop
            # current = 2
            # next_node = 3
            # prev = 1
            # current.next = 1
            # prev = 2
            # current = 3
        # 3rd loop
            # current = 3
            # next_node = 4
            # prev = 2
            # current.next = 2
            # prev = 3
            # current = 4
        # 4th loop



        # Input: head = [1, 2, 3, 4, 5]
        # Output: [5, 4, 3, 2, 1]

    return prev  # prev will be the new head of the reversed list


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

    # Remove the "head = " part and extract the list of integers
    if input_data.startswith("head = "):
        input_list_str = input_data[len("head = "):].strip()
        if input_list_str == "[]":
            input_list = []
        else:
            input_list = list(map(int, input_list_str.strip("[]").split(',')))

    # Create linked list
    head = create_linked_list(input_list)

    # Reverse linked list
    reversed_head = reverse_linked_list(head)

    # Convert back to list to print
    output_list = linked_list_to_list(reversed_head)

    print(output_list)
