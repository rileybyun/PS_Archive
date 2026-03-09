def solution(numbers, target):
    answer = 0
    
    def dfs(idx, sum_value):
        nonlocal answer
        
        if idx == len(numbers):
            if sum_value == target:
                answer += 1
            return
        
        dfs(idx + 1, sum_value + numbers[idx])
        dfs(idx + 1, sum_value - numbers[idx])
    
    dfs(0,0)
            
    return answer