sel = int(input("입력 진수 결정(16/10/8/2): "))
num = input("값 입력: ")

if sel == 16:
    num10 = int(num, 16)
if sel == 10:
    num10 = int(num, 10)
if sel == 8:
    num10 = int(num, 8)
if sel == 2:
    num10 = int(num, 2)

print("16 진수 ", hex(num10))
print("10 진수 ", num10)
print("8 진수 ", oct(num10))
print("2 진수 ", bin(num10))
