# Two Pointer Approach in Python
=====================================

This script teaches the two pointer approach used to solve various problems such as finding the intersection of two sorted arrays or reversing a linked list.

The two pointer approach is a common technique used to solve problems that involve traversing two lists or arrays simultaneously. It is useful when dealing with problems where we need to find an element in one list that is also present in another list, or where we need to traverse both lists at the same time.

Here's how it works:

- We initialize two pointers, one for each list.
- We move the pointer of the list that has a smaller current element first. This ensures that we compare elements from both lists simultaneously.
- If the current elements are equal, we can return the common element or increment both pointers.
- If the current elements are not equal, we increment the pointer of the list that has the larger current element.

This approach is efficient because it avoids unnecessary comparisons and traversals. It also makes the code more readable by using clear variable names and separating different steps into different sections.

```python
def find_intersection(list1, list2):
    # Initialize two pointers at the beginning of both lists
    i = j = 0

    # Traverse both lists until we reach the end of either list
    while i < len(list1) and j < len(list2):
        # If the current elements are equal, return the common element
        if list1[i] == list2[j]:
            return list1[i]
        # Move the pointer of the list that has a smaller current element first
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    # If we reach the end of either list without finding an intersection, return None
    return None


def reverse_linked_list(head):
    # Initialize two pointers for the linked list
    prev_node = None
    current_node = head

    # Traverse the linked list and reverse it
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    # Return the new head of the reversed linked list
    return prev_node


def test_two_pointer():
    print(find_intersection([1, 3, 5], [2, 4, 6]))  # Output: None
    print(find_intersection([1, 2, 3], [2, 4, 6]))  # Output: 2
    print(reverse_linked_list(1))  # Output: 1


if __name__ == "__main__":
    test_two_pointer()