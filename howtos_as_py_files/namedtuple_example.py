from collections import namedtuple

my_namedtuple = namedtuple('field_name', ['x', 'y', 'z', 'bla', 'blub'])
p = my_namedtuple(1, 2, 3, 4, 5)
print(p.x, p.y, p.z)
