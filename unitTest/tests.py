import unittest
from square import SquareField


class TestSquareField(unittest.TestCase):

    def setUp(self):
        self.square = SquareField()

    def testSquareFieldInit(self):
        self.square = SquareField()
        assert self.square.side_value != None, "square side value is None"

    def testSquareFieldSideValue(self):
        self.square = SquareField()
        self.square.setSquareField(4)
        assert self.square.side_value == 4, "square field isn't correctly"


if __name__ == "__main__":
    unittest.main()
