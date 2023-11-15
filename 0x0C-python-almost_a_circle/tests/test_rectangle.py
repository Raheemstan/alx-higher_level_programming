import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        # Test __init__ method with valid input
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)

        # Test __init__ method with invalid input
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)

    def test_area(self):
        # Test area method
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        # Test display method
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        self.assertEqual(r.display(), expected_output)

    def test_str(self):
        # Test __str__ method
        r = Rectangle(4, 5, 1, 2, 6)
        expected_output = "[Rectangle] (6) 1/2 - 4/5"
        self.assertEqual(str(r), expected_output)

    def test_update(self):
        # Test update method
        r = Rectangle(2, 3)
        r.update(7, 4, 5, 1, 2)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_to_dictionary(self):
        # Test to_dictionary method
        r = Rectangle(4, 5, 1, 2, 6)
        expected_dict = {'id': 6, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
