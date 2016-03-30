def intersection(a1, b1, c1, a2, b2, c2):
    # find the point of lines intersection. a1x+b1y+c1=0 and a2x+b2y+c2=0.
    # if these lines do not have intersection, return (inf,inf)
    d = a1 * b2 - a2 * b1
    if d == 0:
        return (float('inf'), float('inf'))
    if a1 == 0:
        x = (b2*c1-b1*c2)/(a2*b1)
        y = -c1/b1
        return (x,y)
    else:
        y =-(a1*c2-a2*c1)/(a1*b2-b1*a2)
        x = -(b1*y+c1)/a1
        return (x,y)


def is_line(a, b, c):
    # determine ax+by+c=0.
    if a == 0 and b == 0:
        return False
    else:
        return True

print(intersection(2,-1,4,-2,-1,2))
