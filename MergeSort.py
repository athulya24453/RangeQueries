def merge(x,y):
    ans = []
    i=0
    j=0

    while i<len(x) or j<len(y):
        if j==len(y) or i<len(x) and x[i]<=y[j]:
            ans.append(x[i])
            i += 1

        else:
            ans.append(y[j])
            j += 1

    return ans

l1 = [1,3,4,5]
l2 = [1,2,4,6]

print(merge(l1,l2))