text = []
print('введите латинское слово. всё кончится, если вы введете пустое слово')
a = 'hey'
infinitives = []
while a != '':
    a = (input())
    text.append(a)
length = len(text)
# -are -ere ire ari eri iri - окончания латинских инфинитивов
for x in range(length):
    word = text[x]
    if (len(word) >= 4) and word.endswith(('ere', 'ire', 'are')):
        infinitives.append(word)
    if (len(word) >= 4) and word.endswith(('ari', 'eri', 'iri')):
        infinitives.append(word)

with open("lat_inf.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(infinitives))
