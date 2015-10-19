from math import hypot

x1 = int(input("Give me the first parameter(x1):"))
y1 = int(input("Give me the first parameter(y1):"))
x2 = int(input("Give me the second parameter(x2):"))
y2 = int(input("Give me the second parameter(y2):"))

hip1 = hypot(x1,y1)
hip2 = hypot(x2,y2)

def Distance(hip1,hip2):
    x = abs(hip2 - hip1)
    print ("The Distance between the 2 points on the cartesian plane is:",x)

Distance(hip1,hip2)
