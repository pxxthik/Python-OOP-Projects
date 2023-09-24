from random import randint
import turtle


class Point:
    """
    Class that contain x and y coordinates of a point and tells
    the point falls in given rectangle or not.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle_area):
        return rectangle_area.point1.x < self.x < rectangle_area.point2.x \
            and rectangle_area.point1.y < self.y < rectangle_area.point2.y


class Rectangle:
    """
    Class that contains lower left point (point1) and upper right
    (point2) of a rectangle and returns the area of rectangle.
    """

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    """
    Child of Rectangle class for a GUI representation of rectangle.
    """
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):
    """Child of Point class for GUI representation of point"""

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)

        canvas.pendown()
        canvas.dot(size, color)

        turtle.done()


# Create rectangle object
rectangle = GuiRectangle(Point(randint(0, 200), randint(0, 200)),
                         Point(randint(10, 200), randint(10, 200)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

myturtle = turtle.Turtle()
rectangle.draw(myturtle)
user_point.draw(myturtle)
