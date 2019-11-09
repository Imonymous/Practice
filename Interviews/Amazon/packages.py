#!/usr/bin/env python

def IDsOfPackages(truckSpace, packagesSpace):
    # WRITE YOUR CODE HERE
    safetyUnits = 30

    if truckSpace > safetyUnits:
        realTruckSpace = truckSpace - safetyUnits
    else:
        return

    ans = [0, 0]
    first = True
    for i in range(len(packagesSpace)):
        p = packagesSpace[i]
        if p < realTruckSpace:
            max_comp = realTruckSpace - p
            for j in range(i, len(packagesSpace)):
                comp = packagesSpace[j]
                if comp == max_comp:
                    candidate = sorted([i,j])
                    if first:
                        ans = candidate
                        first = False
                        continue

                    if (((packagesSpace[ans[0]]+packagesSpace[ans[1]]) == (packagesSpace[candidate[0]]+packagesSpace[candidate[1]])) and
                        max(packagesSpace[ans[0]], packagesSpace[ans[1]]) < max(packagesSpace[candidate[0]], packagesSpace[candidate[1]])):
                        ans = candidate
    return ans
print(IDsOfPackages(250, [100,180,40,120,10]))
