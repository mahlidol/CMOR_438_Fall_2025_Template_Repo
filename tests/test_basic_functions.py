
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from rice_ml.basic_functions import add

def test_add():
    assert add(2, 3) == 5
