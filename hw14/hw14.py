def reader():
    print('введите название файла')
    filename = input()
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        extra_punctuation = '?!\n'              # если честно, то непонятно, что делать с диалогами
        phrase_punctuation = '-,:;“”"—'
        word_punctuation = "'"                  # для английских текстов, чтоб считать слова с апострофами нормально
    for x in extra_punctuation:
        text = text.replace(x, '.')
    for x in phrase_punctuation:
        text = text.replace(x, ' ')
    for x in word_punctuation:
        text = text.replace(x, '')
    return text


def sentence_splitter(text):
    sentences = text.split('.')
    dictionary = {i: {word: len(word) for word in i.split()} for i in sentences}
    for key, value in dictionary.items():
        print(key, value)


def main():
    text = reader()
    sentence_splitter(text)


if __name__ == "__main__":
    main()
