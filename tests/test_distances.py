# tests/test_distances.py

from rice_ml.distances import euclidean_distance

def test_euclidean_distance():
    assert euclidean_distance([0, 0], [3, 4]) == 5.0
