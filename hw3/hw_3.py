#abracadabra
#aabracadabr
#raabracadab
#braabracada
#abraabracad
#dabraabraca
#adabraabrac
#cadabraabra
#acadabraabr
#racadabraab
#bracadabraa
print('введите последовательность букв или цифр без разделеителй')
letters = list(input())
x = len(letters)
# x is len_letters
print(''.join(letters))
while x > 1:
    last_letter = letters[-1]
    letters.insert(0, last_letter)
    letter = letters.pop()
    print(''.join(letters))
    x -= 1
