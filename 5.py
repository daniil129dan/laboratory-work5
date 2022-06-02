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

print(boysnames)
print(girlsnames)


