import unittest
from docking_station import DockingStation

class TestDockingStation(unittest.TestCase):

    def test_rack(self):
        self.assertIsInstance( DockingStation().rack, list)

    def test_dock_bike(self):
        bike = 'bike'
        station = DockingStation()
        station.dock_bike(bike)
        self.assertTrue( station.rack[0] == bike)

if __name__ == '__main__':
    unittest.main()
