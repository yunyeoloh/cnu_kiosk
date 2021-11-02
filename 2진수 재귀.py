#5-2
num = float(input("숫자를 입력하세요 : "))
a = []
b = []
def mb(num):
    num = int(num)
    if num%2 == 1:
        a.append(1)
        num = (num-1)/2
    else:
        a.append(0)
        num /= 2
    if num != 0:
        mb(num)
def mb2(num):
    num = num - int(num)
    if int(num* 2) == 1:
        b.append(1)
        num =  (num * 2) - 1
    else:
        b.append(0)
        num *=2
    if len(b) < 10:
        mb2(num)

mb(num)
for i in a[::-1]:
    print(i,end = "")
print(".",end = "")
mb2(num)
for i in b:
    print(i,end = "")
