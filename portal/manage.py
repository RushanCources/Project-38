def bin_min(arr, x):
    l, r = 0, len(arr) - 1
    
    while r - l > 1:
        c = (l + r)//2
        
        if x > arr[c]:
            l = c
            
        else:
            r = c
            
    return l

class IndexedTree:
    p = None
    l = None
    r = None
    val = None
    index = None
    
def search_in_tree(tree, x):
    now = tree
    
    while True:
        if x > now.val:
            if now.r:
                if (now.r.val < x) or (minimum(now.r).val < x):
                    now = now.r
                    
                else:
                    return now
                
            else:
                return now
            
        else:
            if now.l:
                now = now.l
                
            else:
                return IndexedTree()
        
def add_to_tree(tree, x, index):
    now = tree
    
    while True:
        if x > now.val:
            if now.r:
                now = now.r
                
            else:
                a = IndexedTree()
                a.val = x
                a.index = [index]
                a.p = now
                now.r = a
                
                return a
            
        elif x < now.val:
            if now.l:
                now = now.l
                
            else:
                a = IndexedTree()
                a.val = x
                a.index = [index]
                a.p = now
                now.l = a
                
                return a
            
        else:
            now.index.append(index)
            
            return now
            
def minimum(node):
    now = node
    
    while True:
        if now.l:
            now = now.l
            
        else:
            return now
        
def maximum(node):
    now = node
    
    while True:
        if now.r:
            now = now.r
            
        else:
            return now
    
def del_node(node):
    if node.p.l == node:
        if node.r:
            node.p.l = node.r
            node.r.p = node.p
            m = minimum(node.r)
            m.l = node.l
            
            if node.l:
                node.l.p = m
            
        else:
            node.p.l = node.l
            
            if node.l:
                node.l.p = node.p
        
    else:
        if node.l:
            node.p.r = node.l
            node.l.p = node.p
            m = minimum(node.l)
            m.r = node.r
            
            if node.r:
                node.r.p = m
            
        else:
            node.p.r = node.r
            
            if node.r:
                node.r.p = node.p

k = int(input())
text = input().encode("utf-8")
lines = []
curs = IndexedTree()
curs.val = 0

if text:
    for i in text:
        res = search_in_tree(curs, i)
        
        if res.index == None:
            print(f"add {i} to {len(lines)}") 
            res = add_to_tree(curs, i, len(lines))
            lines.append([i])
            
        else:
            print(f"remove {res.val} and add {i}") 
            c = res.index.pop(0)
            lines[c].append(i)
            
            if not res.index:
                del_node(res)
                
            res = add_to_tree(curs, i, c)

    flag = True

    for i in lines:
        errors = 0
        
        if i[0] != 65:
            errors = i[0] - 65
        
        for n in range(1, len(i)):
            errors += i[n] - i[n - 1] - 1
            
        if errors > k:
            flag = False
            
            break

    if flag:
        print(len(lines))

    else:
        print("Impossible")
        
else:
    if k == 0:
        print("Impossible")
        
    else:
        print(1)
