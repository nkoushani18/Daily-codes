# Bit Manipulation Tricks in Python
# ===============================
#
# This script teaches various bit manipulation tricks and their usage in Python.
# Bit manipulation is a low-level operation that allows us to perform operations on individual bits of a number.

def bitwise_and(n1, n2):
    """
    Returns the result of the bitwise AND operation between two numbers.
    
    Parameters:
    n1 (int): The first number.
    n2 (int): The second number.
    
    Returns:
    int: The result of the bitwise AND operation.
    """
    # We use the '&' operator to perform the bitwise AND operation
    return n1 & n2

def bitwise_or(n1, n2):
    """
    Returns the result of the bitwise OR operation between two numbers.
    
    Parameters:
    n1 (int): The first number.
    n2 (int): The second number.
    
    Returns:
    int: The result of the bitwise OR operation.
    """
    # We use the '|' operator to perform the bitwise OR operation
    return n1 | n2

def bitwise_xor(n1, n2):
    """
    Returns the result of the bitwise XOR operation between two numbers.
    
    Parameters:
    n1 (int): The first number.
    n2 (int): The second number.
    
    Returns:
    int: The result of the bitwise XOR operation.
    """
    # We use the '^' operator to perform the bitwise XOR operation
    return n1 ^ n2

def left_shift(n, shift):
    """
    Shifts the bits of a number to the left by 'shift' positions.
    
    Parameters:
    n (int): The number to be shifted.
    shift (int): The number of positions to shift the bits.
    
    Returns:
    int: The result of shifting the bits.
    """
    # We use the << operator to perform the left shift operation
    return n << shift

def right_shift(n, shift):
    """
    Shifts the bits of a number to the right by 'shift' positions.
    
    Parameters:
    n (int): The number to be shifted.
    shift (int): The number of positions to shift the bits.
    
    Returns:
    int: The result of shifting the bits.
    """
    # We use the >> operator to perform the right shift operation
    return n >> shift

# Example usage:
if __name__ == "__main__":
    num1 = 5   # 00000101 in binary
    num2 = 3   # 00000011 in binary
    
    print("Bitwise AND:", bitwise_and(num1, num2))   # Output: 1 (00000001 in binary)
    print("Bitwise OR:", bitwise_or(num1, num2))     # Output: 7 (00000111 in binary)
    print("Bitwise XOR:", bitwise_xor(num1, num2))   # Output: 6 (00000110 in binary)
    
    num3 = 10  # 00001010 in binary
    
    shifted_num = left_shift(num3, 2)     # Shift bits of num3 to the left by 2 positions
    print("Left Shift:", shifted_num)      # Output: 40 (000001000 in binary)
    
    shifted_num = right_shift(shifted_num, 2)