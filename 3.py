import os.path
head = str(input("Введите первого файла\n"))
head1 = str(input("Введите второго файла\n"))
head2 = str(input("Введите название файла в котором хотите объеденить файлы\n"))

if (os.path.exists(head) == True) and (os.path.exists(head1) == True) and (os.path.exists(head2) == True):
    open(head2,"w").write(open(head,"r").read() + open(head1,"r").read())

else:
    if os.path.exists(head) == False:
        print('файла с именем',head,'не существует')

    if os.path.exists(head1) == False:
        print('файла с именем',head1,'не существует')

    if os.path.exists(head2) == False:
        print('файла с именем',head2,'не существует')
