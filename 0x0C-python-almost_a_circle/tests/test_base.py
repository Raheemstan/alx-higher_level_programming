import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
