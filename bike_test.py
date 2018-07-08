import unittest
from bike import Bike

class TestBike(unittest.TestCase):

    def test_working(self):
        self.assertTrue( Bike().working)

if __name__ == '__main__':
    unittest.main()
