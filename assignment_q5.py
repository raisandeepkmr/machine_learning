import math

def calcArea(param):
    return math.pi * param * param
def calcCircum(param):
    return 2 * math.pi * param

radius = 30;
_area_of_circle_ = calcArea(radius)
print("Area of circle(m): " + str(_area_of_circle_))
_circum_of_circle_ = calcCircum(radius)
print("Circumference of circle(m): " + str(_circum_of_circle_))
print("Enter radius to calculate area(m): ")
userRad = int(input())
print("Area of user input(m): " + str(calcArea(userRad)))