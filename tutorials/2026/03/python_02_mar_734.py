# Monotonic Stack
# A monotonic stack is a data structure that always maintains the order of the elements
# in a way that the top element is always greater than or equal to the bottom elements

class MonotonicStack:
    def __init__(self):
        self.stack = []

    # Push a new element into the stack
    def push(self, num):
        # Create a new stack to store the negative of the number
        neg_stack = []
        while self.stack and self.stack[-1] > -num:
            # Pop the top element from the stack and push its negative
            neg_stack.append(-self.stack.pop())
        # Push the negative of the number into the new stack
        neg_stack.append(-num)
        # Push the new stack into the original stack
        while neg_stack:
            self.stack.append(neg_stack.pop())

    # Pop the top element from the stack
    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack.pop()

    # Check if the stack is empty
    def is_empty(self):
        return not self.stack

# Example usage
if __name__ == "__main__":
    stack = MonotonicStack()
    print("Is stack empty?", stack.is_empty())
    stack.push(5)
    stack.push(2)
    stack.push(8)
    print("Popped element:", stack.pop())
    print("Is stack empty?", stack.is_empty())