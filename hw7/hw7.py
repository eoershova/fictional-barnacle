# эта программа использует словарь, который создает из файла verb.txt, поэтому он должен лежать в одной папке с ней

def lets_play_linguists():
    my_dict = {}
    new_text = []
    with open('verb.txt', encoding="utf-8") as f:
        text = f.read()
        text = text.replace(',', ' ')
    for line in text.split('\n'):
        if len(line.split()) == 5:
            new_text.append(line.split())
    for line in new_text:
        infinitive = line[0]
        participle = line[4]
        my_dict[participle] = infinitive
    return my_dict


def only_ed_forms():
    ed_forms = []
    print('введите полное название файла')
    filename = input()
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        punctuation = '.,&!@*()-?:;“”'
        trans_table = str.maketrans({x: None for x in punctuation})
        text = text.translate(trans_table)
        words = text.split()
    for line in words:
        if line.endswith('ed'):
            ed_forms.append(line)
    return ed_forms


def lets_compare_dict(ed_forms, my_dict):
    infinitives = []
    for line in ed_forms:
        if line in my_dict.keys():
            infinitives.append(my_dict[line])
        elif line.startswith('un'):
                line = line[2:]
                if line in my_dict.keys():
                    infinitives.append(my_dict[line])
        elif line.startswith('mis'):
                line = line[3:]
                if line in my_dict.keys():
                    infinitives.append(my_dict[line])
        elif line.startswith('be'):
                line = line[2:]
                if line in my_dict.keys():
                    infinitives.append(my_dict[line])
    return infinitives


def last_letter(infinitives):
    y_verb = []
    e_verb = []
    for line in infinitives:
        if line.endswith('y'):
            y_verb.append(line)
        elif line.endswith('e'):
            e_verb.append(line)
    return y_verb, e_verb


def final_answer(ed_forms, y_verb, e_verb):
    answer1 = len(ed_forms)
    answer2 = len(y_verb) + len(e_verb)
    print('кол-во форм на -ed', answer1)
    print('кол-во форм, образованых от глаголов на -y  или -e', answer2)


def main():
    my_dict = lets_play_linguists()
    ed_forms = only_ed_forms()
    infinitives = lets_compare_dict(ed_forms, my_dict)
    y_verb, e_verb = last_letter(infinitives)
    final_answer(ed_forms, y_verb, e_verb)


if __name__ == '__main__':
    main()
