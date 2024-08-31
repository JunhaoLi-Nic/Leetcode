class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

def introduce_cycle(head, pos):
    if pos == -1:
        return head
    cycle_start = None
    current = head
    index = 0
    while current.next:
        if index == pos:
            cycle_start = current
        current = current.next
        index += 1
    current.next = cycle_start  # Creating a cycle


def hasCycle(head) -> bool:
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False

# Convert list to linked list
elements = [3, 2, 0, -4]
linked_list = create_linked_list(elements)

# Optionally introduce a cycle, for example back to the node at index 1
introduce_cycle(linked_list, 1)  # Remove or change index to test different scenarios

# Check if there is a cycle
print(hasCycle(linked_list))  # Should print True if there's a cycle, False otherwise
