from shapely.geometry import Polygon

from dzialki.geometria import wymiary


def test_prostokat_20_na_50():
    dzialka = Polygon([(0, 0), (20, 0), (20, 50), (0, 50)])
    wynik = wymiary(dzialka)
    assert wynik["powierzchnia_m2"] == 1000.0
    assert wynik["obwod_m"] == 140.0
    assert wynik["szerokosc_frontu_m"] == 20.0
    assert wynik["glebokosc_m"] == 50.0
    assert wynik["liczba_bokow"] == 4
