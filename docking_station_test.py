import unittest
from docking_station import DockingStation

class TestDockingStation(unittest.TestCase):

    def test_rack(self):
        self.assertIsInstance( DockingStation().rack, list)

if __name__ == '__main__':
    unittest.main()
