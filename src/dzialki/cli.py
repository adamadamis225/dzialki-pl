# src/dzialki/cli.py
import argparse
import json

from .uldk import pobierz_dzialke, BladULDK
from .geometria import wymiary


def main():
    parser = argparse.ArgumentParser(
        description="Wymiary działki ewidencyjnej na podstawie danych ULDK"
    )
    parser.add_argument("identyfikator", help="np. 141201_1.0001.6509")
    args = parser.parse_args()

    try:
        wynik = wymiary(pobierz_dzialke(args.identyfikator))
    except BladULDK as blad:
        raise SystemExit(f"Błąd: {blad}")
    print(json.dumps(wynik, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
