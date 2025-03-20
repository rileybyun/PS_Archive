def fibonacci(n):
    # 재귀함수 (n이 너무 클 경우 부적합)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

def solution(n):
    answer = 0
    fibo = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            fibo.append(fibo[i-2] + fibo[i-1])  # Dynamic Programming (기억하며 풀기)
    # answer = fibonacci(n) % 1234567   # 시간초과 (함수 스택의 제한)
    answer = fibo[n] % 1234567
    return answer