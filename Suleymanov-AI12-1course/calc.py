
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
print("1 = +, 2 = -, 3 = *, 4 = /, 5 = **, 6 = %, 7 = // ")
g = int(input("Выберите операцию: "))
if g == 1:
    print(a+b)
if g == 2:
    print(a-b)
if g == 3:
    print(a*b)
if g == 4:
    print(a/b)
if g == 5:
    print(a**b)
if g == 6:
    print(a%b)
if g == 7:
    print(a//b)
if g != 1 and g != 2 and g != 3 and g != 4 and g != 5 and g != 6 and g != 7:
    print("Нет")
    