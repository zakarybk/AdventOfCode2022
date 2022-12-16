from unittest import TestCase


from one import run


EXAMPLE_2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


class TestInstructions(TestCase):

    def test_example(self):
        example = [
            "noop",
            "addx 3",
            "addx -5"
        ]
        assert run(example, lambda x: False) == []

        assert run(example, lambda x: x == 1) == [(1, 1)]  # x, cycle
        assert run(example, lambda x: x == 2) == [(1, 2)]  # x, cycle
        assert run(example, lambda x: x == 3) == [(1, 3)]  # x, cycle
        assert run(example, lambda x: x == 4) == [(4, 4)]  # x, cycle

        """ x == cycle to break at - this value should be before the cycle has finished """

    def test_example_2(self):
        commands = EXAMPLE_2.splitlines()

        signals = run(commands, lambda i: i in [20, 60, 100, 140, 180, 220])

        assert signals[0] == (21, 20)
        assert signals[1] == (19, 60)
        assert signals[2] == (18, 100)
        assert signals[3] == (21, 140)
        assert signals[4] == (16, 180)
        assert signals[5] == (18, 220)
