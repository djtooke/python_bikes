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

    def test_default_capacity_constant(self):
        self.assertEqual( DockingStation().DEFAULT_CAPACITY, 20)

    def test_default_capacity_set(self):
        self.assertEqual( DockingStation().capacity, 20)

    def test_setting_chosen_capacity(self):
        station = DockingStation(15)
        self.assertEqual( station.capacity, 15)

    def test_release_bike(self):
        station = DockingStation()
        station.dock_bike('Bike')
        self.assertEqual( station.release_bike(), 'Bike')

    def test_no_bike_released_if_rack_empty(self):
        station = DockingStation()
        with self.assertRaises(Exception) as e:
            station.release_bike()
            self.assertEqual(e.exception.message, 'Bike rack is empty!')

if __name__ == '__main__':
    unittest.main()
