#a и b в сумме дают c
#a разделить на b равно c
a = int(input())
b = int(input())
c = int(input())

if a + b == c:
    print('a и b дают в сумме с')
else:
    print('a и b не дают в сумме с')
if a // b == c:
    print('a разделить на b равно c')
else:
    print('a разделить на b не равно c')
