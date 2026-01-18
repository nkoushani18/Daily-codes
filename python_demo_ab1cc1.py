# Learning Objective:
# This tutorial demonstrates how to procedurally generate evolving abstract art
# using a genetic algorithm and Python's Pillow library. We will focus on
# evolving the parameters of simple shapes (like rectangles) to create visually
# interesting and unique artwork that changes over generations.

# Import necessary libraries
from PIL import Image, ImageDraw
import random

# --- Configuration ---
IMAGE_WIDTH = 800  # Width of the generated image
IMAGE_HEIGHT = 600 # Height of the generated image
NUM_INITIAL_SHAPES = 50 # Number of shapes in the initial population
NUM_GENERATIONS = 20  # How many times the art will evolve
MUTATION_RATE = 0.1   # Probability of a gene mutating
ELITISM_COUNT = 2     # Number of best artworks to carry over to the next generation

# --- Gene Structure (Defining our "DNA" for each artwork) ---
# Our "genes" will define the properties of shapes.
# For simplicity, we'll evolve parameters for rectangles:
# [x0, y0, x1, y1, fill_color_r, fill_color_g, fill_color_b, outline_color_r, outline_color_g, outline_color_b]
# Each element in the list represents a "gene".

def create_random_gene():
    """Creates a single random set of genes for a rectangle."""
    # Rectangle coordinates (x0, y0, x1, y1)
    x0 = random.randint(0, IMAGE_WIDTH)
    y0 = random.randint(0, IMAGE_HEIGHT)
    x1 = random.randint(x0, IMAGE_WIDTH) # Ensure x1 is greater than or equal to x0
    y1 = random.randint(y0, IMAGE_HEIGHT) # Ensure y1 is greater than or equal to y0

    # Fill color (RGB tuple)
    fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Outline color (RGB tuple)
    outline_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Combine all genes into a single list
    return [x0, y0, x1, y1] + list(fill_color) + list(outline_color)

# --- Fitness Function (How "good" is an artwork?) ---
# This is crucial for genetic algorithms. It tells us how to rank solutions.
# For abstract art, "good" is subjective. We'll create a simple, somewhat
# arbitrary fitness function to demonstrate the concept.
# A more complex function could analyze color contrast, shape distribution, etc.
def calculate_fitness(gene_set):
    """
    Calculates the "fitness" of a gene set. Higher is better.
    This is a placeholder; a real-world application might use more sophisticated metrics.
    Here, we'll favor artworks with more color variation and shapes spread out.
    """
    # We need to draw the image to evaluate it.
    img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), color="white")
    draw = ImageDraw.Draw(img)

    # Draw all shapes defined by the gene_set
    for i in range(0, len(gene_set), 10): # Iterate through each set of 10 genes (1 rectangle)
        rect_genes = gene_set[i : i + 10]
        x0, y0, x1, y1, r1, g1, b1, r2, g2, b2 = rect_genes
        fill_color = (r1, g1, b1)
        outline_color = (r2, g2, b2)
        draw.rectangle([x0, y0, x1, y1], fill=fill_color, outline=outline_color)

    # Fitness calculation:
    # 1. Color diversity (sum of squared differences between color channels)
    total_color_diff = 0
    all_pixels = list(img.getdata())
    unique_colors = set(all_pixels)

    # Simple measure of color diversity: more unique colors, higher fitness.
    color_diversity_score = len(unique_colors) * 5

    # 2. Area covered by shapes (more filled area might be seen as more "complete")
    # A more accurate way to do this would involve checking pixel values.
    # For this example, we'll approximate by summing the areas of the rectangles.
    total_shape_area = 0
    for i in range(0, len(gene_set), 10):
        rect_genes = gene_set[i : i + 10]
        x0, y0, x1, y1, _, _, _, _, _, _ = rect_genes
        area = abs(x1 - x0) * abs(y1 - y0)
        total_shape_area += area
    area_coverage_score = min(total_shape_area / (IMAGE_WIDTH * IMAGE_HEIGHT), 1.0) * 50 # Scale it down

    # Combine scores (these weights can be tweaked)
    fitness = color_diversity_score + area_coverage_score
    return fitness

# --- Genetic Operations ---

def create_initial_population(size):
    """Creates the first generation of random gene sets."""
    population = []
    for _ in range(size):
        # Each individual in the population is a list of genes for multiple shapes
        individual_genes = []
        num_shapes_in_individual = random.randint(10, 100) # Random number of shapes per artwork
        for _ in range(num_shapes_in_individual):
            individual_genes.extend(create_random_gene())
        population.append(individual_genes)
    return population

def select_parents(population, fitnesses):
    """Selects two parents from the population based on their fitness."""
    # We'll use tournament selection: pick a few random individuals and choose the best.
    tournament_size = 5
    selected_indices = random.sample(range(len(population)), tournament_size)
    best_index = selected_indices[0]
    for i in selected_indices[1:]:
        if fitnesses[i] > fitnesses[best_index]:
            best_index = i
    parent1 = population[best_index]

    selected_indices = random.sample(range(len(population)), tournament_size)
    best_index = selected_indices[0]
    for i in selected_indices[1:]:
        if fitnesses[i] > fitnesses[best_index]:
            best_index = i
    parent2 = population[best_index]

    return parent1, parent2

