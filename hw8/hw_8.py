from collections import defaultdict


def dictionary_maker():
    d = defaultdict(list)
    with open('words.csv', 'r', encoding='utf-8') as f:
        for line in f:
            sp = line.strip().split(';')
            if len(sp) != 2:
                continue
            d[sp[0]].append(sp[1])
    return d


def riddles(d):
    n = 0
    w = 0
    print('начало игры "угадайте существительное по словосочетанию"')
    for i in d:
        the_word = i
        for x in range(0, len(d[i])):
            clue = d[i][x]
            print(clue, '.' * len(clue))
            print('ваша догадка?')
            guess = input()
            if guess == the_word:
                w += 1
                if n + w == len(d) and w >= 1:
                    print('Поздравляю, игра окончена и вы даже что-то угадали')
                else:
                    print('круто! вы угадали; переходим к следующему слову')
                    break
            else:
                if x < len(d[i]) - 1:
                    print('НЕТ. попробуйте угадать это же слово еще раз')
                elif x == len(d[i]) - 1 and n + w != len(d) - 1:
                    print('все еще нет, давайте попробуем другое слово')
                    n += 1
                elif n + w == len(d) - 1 and w >= 1:
                    print('Поздравляю, игра окончена и вы даже что-то угадали')
                else:
                    print('НЕТ. Игра окончена.')


def main():
    d = dictionary_maker()
    riddles(d)


if __name__ == "__main__":
    main()
