import numpy as np

def initialize_array(n = 1000000):
    result = []
    for i in range(n):
        result.append(np.sin(i))
    return result
        
def compute_norm(array):
    return np.linalg.norm(array)

if __name__ == '__main__':
    print(compute_norm(initialize_array()))

