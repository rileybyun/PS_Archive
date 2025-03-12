n = int(input())    # 입력되는 정수의 개수
nums = map(int, input().split())
target_n = int(input())

answer = 0
for i in nums:
    if i == target_n:
        answer += 1

print(answer)