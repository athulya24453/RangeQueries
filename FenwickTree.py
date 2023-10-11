# Range sum queries

def sum(Tree,i): 
    sum = 0
    i = i+1 
    while i > 0: 

        sum += Tree[i]

        i -= i & (-i)
    return sum


def update(Tree ,n ,i ,v): 

    i += 1

    while i <= n: 

        Tree[i] += v 

        i += i & (-i) 
  


def construct(arr, n): 
    Tree = [0]*(n+1) 

    for i in range(n): 
        update(Tree, n, i, arr[i]) 

    return Tree 

freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9] 
Tree = construct(freq,len(freq)) 
print("Sum of elements in arr[0..5] is " + str(sum(Tree,5))) 
freq[3] += 6
update(Tree, len(freq), 3, 6) 
print("Sum of elements in arr[0..5]"+
                    " after update is " + str(sum(Tree,5)))