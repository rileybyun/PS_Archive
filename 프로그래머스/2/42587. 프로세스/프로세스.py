# priorities의 종류는 9가지 (1~9)
# 리스트로 각 priority 별 프로세스의 개수를 관리할까?
# 그리고 매번 가장 높은 priority 프로세스 중 가장 앞에 있는 것을 찾아내면 될 듯 한데..
# 여기에서 중요한 건 대상이 되는 프로세스의 priority 이상의 프로세스들 (그것보다 낮으면 관심X)
# 매번 실행해야 하는 프로세스가 어디에 있는지 파악 => 새롭게 큐가 만들어졌다고 상상하고, 그 큐에서의 순서대로 각 원소별 위치를 저장(해당 프로세스 바로 오른쪽에 있으면 새로운 큐의 인덱스 상 0번째)
# 매번 실행해야 하는 프로세스가 리스트에서 제거하고, 관심 프로세스의 리스트 상 위치도 재조정

def get_highest_priority(priorities_sum):
    '''
    남아 있는 프로세스 중 가장 높은 우선순위 구하는 함수
    입력값: 우선순위 별 프로세스 계수 합계
    '''
    for i in range(len(priorities_sum)-1,-1,-1):
        if priorities_sum[i] > 0:
            return i
        else:
            pass
    return -1


def solution(priorities, location):
    answer = 1  # 실행 순서
    
    # 리스트 생성 (관심 프로세스의 우선순위 이상의 프로세스들만 남김)
    interest_process_priority = priorities[location]
    prior_sum = [0] * 10    # 사용하는 인덱스: 1 ~ 9
    prior_filtered = []     # 필터링된 프로세스들 우선순위 저장
    prior_queue = []        # 필터링된 프로세스들의 가상의 큐 인덱스 저장
    queue_location = location   # 가상의 큐에서의 관심 프로세스 위치
    queue_idx = 0
    for i in range(len(priorities)):
        if priorities[i] < interest_process_priority:
            # 해당 프로세스 제외
            if i < location:
                queue_location -= 1   # 관심 프로세스 위치 재조정
        else:
            # 해당 프로세스 포함
            prior_sum[priorities[i]] += 1
            prior_filtered.append(priorities[i])
            prior_queue.append(queue_idx)
            queue_idx += 1
    
    queue_pointer = 0   # 가상의 큐 인덱스가 0인 곳의 위치
    while True:
        # 이번에 실행할 프로세스 찾기
        highest_priority = get_highest_priority(prior_sum)
        try:
            next_process_idx = prior_filtered.index(highest_priority, queue_pointer)
        except:
            next_process_idx = prior_filtered.index(highest_priority, 0)
        
        # 이번에 실행할 프로세스가 관심 프로세스인지 확인
        if next_process_idx == queue_location: 
            return answer
        else: pass
        
        # 실행된 프로세스 제거
        prior_sum[highest_priority] -= 1
        del prior_filtered[next_process_idx]
        del prior_queue[next_process_idx]
        if next_process_idx < queue_location:
                queue_location -= 1   # 관심 프로세스 위치 재조정
        
        # 가상의 실행 큐 재구성
        if next_process_idx == len(prior_queue):
            queue_pointer = 0
        else:
            queue_pointer = next_process_idx
        queue_idx = 0
        
        for i in range(next_process_idx, len(prior_queue)):
            prior_queue[i] = queue_idx
            queue_idx += 1
        if next_process_idx > 0:
            for i in range(next_process_idx):
                prior_queue[i] = queue_idx
                queue_idx += 1
        
        # 실행 횟수 카운트 업
        answer += 1


print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1], 0))
