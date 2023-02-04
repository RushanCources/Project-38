def bin_min(arr, x):
    l, r = 0, len(arr) - 1
    
    while r - l > 1:
        c = (l + r)//2
        
        if x > arr[c]:
            l = c
            
        else:
            r = c
            
    return l, r

N = int(input())
A = [list(map(int, input().split(" "))) for i in range(N)]
A.sort()
U = {i[1]: [] for i in A}

for i in A:
    U[i[1]].append(i[0])
    
m = float("inf")
first = list(U)[0]

for i in U[first]:
    arr = [(bin_min(U[k], i), k) for k in U if k != first]
    arr = [U[k[1]][k[0][0]] if (abs(U[k[1]][k[0][0]] - i) < abs(U[k[1]][k[0][1]] - i)) else U[k[1]][k[0][1]] for k in arr] + [i]
    
    m2 = max(arr) - min(arr)
    
    if m2 < m:
        m = m2
    
print(m)