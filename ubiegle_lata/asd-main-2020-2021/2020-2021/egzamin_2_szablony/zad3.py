from zad3testy import runtests


# to jest zlozonosc akceptowalna. wzorcowa to drzewa przedzialowe. musze do tego wrocic


def lamps(n, L):
    t = [0 for _ in range(n)]
    cnt = 0
    res = 0
    for a, b in L:
        for i in range(a, b + 1):
            t[i] += 1
            if t[i] % 3 == 2:
                cnt += 1
            if t[i] % 3 == 0:
                cnt -= 1
        res = max(res, cnt)
    return res


runtests(lamps)

