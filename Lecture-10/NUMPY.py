import NUMPY as np
random_matrix = np.random.randint(1, 11, size =(3, 3))
print("random 3x3 matrix:\n",random_matrix)

matrix_sum = np.sum(random_matrix)
print(f"\nsum of all elements:{matrix_sum}")

matrix_mean = np.mean(random_matrix)
print(f"\nmean of the matrix:{matrix_mean:2.2f}")

transposed_matrix = np.transposed(random_matrix)
print("\ntransposed matrix:\n", transposed_matrix)