# 2020.02.03 List2 연습문제1
def isWall(x,y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    return False

arr = [[1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,1]]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
sum = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX,testY) == False:
                sum += abs(arr[x][y] - arr[testX][testY])
print(sum)