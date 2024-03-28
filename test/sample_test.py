import sys

# adding src to the system path
# sys.path.insert(0, '/home/circleci/circleci-python/src')

sys.path.insert(0, "C:\\Personal\\Vinodh\\Projects\\PythonProjects\\Workspace\\UITestFramework\\src")
from sample import inc

def test_answer():
    print("abc")
    assert inc(3) == 4


if __name__ =='__main__':
    test_answer()
