import sys
import pytest

# adding src to the system path
# sys.path.insert(0, '/home/circleci/circleci-python/src')

sys.path.insert(0, "C:\\Personal\\Vinodh\\Projects\\PythonProjects\\Workspace\\UITestFramework\\src")
from sample import inc

class TestSample:
    @pytest.mark.sanity
    def test_answer(self):
        print("abc")
        assert inc(3) == 4

    @pytest.mark.functional
    def test_product(self):
        print("abc")
        assert inc(3) == 4    

    @pytest.mark.regression
    def test_division(self):
        print("abc")
        assert inc(3) == 4 


