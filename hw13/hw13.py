import os
import collections
import re


def folder_finder():
    start_path = '.'
    letter = collections.Counter()
    not_letter = r'[^A-Za-z]'
    for root, dirs, files in os.walk(start_path):
        for directory in dirs:
            if re.search(not_letter, directory[0]):
                continue
            else:
                letter.update(directory[0])
    return letter


def answer_giver(letter):
    answer = list(letter.most_common(1)[0])
    print('название большинства папок начинается на букву', answer[0])


def main():
    letter = folder_finder()
    answer_giver(letter)


if __name__ == "__main__":
    main()
