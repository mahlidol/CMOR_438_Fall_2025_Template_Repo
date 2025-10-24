from rice_ml.distances import euclidean_distance
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

def test_euclidean_distance():
    assert euclidean_distance([0, 0], [3, 4]) == 5.0
