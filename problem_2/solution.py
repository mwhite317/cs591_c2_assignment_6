import math
import sys


class Square(object):

    def __init__(self, length):
        self.length = length

    def perimeter(self):
        return self.length * 4

    def area(self):
        return self.length * self.length

    def __str__(self):
        return "Area: " + str(self.area()) + " square units and Perimeter: " + str(self.perimeter()) + " units"


class Rectangle(object):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def area(self):
        return self.length * self.width

    def __str__(self):
        return "Area: " + str(self.area()) + " square units and Perimeter: " + str(self.perimeter()) + " units"


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        answer = math.pi * (self.radius * 2)
        return round(answer, 2)

    def area(self):
        answer = math.pi * (math.pow(self.radius, 2))
        return round(answer, 2)

    def __str__(self):
        return "Area: " + str(self.area()) + " square units and Circumference: " + str(self.circumference()) + " units"


def circle_input():
    circle_question = input("Circle radius? ")
    if not circle_question <= -1 and circle_question is not "":
        shape = Circle(circle_question)
        print shape


def square_input():
    square_question = input("Square side length? ")
    if not square_question <= -1:
        shape = Square(square_question)
        print shape


def rectangle_input():
    rect_length_question = input("Rectangle length? ")
    rect_width_question = input("Rectangle width? ")
    if not rect_length_question <= -1 and not rect_width_question <= -1:
        shape = Rectangle(rect_length_question, rect_width_question)
        print shape


def quit_input():
    print "Quitting shape game, goodbye."
    sys.exit()


shapes = {"R": rectangle_input,
          "S": square_input,
          "C": circle_input,
          "Q": quit_input}


def unknown_input():
    print "Please select from {}".format(key for key in shapes.keys())


if __name__ == '__main__':
    while True:
        initial_question = ""
        while initial_question not in shapes.keys():
            initial_question = raw_input("Choose a shape: (C)ircle or (R)ectangle or (S)quare: ")

        shapes.get(initial_question, unknown_input)()
