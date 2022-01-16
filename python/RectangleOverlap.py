def isRectangleOverlap(rec1, rec2):
    if rec2[0] - rec1[0] >= 0:
        if rec2[0] - rec1[2] < 0:
            if rec2[1] - rec1[1] >= 0:
                if rec2[1] - rec1[3] < 0:
                    return True
                else:
                    return False
            else:
                if rec2[3] - rec1[1] > 0:
                    return True
                else:
                    return False
        else:
            return False
    else:
        if rec2[2] - rec1[0] > 0:
            return True
        else:
            return False
    return False

def overlappedRec(rec1, rec2):
    if isRectangleOverlap(rec1, rec2):
        if rec2[0] - rec1[0] >= 0:
            x1 = rec2[0]
        else:
            x1 = rec1[0]
        if rec2[2] - rec1[2] <= 0:
            x2 = rec2[2]
        else:
            x2 = rec1[2]
        if rec2[1] - rec1[1] >= 0:
            y1 = rec2[1]
        else:
            y1 = rec1[1]
        if rec2[3] - rec1[3] <= 0:
            y2 = rec2[3]
        else:
            y2 = rec1[3]
        newrec = [x1, y1, x2, y2]
        area = (x2 - x1) * (y2 - y1)
    else:
        newrec = []
        area = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1]) + (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])
    return newrec, area

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
# rec1 = [0,0,1,1]
# rec2 = [1,0,2,1]
# rec1 = [0,0,1,1]
# rec2 = [2,2,3,3]
print(isRectangleOverlap(rec1, rec2))
print(overlappedRec(rec1, rec2))
