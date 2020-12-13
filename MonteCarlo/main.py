#Inspired by https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/
#Changed points distribution to one quarter and added showProgress variable which can be used to check how program works in each iteration
import random
points = 1000
showProgress= False
circle_points = 0
square_points = 0

for i in range(points):

    #We will work on <0, 1> range (one quarter of cirle)
    rand_x = random.uniform(0, 1)
    rand_y = random.uniform(0, 1)

    #Check distance from points (0,0)
    origin_dist = rand_x ** 2 + rand_y ** 2

    #Check if points belong to circle
    if origin_dist <= 1:
        circle_points += 1
    square_points += 1

    #Calculate PI
    pi = 4 * circle_points / square_points
    #Debug option
    if(showProgress):
        print("Current pi estimation ", pi, (points-i), " points remaining")

#Results
print("Final Estimation of Pi=", pi)
if (showProgress):
    print(circle_points, " Circle points and ", square_points, " Square points")