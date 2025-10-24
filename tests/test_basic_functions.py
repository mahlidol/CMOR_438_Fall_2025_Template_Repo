import sys
import os

# ⬅️ This line adds your `src/` folder to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# ⬅️ This import ONLY works after the sys.path fix above
from rice_ml.basic_functions import add

def test_add():
    assert add(2, 3) == 5
