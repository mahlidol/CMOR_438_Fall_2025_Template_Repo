# src/rice_ml/distances.py
import numpy as np
from typing import Sequence
import math

def euclidean_distance(a: Sequence[float], b: Sequence[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def _validate_vectors(a: Sequence, b: Sequence):
    if len(a) != len(b):
        raise ValueError("Input vectors must be the same length")
    return np.array(a), np.array(b)

def manhattan_distance(a: Sequence, b: Sequence) -> float:
    a, b = _validate_vectors(a, b)
    return np.sum(np.abs(a - b))
