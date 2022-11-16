import random

def isTriangle(piece1, piece2, piece3):
# REFERENCE: https://www.mathwarehouse.com/geometry/triangles/triangle-inequality-theorem-rule-explained.php
    # a + b > c and a + c > b and b + c > a
    if(((piece1 + piece2) > piece3) and ((piece1 + piece3) > piece2) and ((piece2 + piece3) > piece1)): #check if the 3 pieces/sides form a valid triangle using the Triangle Inequality Theorem
        return 1
    return 0 


def monteCarlo():
    runs = 10000
    count = 0
    numValid = 0

    while(count < runs): #run 10,000 times
       #creating the sides of the triangle
        a = 0
        b = 0

        #creating the 2 random break points
        for i in range(2):
            a = random.random()
            b = random.random()
            # print(a, " ", b)

        breakA = min(a, b)
        breakB = max(a, b)

        #break stick into 3 pieces for the 3 sides
        piece1 = breakA
        piece2 = breakB - breakA
        piece3 = 1 - breakB

        if(isTriangle(piece1, piece2, piece3)): #check if the 3 sides can make a triangle
            numValid +=1 
        count+=1

    probability = round((numValid / runs), 3)

    print("The probablity that a 1 meter stick can be arranged into a triangle is:", probability)

    
if __name__ == '__main__':
    monteCarlo()