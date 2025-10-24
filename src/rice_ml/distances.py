# src/rice_ml/distances.py

def euclidean_distance(a, b):
    """Compute the Euclidean distance between two lists of numbers."""
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5
