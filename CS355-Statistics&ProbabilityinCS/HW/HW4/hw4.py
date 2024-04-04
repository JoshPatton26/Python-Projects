from math import pi, sin, cos

# Riemann Sum Calculator: Area under the curve of f(x) = sin(x) * cos(x) from (0, 4pi)

# Get the number of rectangles 
s = int(input("How many rectangles would you like to use? "))
# Divide the 4pi by number of rectangles to get each rectangles width.
w = (4*pi)/s

# Takes in a value and calculate the y-value of the graph of the given function.
def exp(n):
    v = (sin(n) * cos(n))
    return v

i = 0
sum = 0.0
# Loop from 0 to 4pi and get every y-value(height) and multiply by the width to get area of that rectangle. 
while(i <= 4*pi):
    k = exp(i)
    # For this assignment we were told to assume all the area is positive, so take the absloutes of the negative y-values.   
    val = abs(k) * w 
    # Form a sum of all the rectangles areas to get the approximation of the area under the curve.
    sum = sum + val
    # Increment the value of i to the width of the rectangle.
    i += w
print("\nArea under the curve = %f\n" %sum)