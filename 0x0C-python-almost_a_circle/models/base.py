#!/usr/bin/python3
"""Base module"""

import json
import csv
import turtle

class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""

        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""

        filename = "{}.json".format(cls.__name__)

        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string"""

        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy


    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""

        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                contents = file.read()
                list_dicts = cls.from_json_string(contents)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
        
    
    def update(self, *args, **kwargs):
        attributes = ["id", "width", "height", "size", "x", "y"]
        for idx, arg in enumerate(args):
            setattr(self, attributes[idx], arg)

        if not args or len(args) < len(attributes):
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return self.__dict__
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        file_name = cls.__name__ + ".csv"
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv())

    @classmethod
    def load_from_file_csv(cls):
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, mode='r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    args = [int(x) if i != 0 else x for i, x in enumerate(row)]
                    instance = cls.create(*args)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
        
    def to_csv(self):
        return [self.id, self.width, self.height, self.x, self.y]

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.title("Rectangles and Squares")
        t = turtle.Turtle()

        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.forward(rectangle.width)
            t.left(90)
            t.forward(rectangle.height)
            t.left(90)
            t.forward(rectangle.width)
            t.left(90)
            t.forward(rectangle.height)
            t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        turtle.done()