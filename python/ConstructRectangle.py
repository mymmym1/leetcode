import math

def constructRectangle(area):
    mid = int(math.sqrt(area))
    product, l = multiply(area, mid)
    if product == area:
        return [l, mid]
    elif product > area:
        while mid - 1 >= 0:
            mid -= 1
            product, l = multiply(area, mid)
            if product == area:
                return [l, mid]
    return [area, 1]

def multiply(area, mid):
    product = 0
    n = -1
    while product < area:
        n += 1
        l = mid + n
        product = mid * l
    return product, l

#area = 4
#area = 37
area = 122122
print(constructRectangle(area))

