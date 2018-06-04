#my version also works, but this one is more elegant and fast
def reader():
    with open('Ozhegov.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        d = text.splitlines()
    return d


def word_finder(d):
    for line in d:
        slovo = line.split('|')[0]
        if slovo.startswith('кин') and slovo.endswith('т'):
                print(slovo)


def anton_finder(d):
    anton = 0
    for line in d:
        anton_word = line.split('|')[2]
        #print(anton_word)
        if len(anton_word) > 0:
            anton += 1
    print('число антонимов:', anton)


def process_word(word, d):
    for line in d:
        if line.split('|')[0] == word:
            definition = line.split('|')[1]
            example = line.split('|')[3]
            print(len(word), definition, example, sep=':')
            return
        else:
            continue
    print('слово не нашлось')


def ozhegov_interactive(d):
    print('введите слова через пробел')
    user_words = input()
    words = user_words.split(' ')
    for word in words:
        #print(word)
        process_word(word, d)

# катод кинопрокат кот мям
def main():
    d = reader()
    word_finder(d)
    anton_finder(d)
    ozhegov_interactive(d)


if __name__ == "__main__":
    main()
