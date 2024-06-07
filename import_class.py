from Coordinate_class import Coordinate

c = Coordinate(3, 4)
print(c.distance_from_zero())
d = Coordinate(12, 9)
origin = Coordinate(0, 0)
print(d.distance_between_2_points(c, d))
print(c.distance_from_a_point(origin))

e = Coordinate(0, 0)
print(e.distance_from_zero())

#we can  also use class.method(object and parameter)
print(Coordinate.distance_from_zero(c))

print(c)