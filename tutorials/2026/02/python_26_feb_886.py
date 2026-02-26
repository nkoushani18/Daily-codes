# Monotonic Stack Implementation in Python

# Define a class to represent the monotonic stack
class MonotonicStack:
    def __init__(self):
        # Initialize an empty list to store elements
        self.stack = []

    # Method to push an element onto the stack
    def push(self, element):
        # If the stack is empty or the new element is greater than the top element,
        # push the element onto the stack
        if not self.stack or element >= self.stack[-1]:
            self.stack.append(element)
        # Otherwise, find the largest element in the stack and replace it with the new element
        else:
            self._find_largest(self.stack)
            self.stack.append(element)

    # Method to pop an element from the stack
    def pop(self):
        # If the stack is not empty, remove the top element
        if self.stack:
            return self.stack.pop()
        # If the stack is empty, return None
        else:
            return None

    # Helper method to find the largest element in the stack
    def _find_largest(self, stack):
        # Initialize the largest element with the top element of the stack
        largest = stack[-1]
        # Iterate through the stack from the top to the bottom
        for element in reversed(stack[:-1]):
            # If a larger element is found, update the largest element
            if element > largest:
                largest = element
        # Replace the top element with the largest element
        self.stack[-1] = largest

    # Method to check if the stack is empty
    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        return len(self.stack) == 0

# Example usage
if __name__ == "__main__":
    # Create a monotonic stack
    stack = MonotonicStack()

    # Push elements onto the stack
    stack.push(5)
    stack.push(10)
    stack.push(3)
    stack.push(8)

    # Print the stack
    print("Stack:", stack.stack)

    # Pop elements from the stack
    while not stack.is_empty():
        print("Popped:", stack.pop())

    # Print the final stack
    print("Final Stack:", stack.stack)