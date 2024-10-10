def solution(n, words):
    beforewords = set(); last_character = ""
    i = 0
    while i < len(words):
        if len(beforewords) == 0:
            pass
        else:
            if len(words[i]) <= 1:
                return [(i % n) + 1, (i // n) + 1]
            elif words[i] in beforewords:
                return [(i % n) + 1, (i // n) + 1]
            elif words[i][0] != last_character:
                return [(i % n) + 1, (i // n) + 1]
            else:
                pass
        beforewords.add(words[i])
        last_character = words[i][-1]
        i += 1
    return [0, 0]