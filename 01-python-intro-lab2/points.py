
class Point(object):
    nextId = 0
    def __init__(self, x, y):
        self.__class__.nextId += 1; # autoincrement id
        self.id = Point.nextId
        self.x = x
        self.y = y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == "__main__":
    p1 = Point(4, 5) # create class instance = object
    print(f'(id: {p1.id}, x:{p1.x}, y:{p1.y})')
    p1.move(10,10)
    Point.move(p1, 10, 10)
    print(f'(id: {p1.id}, x:{p1.x}, y:{p1.y})')
    p2 = Point(12, 7) # create class instance = object
    print(f'(id: {p2.id}, x:{p2.x}, y:{p2.y})')

    print(Point.nextId)
    print(p1.x)
    print(getattr(p1, 'x'))
    print(p1.__class__)
    print(type(p1))