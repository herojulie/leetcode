def openLock(target):
    q1 = set()
    q2 = set()
    visited = set()
    q1.add("000")
    q2.add(target)
    step = 0

    while(len(q1) != 0 and len(q2) != 0):
        temp = set()
        
        for cur in q1:
            if cur in q2:
                return step
            visited.add(cur)

            for j in range(3):
                up = plusOne(cur, j)
                if up not in visited:
                    temp.add(up)
                down = minusOne(cur, j)
                if down not in visited:
                    temp.add(down)
        
        step += 1
        q1 = q2
        q2 = temp
    
    return -1

def plusOne(s, j):
    ch = [c for c in s]
    if ch[j] == '9':
        ch[j] = '0'
    else: 
        ch[j] = str(int(ch[j]) + 1)
    return ''.join(ch)

def minusOne(s, j):
    ch = [c for c in s]
    if ch[j] == '0':
        ch[j] = '9'
    else: 
        ch[j] = str(int(ch[j]) - 1)
    return ''.join(ch)


print(openLock('101'))
