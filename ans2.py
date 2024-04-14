import heapq

INF = 2**12
cur = [INF] * 100
cur[1]= 0
Q = []
heapq.heappush(Q,(cur[1],1))
print(Q)