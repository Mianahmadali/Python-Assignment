#Write a Python program that checks if a point (x, y) lies:

"""On the origin.
On the x-axis or y-axis.
In one of the four quadrants."""

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x == 0 and y == 0:
    print("The point is on origin")
elif x == 0:
    print("The point on y axis")
elif y == 0:
    print("The point in on X axis")
elif x > 0 and y > 0:
    print("The point is on Quadrant I")
elif x < 0 and y > 0:
    print("The point in on Quadrant II")
elif x < 0 and y < 0:
    print("The Point is on Quadrant III")
elif x > 0 and y < 0:
    print("The point6 is on Quadrant IV")