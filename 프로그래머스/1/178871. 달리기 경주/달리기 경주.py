def solution(players, callings):
    # list index()를 피하는 대신, 새로운 자료구조를 만들어 해결
    orders = list(range(len(players)))
    ahead = [""] + players[:-1]
    back = players[1:] + [""]

    a = map(list, zip(orders, ahead, back))
    ds = dict(zip(players, a))

    pivot = players[0]  # 맨 앞에 있는 사람 이름

    for called_person in callings:
        the_rank = ds[called_person][0]
        back_person = ds[called_person][2]
        front_person = ds[called_person][1]
        front_front_person = ds[front_person][1]

        if front_front_person != '':
            ds[front_front_person][2] = called_person
        else:
            pivot = called_person
        ds[called_person] = [the_rank - 1, front_front_person, front_person]
        ds[front_person] = [the_rank, called_person, back_person]
        if back_person != '':
            ds[back_person][1] = front_person

    result = []
    while pivot != '':
        result.append(pivot)
        pivot = ds[pivot][2]

    return result