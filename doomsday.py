def solution(total_lambs):
    minLambs = total_lambs
    minHench = 0
    while minLambs > 0:
        minLambs = minLambs - 2**(minHench)
        minHench = minHench + 1
    if minLambs != 0:
        minHench = minHench - 1

    maxHench = 1
    maxLambs = total_lambs - 1
    n1, n2 = 0, 1
    while 0 < maxLambs:
        nth = n1 + n2
        maxLambs = maxLambs - nth
        n1 = n2
        n2 = nth
        maxHench = maxHench + 1
    if maxLambs != 0:
        maxHench = maxHench - 1

    return maxHench - minHench
