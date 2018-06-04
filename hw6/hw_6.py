# хайку на немецком
import random


def read_words_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        words = text.split(', ')
    return words


def article():
    articles = read_words_from_file('articles.txt')
    return random.choice(articles)


def noun():
    nouns = read_words_from_file('nouns.txt')
    return random.choice(nouns)


def preposition():
    prepositions = read_words_from_file('prepositions.txt')
    return random.choice(prepositions)


def adjective():
    adjectives = read_words_from_file('adjectives.txt')
    return random.choice(adjectives)


def another_noun():
    nouns_2 = read_words_from_file('nouns_set_2.txt')
    return random.choice(nouns_2)


def pronoun():
    pronouns = read_words_from_file('pronouns.txt')
    return random.choice(pronouns)


def verb():
    verbs = read_words_from_file('verbs.txt')
    return random.choice(verbs)


def modifier():
    modifiers = read_words_from_file('modifiers.txt')
    var = random.choice(modifiers)
    if var == 'gar':
        return var + ' ' + 'nicht'
    elif var == 'ganz':
        return var + ' ' + 'gern'
    else:
        another_modifier = read_words_from_file('modifiers_set_2.txt')
        return var + ' ' + '' + random.choice(another_modifier)


def verse1():
    return article() + ' ' + noun()


def verse2():
    return preposition() + ' ' + adjective() + ' ' + another_noun()


def verse3():
    return pronoun() + ' ' + verb() + ' ' + modifier()


def main():
    print(verse1())
    print(verse2())
    print(verse3())


if __name__ == '__main__':
    main()