def crossover(parent1, parent2):
    """Combines genes from two parents to create a child."""
    # Single-point crossover: pick a random point and swap gene segments.
    # We need to ensure we don't break the gene structure (10 genes per shape).
    # So, we'll crossover at the boundary of shape genes.
    
    # Determine the number of shapes in each parent
    num_shapes1 = len(parent1) // 10
    num_shapes2 = len(parent2) // 10
    
    # Create a child with a mix of shapes from parents
    child = []
    
    # Randomly decide how many shapes to take from parent1
    shapes_from_p1 = random.randint(0, num_shapes1)
    child.extend(parent1[:shapes_from_p1 * 10])
    
    # Take the remaining shapes from parent2
    shapes_from_p2 = random.randint(0, num_shapes2)
    child.extend(parent2[:shapes_from_p2 * 10])
    
    # Ensure child is not empty and has a reasonable number of shapes
    if not child:
        if random.random() < 0.5:
            child.extend(parent1[:10]) # Take at least one shape from parent1 if possible
        else:
            child.extend(parent2[:10]) # Or from parent2
    
    return child

def mutate(gene_set):
    """Randomly alters genes in a gene set."""
    mutated_gene_set = gene_set[:] # Create a copy
    for i in range(len(mutated_gene_set)):
        if random.random() < MUTATION_RATE:
            # Mutate a single gene value
            # We need to know which type of gene it is to apply appropriate mutation
            # Genes 0-3 are coordinates, 4-6 are fill color, 7-9 are outline color
            
            if i < 4: # Coordinates (x0, y0, x1, y1)
                # Add or subtract a small random value, clamping to image bounds
                change = random.randint(-50, 50)
                mutated_gene_set[i] += change
                if i < 2: # x0, y0
                    mutated_gene_set[i] = max(0, mutated_gene_set[i])
                    mutated_gene_set[i] = min(IMAGE_WIDTH if i == 0 else IMAGE_HEIGHT, mutated_gene_set[i])
                else: # x1, y1
                    mutated_gene_set[i] = max(0, mutated_gene_set[i])
                    mutated_gene_set[i] = min(IMAGE_WIDTH if i == 2 else IMAGE_HEIGHT, mutated_gene_set[i])
                    # Ensure x1 >= x0 and y1 >= y0
                    if i == 2: # x1
                        mutated_gene_set[i] = max(mutated_gene_set[0], mutated_gene_set[i])
                    elif i == 3: # y1
                        mutated_gene_set[i] = max(mutated_gene_set[1], mutated_gene_set[i])

            else: # Colors (0-255)
                mutated_gene_set[i] = random.randint(0, 255)
    return mutated_gene_set

# --- Evolution Loop ---

def evolve_population(population):
    """Evolves the population for one generation."""
    # 1. Evaluate fitness of each individual
    fitnesses = [calculate_fitness(individual) for individual in population]

    # 2. Create the next generation
    next_generation = []

    # Elitism: Keep the best individuals from the current generation
    sorted_population = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
    for i in range(ELITISM_COUNT):
        next_generation.append(sorted_population[i][0])

    # Fill the rest of the next generation with offspring
    while len(next_generation) < len(population):
        # 3. Select parents
        parent1, parent2 = select_parents(population, fitnesses)

        # 4. Crossover to create a child
        child = crossover(parent1, parent2)

        # 5. Mutate the child
        child = mutate(child)

        next_generation.append(child)

    return next_generation

# --- Rendering ---

def render_artwork(gene_set, filename):
    """Draws the artwork from a gene set to an image file."""
    img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), color="white")
    draw = ImageDraw.Draw(img)

    # Draw each shape defined by the gene set
    for i in range(0, len(gene_set), 10): # 10 genes per shape
        rect_genes = gene_set[i : i + 10]
        x0, y0, x1, y1, r1, g1, b1, r2, g2, b2 = rect_genes
        fill_color = (r1, g1, b1)
        outline_color = (r2, g2, b2)
        draw.rectangle([x0, y0, x1, y1], fill=fill_color, outline=outline_color)

    img.save(filename)
    print(f"Saved artwork to {filename}")

# --- Main Execution ---

if __name__ == "__main__":
    # 1. Create the initial population
    print("Creating initial population...")
    population = create_initial_population(NUM_INITIAL_SHAPES)

    # 2. Evolve the population over several generations
    for generation in range(NUM_GENERATIONS):
        print(f"Evolving Generation {generation + 1}/{NUM_GENERATIONS}...")
        population = evolve_population(population)

    # 3. After evolution, render the best artwork from the final population
    print("Evolution complete. Rendering final artwork.")
    final_fitnesses = [calculate_fitness(individual) for individual in population]
    best_artwork_index = final_fitnesses.index(max(final_fitnesses))
    best_gene_set = population[best_artwork_index]

    render_artwork(best_gene_set, "final_abstract_art.png")
    print("Done!")
```
# Example Usage:
# To run this code:
# 1. Make sure you have Python and Pillow installed (`pip install Pillow`).
# 2. Save the code as a Python file (e.g., `genetic_art.py`).
# 3. Run it from your terminal: `python genetic_art.py`
#
# This will generate an image named `final_abstract_art.png` in the same directory.
# You can experiment by changing the configuration constants at the top of the script:
# - `IMAGE_WIDTH`, `IMAGE_HEIGHT`: To change the canvas size.
# - `NUM_INITIAL_SHAPES`: To start with more or fewer elements.
# - `NUM_GENERATIONS`: To let the art evolve for longer or shorter periods.
# - `MUTATION_RATE`: To control how much the genes change.
# - `ELITISM_COUNT`: To preserve more or fewer of the best artworks.
#
# You can also modify the `calculate_fitness` function to influence what kind of art is considered "good".
# For instance, you could try to reward artworks with more circular shapes (if you were to add circles),
# or specific color palettes.
#
# This example focuses on evolving rectangles. To expand this, you could:
# - Introduce other shapes (circles, lines, polygons).
# - Evolve more complex properties like transparency, blending modes, or gradients.
# - Develop a more sophisticated fitness function that analyzes aesthetic qualities.