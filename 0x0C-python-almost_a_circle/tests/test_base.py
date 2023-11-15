import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Creating test instances for CSV tests
        cls.r1 = Rectangle(10, 7, 2, 8)
        cls.r2 = Rectangle(2, 4)
        cls.list_rectangles_input = [cls.r1, cls.r2]

        cls.s1 = Square(5)
        cls.s2 = Square(7, 9, 1)
        cls.list_squares_input = [cls.s1, cls.s2]


    def setUp(self):
        # Clean up CSV files before each test
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_to_json_string(self):
        # Test to_json_string with a list of dictionaries
        input_list = [{'id': 1, 'name': 'test1'}, {'id': 2, 'name': 'test2'}]
        expected_output = '[{"id": 1, "name": "test1"}, {"id": 2, "name": "test2"}]'
        self.assertEqual(Base.to_json_string(input_list), expected_output)

        # Test to_json_string with an empty list
        empty_list = []
        self.assertEqual(Base.to_json_string(empty_list), '[]')

        # Test to_json_string with None
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_save_to_file(self):
        # Test save_to_file with a list of instances
        r1 = Base(1)
        r2 = Base(2)
        instance_list = [r1, r2]
        Base.save_to_file(instance_list)

        with open("Base.json", "r") as file:
            content = file.read()
            loaded_list = json.loads(content)
            self.assertEqual(len(loaded_list), 2)
            self.assertEqual(loaded_list[0]['id'], 1)
            self.assertEqual(loaded_list[1]['id'], 2)

    def test_from_json_string(self):
        # Test from_json_string with a JSON string
        json_string = '[{"id": 1, "name": "test1"}, {"id": 2, "name": "test2"}]'
        expected_output = [{'id': 1, 'name': 'test1'}, {'id': 2, 'name': 'test2'}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

        # Test from_json_string with an empty string
        empty_string = ''
        self.assertEqual(Base.from_json_string(empty_string), [])

        # Test from_json_string with None
        self.assertEqual(Base.from_json_string(None), [])

    def test_create(self):
        # Test create method
        instance_dict = {'id': 1, 'name': 'Rectangle'}
        instance = Base.create(**instance_dict)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'Rectangle')

    def test_load_from_file(self):
        # Test load_from_file method
        with open("Base.json", "w") as file:
            file.write('[{"id": 1, "name": "test1"}, {"id": 2, "name": "test2"}]')

        loaded_list = Base.load_from_file()
        self.assertEqual(len(loaded_list), 2)
        self.assertEqual(loaded_list[0].id, 1)
        self.assertEqual(loaded_list[1].id, 2)


    def test_save_to_file_csv(self):
        # Testing save_to_file_csv method
        Rectangle.save_to_file_csv(self.list_rectangles_input)
        Square.save_to_file_csv(self.list_squares_input)

        # Checking if CSV files were created
        self.assertTrue(os.path.exists("Rectangle.csv"))
        self.assertTrue(os.path.exists("Square.csv"))

    def test_load_from_file_csv(self):
        # Saving data to CSV files
        Rectangle.save_to_file_csv(self.list_rectangles_input)
        Square.save_to_file_csv(self.list_squares_input)

        # Loading data from CSV files
        loaded_rectangles = Rectangle.load_from_file_csv()
        loaded_squares = Square.load_from_file_csv()

        # Check if loaded data matches input data
        self.assertEqual(len(loaded_rectangles), len(self.list_rectangles_input))
        self.assertEqual(len(loaded_squares), len(self.list_squares_input))

        # Example: Check if the IDs match for rectangles
        self.assertEqual(loaded_rectangles[0].id, self.r1.id)
        self.assertEqual(loaded_rectangles[1].id, self.r2.id)

        # Example: Check if the IDs match for squares
        self.assertEqual(loaded_squares[0].id, self.s1.id)
        self.assertEqual(loaded_squares[1].id, self.s2.id)

    @classmethod
    def tearDownClass(cls):
        # Clean up CSV files after all tests are executed
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

if __name__ == '__main__':
    unittest.main()
