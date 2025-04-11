'''
Karolina Nitsch, 421767
Poniższy algorytm polega na uzupełnianiu tablicy 3-wymiarwej results[i][k][j] wartościami logicznymi, które określają czy da się, aby we fragmencie
sadu składającego się z pierwszych i+1 drzew (czyli kończącym się na i-tym drzewie z tablicy T) po wycięciu k drzew, liczba jabłek które zostały,
dawały określoną resztę z dzielenia przez m. Jeżeli jest to możliwe dla i-1 drzew po wycięciu k drzew z resztą z dzielenia przez m równą j, to również jest możliwe
z taką samą resztą z dzielenia dla i drzew po wycięciu k+1 drzew oraz dla i drzew po wycięciu k drzew z resztą z dzielenia równą (j+T[i])%m.
Na końcu sprawdzam jaka jest najmniejsza liczba k, aby po wycięciu takiej ilości drzew z sadu składającego się z n drzew reszta z dzielenia przez m wynosiła 0.
Złożoność czasowa i pamięciowa wynosi O(n^3)
'''

from kol3testy import runtests


def orchard(T, m):
    n = len(T)
    total_sum = sum(T)

    if total_sum % m == 0:
        return 0

    dp = [[float('inf')] * m for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for r in range(m):
            dp[i][r] = min(dp[i][r], dp[i - 1][r]+1)
            new_r = (r + T[i - 1]) % m
            dp[i][new_r] = min(dp[i][new_r], dp[i - 1][r])

    return dp[n][0]



def orchard1(T, m):
    n=len(T)
    results=[[[False for _ in range(m)] for _ in range(n)] for _ in range(n)]
    # i k j
    results[0][0][T[0]%m]=True
    results[0][1][0]=True
    for i in range(1,n):
        for k in range(i+1):
            for j in range(m):
                if results[i-1][k][j%m]:
                    results[i][k][(j+T[i])%m]=True
                    if k<n-1:
                        results[i][k+1][j%m]=True
    for k in range(n):
        if results[n-1][k][0]:
            return k



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
