
cost = float(input())
lawns = int(input())
total = 0 
for i in range(lawns) :
    length = list(input().split())
    total += float(length[0]) * float(length[1]) * cost

print(total) 