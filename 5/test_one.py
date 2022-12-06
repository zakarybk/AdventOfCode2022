from unittest import TestCase, skip
from collections import deque

from one import parse_stacks, make_stacks, parse_move, Move, run


DEMO_INPUT = \
"""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


class TestStackParse(TestCase):


    @skip('Bad text format')
    def test_parse_stack_text_area(self):
        expected = \
"""    [D]   
[N] [C]    
[Z] [M] [P]
 1   2   3 """
        assert parse_stacks(DEMO_INPUT) == expected

    @skip("deque wrong way around -- see test_ours_matches_demo")
    def test_parse_to_stacks(self):
        stack_data = parse_stacks(DEMO_INPUT)
        expected = [
            deque(('N', 'Z')),
            deque(('D', 'C', 'M')),
            deque(('P')),
        ]
        assert make_stacks(stack_data) == expected


class TestMoveParse(TestCase):


    def test_parse_move(self):
        # Where our index is 1 less due to starting from 0 instead of 1
        expected = Move(count=1,source=1,target=0)
        actual = parse_move("move 1 from 2 to 1")
        assert actual == expected


class TestDemo(TestCase):


    def test_ours_matches_demo(self):
        assert run(DEMO_INPUT) == "CMZ"