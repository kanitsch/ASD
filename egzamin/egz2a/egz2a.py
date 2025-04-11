from egz2atesty import runtests

'''
Karolina Nitsch 421767
Algorytm polega na uzupełnianiu tablicy F, w której F[i][j] oznacza minimalny koszt potrzebny na połączenie wejść od i do j.
Dla sąsiednich i, j jest to koszt kabla łączącego te dwa wejścia, a jeżeli i oraz j nie sąsiadują ze sobą, to wartość funkcji obliczam
jako minimum kosztu połączenia wejścia j z każdym możliwym wejściem (k) od i do j-1 plus połączenia wejść od i do k-1 oraz od k+1 do j-1.
W pętli wewnątrz funkcji jest iterowanie co 2, ponieważ nie da się połączyć nieparzystej ilości wejść.
Złożoność czasowa wynosi O(n^3), pamięciowa O(n^2)
'''


def wired(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]

    # for i in range(n - 1):
    #   F[i][i + 1] = abs(T[i] - T[i + 1]) + 1

    def uzup(i, j):
        if i > j:
            return 0

        if F[i][j] < float('inf'):
            return F[i][j]

        if i == j - 1:
            F[i][i + 1] = abs(T[i] - T[i + 1]) + 1
            return F[i][j]

        # F[i][j] = uzup(i, j - 2) + abs(T[j - 1] - T[j]) + 1
        for k in range(i, j, 2):
            F[i][j] = min(uzup(i, k - 1) + uzup(k + 1, j - 1) + abs(T[k] - T[j]) + 1, F[i][j])
        return F[i][j]

    return uzup(0, n - 1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wired, all_tests=True)
