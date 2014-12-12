m = float(input())/1000
VV = 0
if m <= 5:
    VV = int(m*10)
elif m <= 30:
    VV = int(m+50)
elif m <= 70:
    VV = int((m-30)/5 + 80)
else:
    VV = 89

if VV < 10:
    VV = '0' + str(VV)
print(VV)