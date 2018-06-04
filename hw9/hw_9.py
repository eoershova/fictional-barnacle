import re


def text_prep():
    print('название файла')
    with open(input(), 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        text = re.sub(r'[^а-я ]', ' ', text)
    return text


def forms_finder(text):
    verb_infinitive = set(re.findall('выпить', text))
    verb_future_forms = set(re.findall('выпь(?:ю|ешь|ем|ет|ют)', text))
    verb_past_forms = set(re.findall('выпил[а-я]*', text))
    verb_participle_active = set(re.findall('выпивш[а-р,т-я]{2,3}', text))
    verb_participle_pass = set(re.findall('выпит[а-ы,э-я]{0,3}', text))
    verb_participle_transgressive = set(re.findall('выпив\s|выпимши', text))
    verb_reflexive_past_forms = set(re.findall('выпил[а-я]*(?:ся|сь)', text))
    verb_reflexive_participle_active = set(re.findall('выпивш[а-р,т-я]{2,3}(?:ся|сь)', text))
# похоже, форм настощего времени и возвратных форм пассивного залога не существует
# set() превращает список в беспорядочную коллекцию дистинктных обьетов, т е убирает повторения
    print('инфинитив:', "\t".join(verb_infinitive))
    print('формы глагола в будущем времени:',"\t".join(verb_future_forms))
    print('формы глагола в прошедшем времени:',"\t".join(verb_past_forms))
    print('формы действительных причастий:',"\t".join(verb_participle_active))
    print('формы страдательных причастий:',"\t".join(verb_participle_pass))
    print('деепричатия:',"\t".join(verb_participle_transgressive))
    print('возвратные формы глагола в прошедшем времени:',"\t".join(verb_reflexive_past_forms))
    print('возвратные формы действительных причастий:',"\t".join(verb_reflexive_participle_active))


def main():
    text = text_prep()
    forms_finder(text)


if __name__ == "__main__":
    main()

#test2.txt
