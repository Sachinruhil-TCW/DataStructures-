from math import sqrt, pow
def closestLoc(t, all, cap):
    obj = {}
    data = []
    result = []
    for i in range(len(all)-1):
        curr = all[i]
        y = curr[1]
        x = curr[0]
        dist = sqrt(pow(y, 2) + pow(x, 2))
        dist = round(dist, 2)
        data.append(dist)
        obj[dist] = curr

    data.sort()

    for i in range(cap):
        curr = data[i]
        result.append(obj[curr])

    return result
    


input = [[1, -3], [1, 2], [3, 4]]
print(closestLoc(3, input, 2))
