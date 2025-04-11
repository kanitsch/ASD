from zad2testy import runtests

from collections import defaultdict

def double_prefix(L):
    # Zbiór wszystkich prefiksów z listy
    all_prefixes = set()
    
    # Zliczanie prefiksów
    prefix_count = defaultdict(int)
    for s in L:
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            all_prefixes.add(prefix)
            prefix_count[prefix] += 1
    
    # Znajdowanie prefiksów spełniających warunki
    result = []
    for prefix in all_prefixes:
        if prefix_count[prefix] >= 2:  # Prefiks pojawia się w co najmniej 2 napisach
            zero_added = prefix + '0'
            one_added = prefix + '1'
            if zero_added not in all_prefixes and one_added not in all_prefixes:
                result.append(prefix)
    
    return result



runtests(double_prefix)

