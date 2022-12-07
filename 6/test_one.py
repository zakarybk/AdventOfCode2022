from unittest import TestCase
from one import pos_of_marker


class TestPos(TestCase):


    def test_demo_marker_5(self):
        assert pos_of_marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5


    def test_demo_marker_6(self):
        assert pos_of_marker("nppdvjthqldpwncqszvftbrmjlhg") == 6


    def test_demo_marker_10(self):
        assert pos_of_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10


    def test_demo_marker_11(self):
        assert pos_of_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11