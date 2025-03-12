original_members = set(range(1,31))
attendence = set()

for i in range(28):
    n = int(input())
    attendence.add(n)

answer = list(original_members - attendence)
answer.sort()

print(answer[0])
print(answer[1])