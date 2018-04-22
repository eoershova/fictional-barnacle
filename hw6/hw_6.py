# хайку на немецком
import random


def article():
    articles = ['Meine', 'Deine', 'Seine', 'Ihre', 'Keine', 'Kleine']
    return random.choice(articles)


def noun():
    nouns = ['Großmutter', 'Melodie', 'Malerei', 'Facette', 'Waagschale']
    return random.choice(nouns)


def adjective():
    adjectives = ['anatomischen', 'declarativen', 'demiurgischen', 'unerfindlichen', 'birnenförmigen', 'charakterlosen']
    return random.choice(adjectives)


def another_noun():
    nouns_2 = ['Baum', 'Bein', 'Bier', 'Freund', 'Zwerg', 'Maul', 'Haar']
    return random.choice(nouns_2)


def pronoun():
    pronouns = ['Mir', 'Ihm', 'Uns', 'Dir', 'Ihr']
    return random.choice(pronouns)


def modifier():
    modifiers = ['auch', 'ganz', 'gar']
    var =  random.choice(modifiers)
    if var == 'gar':
        return var + ' ' + 'nicht'
    elif var == 'ganz':
        return var + ' ' + 'gern'
    else:
        another_modifier = ['gern', 'ganz']
        return var + ' ' + '' + random.choice(another_modifier)



def verse1():
    return article() + ' ' + noun()


def verse2():
    return 'Mit' + ' ' + adjective() + ' ' + another_noun()


def verse3():
    return pronoun() + ' ' + 'gefällt' + ' ' + modifier()


def main():
    print(verse1())
    print(verse2())
    print(verse3())


if __name__ == '__main__':
    main()
