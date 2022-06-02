from collections import deque

head = str(input("Введите названия файла\n"))

try:
    inf = open(head, "r")

    with inf as f:
            for row in deque(f, 10):
                print (row.strip())
except FileNotFoundError:
     print("Файла не существует")