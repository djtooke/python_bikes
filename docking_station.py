class DockingStation:

    DEFAULT_CAPACITY = 20

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.rack = []
        self.capacity = capacity

    def dock_bike(self, bike):
        self.rack.append(bike)

    def release_bike(self):
        if self.__is_rack_empty(): raise Exception('Bike rack is empty!')
        return self.rack.pop()

    def __is_rack_empty(self):
        return len(self.rack) == 0
