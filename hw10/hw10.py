import re


def f():
    print('Введите полное имя файла')
    filename = input()
    with open(filename, 'r', encoding='utf-8') as a:
        b = a.read()
    return b


def finder(b):
    found = re.findall('Научная\sсфера([\s\S]*?)</span>', b)
    answer = re.findall('title="([а-яА-яёЁ\s]*)', found[0])
    print(answer)


def main():
    b = f()
    finder(b)


if __name__ == "__main__":
    main()
