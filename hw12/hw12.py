import os
import re


def file_finder():
    files = []
    directories = []
    for i in os.listdir():
        if os.path.isfile(i):
            files.append(i)
        elif os.path.isdir(i):
            directories.append(i)
    return files, directories


def is_this_latinitsa(files):
    latinitsa = r'[^A-Za-z]'
    number_of_files = 0
    lat_name_files = []
    for i in files:
        if re.search(latinitsa, i):
            continue
        else:
            number_of_files += 1
            lat_name_files.append(i)
    return number_of_files


def final_answer(number_of_files, files, directories):
    print('найдено файлов, название которых состоит только из латинских символов:', number_of_files)
    print('папки:', ', '.join(directories))
    print('файлы:', ', '.join(files))


def main():
    files, directories = file_finder()
    number_of_files = is_this_latinitsa(files)
    final_answer(number_of_files, files, directories)


if __name__ == "__main__":
    main()
