class DockingStation:

    DEFAULT_CAPACITY = 20

    def __init__(self):
        self.rack = []

    def dock_bike(self, bike):
        self.rack.append(bike)
