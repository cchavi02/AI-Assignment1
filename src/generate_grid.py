import random

def generate_grid(grid_size, output_file, with_cycles=False):
    """
    Generates a grid of specified size with values between 0 (unpassable) and 5 (cost).
    If with_cycles is True, the grid will have guaranteed cycles by creating multiple paths.
    """
    grid = []
    # Create the initial grid with random values between 0-5
    for i in range(grid_size):
        row = [random.randint(1, 5) for _ in range(grid_size)]
        grid.append(row)

    # Add some obstacles (value 0) randomly
    num_obstacles = random.randint(grid_size // 4, grid_size // 2) # Random number of obstacles

    for _ in range(num_obstacles):
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        grid[x][y] = 0 # Mark cell as unpassable

    # Introduce cycles if requested
    if with_cycles:
    # Introduce paths between certain rows and columns to create cycles

        for i in range(1, grid_size - 1):
            grid[i][i + 1] = grid[i + 1][i] = random.randint(1, 5) # Creating a bidirectional path

            # Create an extra bidirectional link between nonadjacent cells to ensure cycles

            if i < grid_size - 2:
                grid[i][i + 2] = grid[i + 2][i] = random.randint(1, 5)


    # Specify the output file path in the parent directory
    output_file = f"../grids/{output_file}"


    # Save the grid to a text file
    with open(output_file, "w") as f:
        for row in grid:
            f.write(" ".join(map(str, row)) + "\n")

    print(f"Grid of size {grid_size}x{grid_size} saved to {output_file}")

# Example usage:
if __name__ == "__main__":
    grid_size = int(input("Enter grid size: ")) # Input the grid size
    with_cycles = input("Do you want to include cycles? (yes/no): ").strip().lower() == 'yes'
    output_file = "generated_grid_with_cycles.txt" if with_cycles else "generated_grid.txt"
    generate_grid(grid_size, output_file, with_cycles)