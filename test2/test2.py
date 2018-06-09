import re
import collections

def file_reader():
    with open('mystem.xml', 'r', encoding='utf-8') as f:
        text = f.read()
    #print(text)
    return text


def body_counter(text):
    found = re.findall('<body>([\s\S]*)</body>', text)
    answer = len(str(found))
    with open("answer_task_1.txt", "w", encoding="utf-8") as f:
        f.write(str(answer))
    return found


def dictionary_maker(text):
    dictionary = collections.Counter()
    word = re.findall('gr="([^"]*)"', text)
    dictionary.update(word)
    #print(dictionary)
    with open("answer_task_2.txt", "w", encoding="utf-8") as f:
        for item in dictionary:
            f.write("%s\n" % item)


def verb_finder(text):
    verbs = re.findall('<w><ana lex="[^"]*" gr="V([^"]*)"', text)
    no_perf = r'несов'
    perf = r'сов'
    single = r'ед'
    answer = 0
    for verb in verbs:
        if re.search(no_perf, verb):
            continue
        elif re.search(perf, verb) and re.search(single, verb):
            answer +=1
    print(answer)




def main():
    text = file_reader()
    body_counter(text)
    dictionary_maker(text)
    verb_finder(text)

if __name__ == "__main__":
    main()
























#mystem.xml