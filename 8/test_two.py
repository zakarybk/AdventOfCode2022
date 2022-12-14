from unittest import TestCase
import numpy as np


from two import count_visible_in_forest, txt_to_forest

from two import (
    trees_blocking_top,
    trees_blocking_bottom,
    trees_blocking_left,
    trees_blocking_right
)

DEMO = txt_to_forest("""30373
25512
65332
33549
35390""")

class TestDemo(TestCase):


    def test_demo(self):
        assert count_visible_in_forest(DEMO) == 8


    def test_top(self):
        assert trees_blocking_top(2,3,DEMO) == 2


    def test_left(self):
        assert trees_blocking_left(2,3,DEMO) == 2


    def test_down(self):
        assert trees_blocking_bottom(2,3,DEMO) == 1


    def test_right(self):
        assert trees_blocking_right(2,3,DEMO) == 2