# dzialki-pl

Małe narzędzie w Pythonie do pobierania geometrii działek ewidencyjnych
z publicznej usługi ULDK (GUGiK) i obliczania ich wymiarów.

## Co potrafi

- pobiera obrys działki po jej identyfikatorze lub współrzędnych,
- liczy powierzchnię, obwód, długości boków i szerokość frontu,
- działa jako biblioteka i z wiersza poleceń.

## Instalacja

pip install dzialki-pl

## Przykład użycia

from dzialki import pobierz_dzialke, wymiary

dzialka = pobierz_dzialke("141201_1.0001.6509")
print(wymiary(dzialka))

## Źródła danych i zastrzeżenia

Dane pochodzą z publicznej usługi ULDK udostępnianej przez GUGiK.
Wyniki mają charakter orientacyjny i nie zastępują mapy do celów
projektowych ani opinii geodety. Prosimy o rozsądne korzystanie
z usługi i przestrzeganie jej limitów zapytań.

## Licencja

MIT
