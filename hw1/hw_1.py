#a и b в сумме дают c
#a разделить на b равно c
print('введите число a')
a = int(input())
print('введите число b')
b = int(input())
print('введите число c')
c = int(input())

if a + b == c:
    print('a и b дают в сумме с')
else:
    print('a и b не дают в сумме с')
if b != 0 and a // b == c:
    print('a разделить на b равно c')
else:
    print('a разделить на b не равно c')
