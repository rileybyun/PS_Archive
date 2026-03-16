# 다리가 큐에 대응된다.
# 큐 총합을 sum으로 연산? => O(N)
# 그러기 보다, 계속 sum 값을 보관하고 있는 것이 나을 것 같다. => O(1)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(maxlen=bridge_length) # deque 최대 크기 제한
    weight_sum = 0
    i = 0
    
    while True:
        # 큐가 꽉 찼을 때 먼저 0번째 인덱스 제거 (weight_sum 관리 목적)
        if len(queue) == bridge_length:
            weight_sum -= queue[0]
            queue.popleft()

        # 조건 판단하여 다리에 트럭 추가
        x = 0
        if i < len(truck_weights):
            if weight_sum + truck_weights[i] <= weight:
                x = truck_weights[i]
                weight_sum += truck_weights[i]
                i += 1
        queue.append(x)
        answer += 1
        
        if i == len(truck_weights) and weight_sum == 0:
            break
    
    return answer