def solution(a, b, c):
    unique_set = {a, b, c}  # set
    if len(unique_set) == 3:
        return a + b + c
    elif len(unique_set) == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)