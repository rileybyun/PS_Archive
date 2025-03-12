r, c = map(int, input().split())
matrix1 = []
matrix2 = []

for i in range(r):
    nums = map(int, input().split())
    matrix1.append(list(nums))

for i in range(r):
    nums = map(int, input().split())
    matrix2.append(list(nums))

# 행렬 합 출력
for i in range(r):
    for j in range(c):
        print(f'{matrix1[i][j] + matrix2[i][j]}', end=' ')
    print()