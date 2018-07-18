class DockingStation:

    DEFAULT_CAPACITY = 20

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.rack = []
        self.capacity = capacity

    def dock_bike(self, bike):
        self.rack.append(bike)
