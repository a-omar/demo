from unittest import TestCase
from demo.demo import Bar

class TestBar(TestCase):
    def test_get_players(self):
        b = Bar()
        self.assertEquals(b.get_players(),10)
