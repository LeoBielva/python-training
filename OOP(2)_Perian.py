class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        pi = 3.14
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * (self.radius) ** 2 * (self.height)

    def surface_area(self):
        return 2 * Cylinder.pi * (self.radius) ** 2 + 2 * Cylinder.pi * (self.radius) * (self.height)


mycylinder = Cylinder(2, 3)
print(mycylinder.volume())
print(mycylinder.surface_area())
