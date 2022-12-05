from unittest import TestCase


from one import item_priority, common_items, split_backpack, total_priorities


class TestPriority(TestCase):


    def test_lower_case_a_is_1(self):
        assert item_priority('a') == 1


    def test_lower_case_p_is_16(self): # oopsie, was using minus wrong way around
        assert item_priority('p') == 16


    def test_upper_case_A_is_1(self):
        assert item_priority('A') == 27


class TestCommonItems(TestCase):


    def test_common_a(self):
        assert common_items('ab', 'ac') == 'a'


class TestSplitBackpack(TestCase):


    def test_8_items_into_2_4s(self):
        assert split_backpack('abcdefgh') == ('abcd', 'efgh')


class TestTotalPriorities(TestCase):


    def test_first_demo_backpack(self):
        backpacks = [
            'vJrwpWtwJgWrhcsFMMfFFhFp'
        ]

        assert total_priorities(backpacks) == 16


    def test_demo(self):
        backpacks = [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw'
        ]

        assert total_priorities(backpacks) == 157