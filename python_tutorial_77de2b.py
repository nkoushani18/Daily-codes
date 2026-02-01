# DNA Sequence Simulator and Analyzer

# Learning Objective:
# This tutorial will teach you how to simulate and analyze simple DNA sequences in Python.
# We will focus on understanding basic DNA properties like length, base composition, and GC content.
# This is a fundamental concept in bioinformatics and computational biology.

# --- Core Concepts ---

# DNA is composed of four bases: Adenine (A), Guanine (G), Cytosine (C), and Thymine (T).
# These bases pair up in specific ways: A with T, and G with C.
# A DNA sequence is a string of these bases.

# --- Helper Functions ---

def generate_random_dna(length):
    """
    Generates a random DNA sequence of a specified length.

    Args:
        length (int): The desired length of the DNA sequence.

    Returns:
        str: A randomly generated DNA sequence.

    This function simulates the random arrangement of DNA bases.
    We use `random.choice` to pick one of the valid bases ('A', 'G', 'C', 'T')
    repeatedly until the desired length is reached.
    """
    import random # Import the random module to use its functions
    bases = ['A', 'G', 'C', 'T'] # Define the possible DNA bases
    dna_sequence = ''.join(random.choice(bases) for _ in range(length)) # Construct the sequence
    return dna_sequence

def is_valid_dna(sequence):
    """
    Checks if a given string is a valid DNA sequence (contains only A, G, C, T).

    Args:
        sequence (str): The string to check.

    Returns:
        bool: True if the sequence is valid DNA, False otherwise.

    This function ensures that our analysis functions only operate on
    legitimate DNA sequences. It iterates through each character and
    checks if it's one of the allowed bases.
    """
    valid_bases = set('AGCT') # Using a set for efficient membership checking
    for base in sequence:
        if base not in valid_bases:
            return False
    return True

# --- Analysis Functions ---

def get_sequence_length(dna_sequence):
    """
    Calculates the length of a DNA sequence.

    Args:
        dna_sequence (str): The input DNA sequence.

    Returns:
        int: The length of the sequence.

    The length of a DNA sequence is simply the number of bases it contains.
    Python's built-in `len()` function is perfect for this.
    """
    if not is_valid_dna(dna_sequence):
        raise ValueError("Input is not a valid DNA sequence.")
    return len(dna_sequence)

def get_base_composition(dna_sequence):
    """
    Calculates the percentage of each base (A, G, C, T) in a DNA sequence.

    Args:
        dna_sequence (str): The input DNA sequence.

    Returns:
        dict: A dictionary where keys are bases and values are their percentages.

    This function helps us understand the distribution of bases within a sequence.
    We count occurrences of each base and then calculate their proportion
    relative to the total length.
    """
    if not is_valid_dna(dna_sequence):
        raise ValueError("Input is not a valid DNA sequence.")

    length = len(dna_sequence)
    if length == 0: # Handle empty sequences to avoid division by zero
        return {'A': 0.0, 'G': 0.0, 'C': 0.0, 'T': 0.0}

    base_counts = {base: dna_sequence.count(base) for base in 'AGCT'} # Efficiently count bases

    composition = {base: (count / length) * 100 for base, count in base_counts.items()} # Calculate percentages
    return composition

def get_gc_content(dna_sequence):
    """
    Calculates the GC content (percentage of G and C bases) in a DNA sequence.

    Args:
        dna_sequence (str): The input DNA sequence.

    Returns:
        float: The GC content as a percentage.

    GC content is an important property as G-C bonds are stronger than A-T bonds,
    affecting DNA stability and melting temperature.
    We sum the counts of G and C and divide by the total length.
    """
    if not is_valid_dna(dna_sequence):
        raise ValueError("Input is not a valid DNA sequence.")

    length = len(dna_sequence)
    if length == 0: # Handle empty sequences
        return 0.0

    gc_bases = dna_sequence.count('G') + dna_sequence.count('C') # Count G and C bases
    gc_percentage = (gc_bases / length) * 100 # Calculate percentage
    return gc_percentage

# --- Example Usage ---

if __name__ == "__main__":
    # This block runs only when the script is executed directly (not imported as a module)

    print("--- DNA Sequence Simulation and Analysis ---")

    # 1. Generate a random DNA sequence
    sequence_length = 50
    my_dna = generate_random_dna(sequence_length)
    print(f"\nGenerated DNA sequence ({sequence_length} bp):")
    print(my_dna)

    # 2. Analyze the generated sequence
    print("\n--- Analysis Results ---")

    # Get the length
    length_of_my_dna = get_sequence_length(my_dna)
    print(f"Length: {length_of_my_dna} base pairs")

    # Get base composition
    composition = get_base_composition(my_dna)
    print("Base Composition:")
    for base, percentage in composition.items():
        print(f"  {base}: {percentage:.2f}%") # .2f formats to 2 decimal places

    # Get GC content
    gc_percentage = get_gc_content(my_dna)
    print(f"GC Content: {gc_percentage:.2f}%")

    # Example with a known sequence
    print("\n--- Analysis of a known sequence ---")
    known_sequence = "ATGCGTACGTACGTAGCTAGCTAGCATCGATCGATC"
    print(f"Known sequence: {known_sequence}")

    if is_valid_dna(known_sequence):
        print(f"Length: {get_sequence_length(known_sequence)} bp")
        composition = get_base_composition(known_sequence)
        print("Base Composition:")
        for base, percentage in composition.items():
            print(f"  {base}: {percentage:.2f}%")
        print(f"GC Content: {get_gc_content(known_sequence):.2f}%")
    else:
        print("The known sequence is not valid DNA.")

    # Example of invalid input handling
    print("\n--- Testing invalid input ---")
    invalid_sequence = "ATGCXYZ"
    try:
        get_sequence_length(invalid_sequence)
    except ValueError as e:
        print(f"Caught expected error for invalid sequence: {e}")