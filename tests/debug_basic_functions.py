import sys
import os

# Add the src/ folder to the path manually
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from rice_ml.basic_functions import add

def test_add():
    assert add(2, 3) == 5

