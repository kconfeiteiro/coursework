import numpy as np

def matrix_multiplication_work_memory_ratio(n, A, B):
    """
    Perform matrix multiplication on two n x n matrices, calculate the total number
    of floating-point operations and data volume, and return the work/memory ratio.

    Parameters:
    n (int): The dimension of the matrices (n x n).

    Returns:
    float: The work/memory ratio ρwm.
    """
    # Step 1: Generate two n x n matrices with random floating-point numbers


    # Step 2: Compute the product matrix C = A * B manually to count operations
    # Initialize the result matrix C
    C = np.zeros((n, n))
    total_operations = 0  # to count floating-point operations

    # Perform the matrix multiplication
    for i in range(n):
        for j in range(n):
            # Sum over k for the dot product of row i of A and column j of B
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
                total_operations += 1  # count each multiplication
            total_operations += (n - 1)  # count additions (n-1 per element in C)

    # Step 3: Calculate the data volume (3n^2 elements)
    total_data_volume = 3 * n**2

    # Step 4: Calculate the work/memory ratio
    rho_wm = total_operations / total_data_volume

    return rho_wm, C, total_operations, total_data_volume

# Example usage
n = 4  # Small example for clarity; you can increase n as needed
A = np.random.rand(n, n)
B = np.random.rand(n, n)

rho_wm, C, total_operations, total_data_volume = matrix_multiplication_work_memory_ratio(n, A, B)

# Display the matrices and results
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix C (Product of A and B):")
print(C)
print(f"\nTotal floating-point operations: {total_operations}")
print(f"Total data volume (memory): {total_data_volume} elements")
print(f"Work/Memory Ratio (ρwm) for n={n}: {rho_wm:.2f}")
