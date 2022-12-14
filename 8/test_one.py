import numpy as np
from unittest import TestCase


from one import count_visible, count_visible_in_forest, txt_to_forest

from one import (
    is_visisble_from_top,
    is_visisble_from_bottom,
    is_visisble_from_left,
    is_visisble_from_right
)


DEMO = """30373
25512
65332
33549
35390"""


class TestEdgesVisible(TestCase):


    def setUp(self) -> None:
        self.forest = np.array(
            [[0,1,0],
            [0,2,0],
            [0,3,0]]
        )
        return super().setUp()


    def test_top_edge_visisble(self):
        assert is_visisble_from_top(x=0,y=0,forest=self.forest) is True


    def test_bottom_edge_visisble(self):
        assert is_visisble_from_bottom(x=1,y=2,forest=self.forest) is True


    def test_left_edge_visisble(self):
        assert is_visisble_from_left(x=0,y=1,forest=self.forest) is True


    def test_right_edge_visisble(self):
        assert is_visisble_from_right(x=2,y=1,forest=self.forest) is True


class TestHidden(TestCase):


    def setUp(self) -> None:
        self.forest = np.array(
            [[0,1,0],
            [0,2,1],
            [0,3,0]]
        )
        return super().setUp()


    def test_top_invisisble(self):
        assert is_visisble_from_top(x=2,y=2,forest=self.forest) is False


    def test_bottom_invisisble(self):
        assert is_visisble_from_bottom(x=1,y=0,forest=self.forest) is False


    def test_left_invisisble(self):
        assert is_visisble_from_left(x=2,y=2,forest=self.forest) is False


    def test_right_invisisble(self):
        assert is_visisble_from_right(x=0,y=2,forest=self.forest) is False


class TestVisibleFromOppositeCorner(TestCase):


    def setUp(self) -> None:
        self.forest = np.array(
            [[4,3,2,1],
            [3,2,1,0],
            [1,2,3,4]]
        )
        return super().setUp()


    def test_top_visisble_from_opposite(self):
        assert is_visisble_from_top(x=3,y=2,forest=self.forest) is True


    def test_bottom_visisble_from_opposite(self):
        assert is_visisble_from_bottom(x=0,y=0,forest=self.forest) is True


    def test_left_visisble_from_opposite(self):
        assert is_visisble_from_left(x=3,y=2,forest=self.forest) is True


    def test_right_visisble_from_opposite(self):
        assert is_visisble_from_right(x=0,y=0,forest=self.forest) is True


class TestMidVisible(TestCase):


    def setUp(self) -> None:
        self.forest = np.array(
            [[0,0,1,2,3],
            [1,2,3,2,1],
            [5,3,2,1,0],
            [0,0,0,0,0]]
        )
        return super().setUp()


    def test_top_mid_visible(self):
        assert is_visisble_from_top(x=2,y=1,forest=self.forest) is True


    def test_bottom_mid_visible(self):
        assert is_visisble_from_bottom(x=3,y=1,forest=self.forest) is True


    def test_left_mid_visible(self):
        assert is_visisble_from_left(x=2,y=1,forest=self.forest) is True


    def test_right_mid_visible(self):
        assert is_visisble_from_right(x=2,y=2,forest=self.forest) is True


class TestCountForest(TestCase):


    def test_demo(self):
        forest = txt_to_forest(DEMO)
        assert count_visible_in_forest(forest) == 21