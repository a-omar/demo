from unittest import TestCase
from demo.demo import Bar

class TestBar(TestCase):
    def test_get_players(self):
        b = Bar()
        self.assertEquals(b.get_players(),10)


if __name__ == '__main__':
    TestBar().test_get_players()