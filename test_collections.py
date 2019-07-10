from collections import namedtuple
import unittest

class CollectionsTestCase(unittest.TestCase):
    
    def test_namedtuple(self):
        x = 1
        y = 2

        Point = namedtuple('Point', ['x', 'y'])
        p = Point(x, y=y)
        self.assertTrue(isinstance(p, Point))
        self.assertEqual(p.x, x)
        self.assertEqual(p.y, y)
        self.assertEqual(p[0], x)
        self.assertEqual(p[1], y)

        Point = namedtuple('Point', ['x', 'y'], defaults=[0, 0])
        p = Point()
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)

        Point = namedtuple('Point', ['x', 'def', 'x'], rename=True)
        p = Point(x, y, "val")
        self.assertEqual(p._1, y)
        self.assertEqual(p.x, x)
        self.assertEqual(p._2, 'val')
    
    def test_deque(self):
        pass


if __name__ == "__main__":
    unittest.main()