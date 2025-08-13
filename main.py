import random
from datetime import date

class Film:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen = 0):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen

    def play(self):
        self.liczba_odtworzen += 1

    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"
    
class Serial(Film):
    def __init__(self, tytul, rok_wydania, gatunek, numer_sezonu, numer_odcinka, liczba_odtworzen = 0):
        super().__init__(tytul, rok_wydania, gatunek, liczba_odtworzen)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def play(self):
        self.liczba_odtworzen += 1

    def __str__(self):
        return f"{self.tytul} S{self.numer_sezonu:02}E{self.numer_odcinka:02}"

## FUNKCJE

def get_movies():
    """Zwraca listę filmów w porządku alfabetycznym"""
    return sorted([item for item in biblioteka if isinstance(item, Film) and not isinstance(item, Serial)], key = lambda x: x.tytul)

def get_series():
    """Zwraca listę seriali w porządku alfabetycznym"""
    return sorted([item for item in biblioteka if isinstance(item, Serial)], key = lambda x: x.tytul)

def search(tytul):
    """Wyszukuje element w bibliotece po tytule."""
    return [item for item in biblioteka if item.tytul.lower() == tytul.lower()]

def generate_views():
    """Losowo wybiera tytuł z biblioteki i zwiększa jego liczbę odtworzeń o losową wartość z zakresu 1–100."""
    if not biblioteka:
        return
    item = random.choice(biblioteka)
    item.liczba_odtworzen += random.randint(1, 100)

def run_generate_views(n=10):
    """Uruchamia generate_views n razy."""
    for i in range(n):
        generate_views()

def top_titles(n=3, content_type=None):
    """
    Zwraca n najpopularniejszych tytułów.
    content_type: None = wszystko, 'film' = filmy, 'serial' = seriale
    """
    if content_type == "film":
        data = get_movies()
    elif content_type == "serial":
        data = get_series()
    else:
        data = biblioteka

    return sorted(data, key=lambda x: x.liczba_odtworzen, reverse=True)[:n]

def add_full_season(tytul, rok, gatunek, numer_sezonu, licznik_odcinkow):
    """Dodaje pełny sezon serialu do biblioteki."""
    for odcinek in range(1, licznik_odcinkow + 1):
        biblioteka.append(Serial(tytul, rok, gatunek, numer_sezonu, odcinek))

def count_episodes(tytul_serialu):
    """Zwraca liczbę odcinków danego serialu w bibliotece."""
    return sum(1 for item in biblioteka if isinstance(item, Serial) and item.tytul.lower() == tytul_serialu.lower())

## LISTA DO PRZECHOWYWANIA BIBLIOTEKI FILMÓW   
biblioteka = []

## CZĘŚĆ GŁÓWNA PROGRAMU 
if __name__ == "__main__":
    print("Biblioteka filmów:")

    # dodanie 2 filmów do biblioteki
    biblioteka.append(Film("Pulp Fiction", 1994, "Kryminalny"))
    biblioteka.append(Film("The Matrix", 1999, "Sci-Fi"))

    # dodatnie 2 seriali do biblioteki
    biblioteka.append(Serial("The Simpsons", 1989, "Komedia", 1, 1))
    biblioteka.append(Serial("The Simpsons", 1989, "Komedia", 1, 2))

    # wykorzystanie funkcji do dodania pełnego sezonu serialu
    add_full_season("Breaking Bad", 2008, "Kryminalny", 1, 7)

    # wygenerowanie wyświetleń
    run_generate_views(10)

    # funkcja wyświetlająca najpopularniejsze filmy i seriale danego dnia
    today = date.today().strftime("%d.%m.%Y")
    print(f"\nNajpopularniejsze filmy i seriale dnia {today}:")
    for item in top_titles(3):
        print(f"{item} - {item.liczba_odtworzen} odtworzeń")

    # funkcja zliczająca odcinki serialu
    print(f"\nLiczba odcinków 'Breaking Bad' w bibliotece: {count_episodes('Breaking Bad')}")