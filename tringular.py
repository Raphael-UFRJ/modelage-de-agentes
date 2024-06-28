import random
def random_triangular(initial_size: int, min_val: float, max_val: float, mode: float) -> list:
    return [random.triangular(min_val, max_val, mode) for _ in range(initial_size)]


import math
def random_triangular_netlogo(initial_size: int, min_val: float, max_val: float, mode: float) -> list:
    rand_vals = []
    for _ in range(initial_size):
        rand = random.random()
        f = (mode - min_val) / (max_val - min_val)
        if rand <= f:
            values = min_val + math.sqrt(rand * (max_val - min_val) * (mode - min_val))
        else:
            values = max_val - math.sqrt((1 - rand) * (max_val - min_val) * (max_val - mode))
        rand_vals.append(values)    
    return rand_vals

def random_triang_netlogo(initial_size: int, min_val: float, max_val: float, mode: float) -> list:
    rand_vals = []
    for _ in range(initial_size):
        rand = random.random()
        f = (mode - min_val) / (max_val - min_val)
        if rand <= f:
            value = min_val + (rand * (max_val - min_val) * (mode - min_val)) ** 0.5
        else:
            value = (
                max_val - ((1 - rand) * (max_val - min_val) * (max_val - mode)) ** 0.5
            )
        rand_vals.append(value)
    return rand_vals


# Comparação entre NetLogo e Python
def compare_triangular():
    initial_size = 10
    min_val = 0.1
    max_val = 11
    mode = 10.8

    netlogo_results = random_triang_netlogo(initial_size, min_val, max_val, mode)
    python_results = random_triangular(initial_size, min_val, max_val, mode)

    python_results2 = random_triangular_netlogo(initial_size, min_val, max_val, mode)

    print(f"NetLogo Triangular: {netlogo_results}")
    print(f"Python Triangular: {python_results}")
    print(f"Python Triangular 2: {python_results2}")

# Executa a comparação
compare_triangular()
