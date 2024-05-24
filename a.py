N,M = map(int,input().split())
S = [input() for _ in range(N)]


tak =[
    '###.?????',
    '###.?????',
    '###.?????',
    '....?????',
    '?????????',
    '?????....',
    '?????.###',
    '?????.###',
    '?????.###' ]

n,m = len(tak), len(tak[0])

for y in range(N-n+1):
    for x in range(M-m+1):
        ok = True
        for dy in range(n):
            for dx in range(m):
                ok &= S[y+dy][x+dx] == tak[dy][dx] or tak[dy][dx] == "?"
        
        if ok:
            print(y+1,x+1)
