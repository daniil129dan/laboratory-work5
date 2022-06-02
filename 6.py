boysnames = []
girlsnames = []
a = 112

for i in range(a):
    boy = str('BabyNames/'+str(1900+i)+'_BoysNames.txt')
    z = open(boy, "r").readlines()
    boysnames.append(z[0].split(' ')[0])

    girl = str('BabyNames/'+str(1900+i)+'_GirlsNames.txt')
    v = open(girl, "r").readlines()
    girlsnames.append(v[0].split(' ')[0])

print('Введите диапазон поиска популяроных имен: ')
p = int(input())
r = int(input())
b = 0
c = 0
bname = boysnames[p]
gname = girlsnames[p]

for p in range(r):
    if bname == boysnames[p]:
        b +=1

    if gname == girlsnames[p]:
        c +=1

if b >= r//p:
    print(boysnames[p])
else:
    print(boysnames[r])

if c >= r//p:
    print(girlsnames[r])
else:
    print(girlsnames[r])

print(boysnames)
print(girlsnames)