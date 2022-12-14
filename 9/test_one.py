from unittest import TestCase


from one import step, run, Vec2, Direction, generate_board


class TestCalcDirection(TestCase):


    def setUp(self) -> None:
        self.source = Vec2(0,0)


    def test_up_right_diagonal(self):
        target = (Direction.RIGHT + Direction.UP) * 2
        assert self.source.direction(target) == (Direction.RIGHT + Direction.UP)


    def test_down_right_diagonal(self):
        target = (Direction.RIGHT + Direction.DOWN) * 2
        assert self.source.direction(target) == (Direction.RIGHT + Direction.DOWN)


    def test_up_left_diagonal(self):
        target = (Direction.LEFT + Direction.UP) * 2
        assert self.source.direction(target) == (Direction.LEFT + Direction.UP)


    def test_down_left_diagonal(self):
        target = (Direction.LEFT + Direction.DOWN) * 2
        assert self.source.direction(target) == (Direction.LEFT + Direction.DOWN)


    def test_left(self):
        # Mainly testing the normalise func
        target = Direction.LEFT * 2
        assert self.source.direction(target) == Direction.LEFT


    def test_up(self):
        self.head = Vec2(4,3)
        self.tail = Vec2(4,1)
        assert self.tail.distance(self.head) == 2
        assert self.tail.direction(self.head) == Direction.UP


class TestCalcDistance(TestCase):


    def setUp(self) -> None:
        self.source = Vec2(0,0)


    def test_distance_of_1(self):
        assert self.source.distance(Vec2(1,0)) == 1
        assert self.source.distance(Vec2(0,1)) == 1
        # assert self.source.distance(Vec2(1,1)) == 1

        assert self.source.distance(Vec2(-1,0)) == 1
        assert self.source.distance(Vec2(0,-1)) == 1
        # assert self.source.distance(Vec2(-1,-1)) == 1


class TestSingleStep(TestCase):


    def setUp(self) -> None:
        self.head, self.tail = Vec2(0,0), Vec2(0,0)


    def test_step_right(self):
        self.head, self.tail = step(self.head, self.tail, Direction.RIGHT)
        assert self.head == Vec2(1,0)


    def test_step_left(self):
        self.head, self.tail = step(self.head, self.tail, Direction.LEFT)
        assert self.head == Vec2(-1,0)


    def test_step_up(self):
        self.head, self.tail = step(self.head, self.tail, Direction.UP)
        assert self.head == Vec2(0,1)


    def test_step_down(self):
        self.head, self.tail = step(self.head, self.tail, Direction.DOWN)
        assert self.head == Vec2(0,-1)


class TestTailFollowsStraights(TestCase):


    def setUp(self) -> None:
        self.head, self.tail = Vec2(0,0), Vec2(0,0)


    def test_follow_right(self):
        self.head, self.tail = step(self.head, self.tail, Direction.RIGHT)
        self.head, self.tail = step(self.head, self.tail, Direction.RIGHT)
        assert self.head == Vec2(2,0)
        assert self.tail == Vec2(1,0)


    def test_follow_left(self):
        self.head, self.tail = step(self.head, self.tail, Direction.LEFT)
        self.head, self.tail = step(self.head, self.tail, Direction.LEFT)
        assert self.head == Vec2(-2,0)
        assert self.tail == Vec2(-1,0)


    def test_follow_up(self):
        self.head, self.tail = step(self.head, self.tail, Direction.UP)
        self.head, self.tail = step(self.head, self.tail, Direction.UP)
        assert self.head == Vec2(0,2)
        assert self.tail == Vec2(0,1)


    def test_follow_down(self):
        self.head, self.tail = step(self.head, self.tail, Direction.DOWN)
        self.head, self.tail = step(self.head, self.tail, Direction.DOWN)
        assert self.head == Vec2(0,-2)
        assert self.tail == Vec2(0,-1)


# class TestTailFollowsDiagonal(TestCase):

#     def setUp(self) -> None:
#         self.head, self.tail = Vec2(0,0), Vec2(0,0)


class TestDemo(TestCase):


    def test_demo_line_1(self):
        steps = ['R 4']
        visits, _ = run(steps)
        assert visits == 4


    def test_demo_line_2(self):
        steps = ['U 4']
        visits, _ = run(steps)
        assert visits == 4


    def test_full_demo(self):
        steps = \
"""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()
        count, history = run(steps)

        plays = generate_board(history)
        print(plays)

        assert count == 13