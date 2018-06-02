import re


def reader():
    print('введите название файла')
    filename = input()
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def word_finder(text):
    new_text = re.sub('философи', 'астрологи', text)
    new_text = re.sub('Философи', 'Астрологи', new_text)
    new_text = re.sub('Филосо́фи', 'Астроло́ги', new_text)
    new_text = re.sub('ФИЛОСОФИ', 'АСТРОЛОГИ', new_text)
    new_text = re.sub('φιλοσοφί', 'ἀστρολογί', new_text)
    with open("astrology.htm", "w", encoding="utf-8") as f:
        f.write(new_text)


def main():
    text = reader()
    word_finder(text)


if __name__ == "__main__":
    main()
