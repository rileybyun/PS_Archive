def solution(phone_book):
    # 각 전화번호의 길이는 1이상 20이하
    prefix_set = set()
    
    # 모든 가능한 접두어 저장
    for phone_num in phone_book:
        for i in range(len(phone_num)-1):
            # 전화번호 전체가 통으로 저장되는 경우는 배제
            prefix_set.add(phone_num[:i+1])
    
    # 접두어와 매칭되는 전화번호 탐색
    for phone_num in phone_book:
        if phone_num in prefix_set:
            return False
    
    return True