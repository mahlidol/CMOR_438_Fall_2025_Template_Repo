import sys, os

print(">>> CURRENT WORKING DIRECTORY:", os.getcwd())
print(">>> SYS.PATH ENTRIES:")
for p in sys.path:
    print("   ", p)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
print(">>> ADDED SRC PATH:", os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
print(">>> SYS.PATH NOW:")
for p in sys.path:
    print("   ", p)

try:
    from rice_ml.basic_functions import add
    print(">>> IMPORT SUCCESSFUL!")
except Exception as e:
    print(">>> IMPORT FAILED:", e)
    raise e

def test_add():
    assert add(2, 3) == 5
