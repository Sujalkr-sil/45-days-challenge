pick = [[0,0],[1,0],[1,0],[2,0],[2,0],[2,1]]
n = 4
result = [[0] * 11 for _ in range(n)]  kheb
count = 0

for player in range(0, len(pick)):
    for color in range(0, len(pick[player])-1):
        players=pick[player][0]
        ball=pick[player][1]
        result[players][ball] += 1
print(result)
for i in range(0,len(result)):
    for j in range(0,len(result[i])):
        if(result[i][j]>i):
            count+=1
            break
print(count)