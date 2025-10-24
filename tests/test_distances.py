# tests/test_distances.py

from rice_ml.distances import euclidean_distance
import numpy as np
from rice_ml.distances import manhattan_distance

def test_manhattan_distance_basic():
    assert manhattan_distance([1, 2, 3], [4, 5, 6]) == 9.0
    assert manhattan_distance(np.array([1, 1]), np.array([1, 1])) == 0.0

def test_euclidean_distance():
    assert euclidean_distance([0, 0], [3, 4]) == 5.0
