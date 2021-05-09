def main() -> None:
    print('A kocka térfogatát kiszámoló függvény!')
    a : float = float(input('a (él) = '))
    if a < 1:
        print('A megadott adattal nem lehet számolni!')
    else:
        kocka_terfogata: float = a * a * a
        print(f'A kocka_térfogata: {kocka_terfogata}')


if __name__ == "__main__":
    main()