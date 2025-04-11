import sys

def test_max_array_size():
    element_size = sys.getsizeof(1)  # Rozmiar jednego elementu int w bajtach
    available_memory = 20*1024**3  # Zakładamy, że mamy 6 GB dostępnej pamięci

    max_elements = available_memory // element_size
    print(f"Próbujemy utworzyć tablicę o rozmiarze: {max_elements} elementów")

    try:
        large_array = [1] * max_elements
        print("Tablica utworzona pomyślnie")
    except MemoryError:
        print("Nie udało się utworzyć tablicy - błąd pamięci")

if __name__ == "__main__":
    test_max_array_size()
