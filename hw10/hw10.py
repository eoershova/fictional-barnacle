import re


def f():
    print('Введите полное имя файла')
    filename = input()
    with open(filename, 'r', encoding='utf-8') as a:
        b = a.read()
    return b


def finder(b):
    found = re.findall('Научная\sсфера</th><td>\n<p><span.*title="([А-Яа-я\s]*)', b)
    print('Научная сфера', found)


def main():
    b = f()
    finder(b)


if __name__ == "__main__":
    main()
