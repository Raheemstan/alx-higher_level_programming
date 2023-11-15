import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        # Test __init__ method with valid input
        s = Square(5)
        self.assertEqual(s.size, 5)

        # Test __init__ method with invalid input
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_area(self):
        # Test area method
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_display(self):
        # Test display method
        s = Square(2)
        expected_output = "##\n##"
        self.assertEqual(s.display(), expected_output)

    def test_str(self):
        # Test __str__ method
        s = Square(4, 1, 2, 6)
        expected_output = "[Square] (6) 1/2 - 4"
        self.assertEqual(str(s), expected_output)

    def test_update(self):
        # Test update method
        s = Square(2)
        s.update(7, 4, 1, 2)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_to_dictionary(self):
        # Test to_dictionary method
        s = Square(4, 1, 2, 6)
        expected_dict = {'id': 6, 'size': 4, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
