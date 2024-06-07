class Coordinate(object):

    def __init__(self, x_cord=0, y_cord=0):
        self.x = x_cord
        self.y = y_cord

    def distance_from_zero(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_from_a_point(self, foreign_point):
        return ((self.x - foreign_point.x) ** 2 + (self.y - foreign_point.y) ** 2) ** 0.5

    def distance_between_2_points(self, p1, p2):
        assert type(p1) is Coordinate
        assert type(p2) is Coordinate
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


'''
c = Coordinate(3, 4)
print(c.distance_from_zero())
d = Coordinate(12, 9)
origin = Coordinate(0,0)
print(d.distance_between_2_points(c, d))

print(c.distance_from_a_point(origin))
e = Coordinate(0,0)
print(e.distance_from_zero)
'''
