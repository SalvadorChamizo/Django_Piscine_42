import sys
sys.path.insert(0, 'local_lib')

from path import Path


def main():
    base = Path('.')
    folder = base / 'data'

    if not folder.is_dir():
        folder.mkdir()

    file = folder / 'file.txt'

    if not file.is_file():
        file.touch()

    file.write_text("Hello, world!\n")
    file.write_text("Another line\n", append=True)

    for line in file.lines():
        print(line.strip())


if __name__ == '__main__':
    main()
