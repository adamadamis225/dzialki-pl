"""Obliczanie wymiarów działki na podstawie jej obrysu."""
from math import hypot


def _boki(wielokat):
    punkty = list(wielokat.exterior.coords)
    return [
        hypot(x2 - x1, y2 - y1)
        for (x1, y1), (x2, y2) in zip(punkty, punkty[1:])
    ]


def wymiary(geometria) -> dict:
    """Zwraca słownik z wymiarami działki (metry i metry kwadratowe)."""
    if geometria.geom_type == "MultiPolygon":
        # Działka z kilku części: bierzemy największą do obliczeń boków.
        glowna = max(geometria.geoms, key=lambda g: g.area)
    else:
        glowna = geometria

    prostokat = glowna.minimum_rotated_rectangle
    krawedzie = sorted(_boki(prostokat)[:2])

    return {
        "powierzchnia_m2": round(geometria.area, 2),
        "obwod_m": round(geometria.length, 2),
        "liczba_bokow": len(_boki(glowna)),
        "szerokosc_frontu_m": round(krawedzie[0], 2),
        "glebokosc_m": round(krawedzie[1], 2),
        "boki_m": [round(b, 2) for b in _boki(glowna)],
    }
