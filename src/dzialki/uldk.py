"""Pobieranie geometrii działek z usługi ULDK (GUGiK)."""
import requests
from shapely import wkt

ULDK_URL = "https://uldk.gugik.gov.pl/"


class BladULDK(Exception):
    """Zgłaszany, gdy usługa nie zwróci poprawnej odpowiedzi."""


def pobierz_dzialke(identyfikator: str, timeout: int = 15):
    """Zwraca geometrię działki (układ EPSG:2180, metry).

    identyfikator: np. "141201_1.0001.6509"
    """
    params = {
        "request": "GetParcelById",
        "id": identyfikator,
        "result": "geom_wkt",
        "srid": "2180",
    }
    odpowiedz = requests.get(ULDK_URL, params=params, timeout=timeout)
    odpowiedz.raise_for_status()

    linie = odpowiedz.text.strip().splitlines()
    # Pierwsza linia to kod statusu: 0 oznacza błąd, 1 oznacza sukces.
    if not linie or linie[0].strip() != "0":
        opis = linie[0] if linie else "pusta odpowiedź"
        raise BladULDK(f"ULDK zwróciło błąd: {opis}")
    if len(linie) < 2:
        raise BladULDK("ULDK nie zwróciło geometrii działki")

    tekst = linie[1].strip()
    # Odpowiedź może mieć prefiks "SRID=2180;", który trzeba usunąć.
    if tekst.upper().startswith("SRID="):
        tekst = tekst.split(";", 1)[1]
    return wkt.loads(tekst)
