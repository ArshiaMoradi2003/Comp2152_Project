class Character:
    def __init__(self, combat_strength, health_points):
        self._combat_strength = combat_strength
        self._health_points = health_points

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if value < 0:
            raise ValueError("Combat strength cannot be negative.")
        self._combat_strength = value

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value < 0:
            raise ValueError("Health points cannot be negative.")
        self._health_points = value

    def __del__(self):
        print("The Character object is being destroyed by the garbage collector")
