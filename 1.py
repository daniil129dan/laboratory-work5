head = str(input("Введите названия файла\n"))
try:
     inf = open(head, "r")
     num = 1
     line = inf.readline()
     while line != '' and num != 11:
          line = line.rstrip()
          print(num,': ',line)
          num += 1
          line = inf.readline()
     inf.close()
except FileNotFoundError:
     print("Файла не существует")
