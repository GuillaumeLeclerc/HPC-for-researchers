import numpy as np

def initialize_matrix(n = 10000):
    matrix = np.random.randn((n, n))
    return matrix

def compute_sum_A(matrix):
    return matrix.sum(0).sum(0)

def compute_sum_B(matrix):
    return matrix.sum(1).sum(0)
