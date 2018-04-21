#какой процент от общего количества слов не оканчивается знаком препинания (можно взять только запятую и точку)
a = 0
b = 0
# a - слово со знаком препинания, b - без знака
print('укажите путь к файлу. полный. пожалуйста.')
path = str(input())
with open(path, encoding="utf-8") as f:
    text = f.read()
    splited_text = text.split()
for line in splited_text:
        if line.endswith(',') or line.endswith('.'):
            a += 1
        else:
            b += 1

answer = (b / (a + b)) * 100
print(round(answer), '%')
