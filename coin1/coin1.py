import socket
import re

n_find = re.compile("N=(\d+)")


def alg(i, j):
    s1 = ""
    a = range(i, j)
    k = int((i + j) / 2)
    for ia in a[:int(len(a) / 2)]:
        s1 += str(ia) + " "
    if j - i > 1:
        s.send((s1 + "\n").encode())
    else:
        s.send((str(i) + "\n").encode())
    rec = s.recv(7).decode().replace("\n", "")
    if rec.startswith("Correct"):
        return
    elif int(rec) % 10 != 0:
        alg(i, k)
        return
    elif int(rec) % 10 == 0:
        alg(k, j)
        return
    return


s = socket.socket()
s.connect(("pwnable.kr", 9007))
bla = s.recv(2048).decode()
while True:
    data = s.recv(20).decode()
    if "!" in data:
        data = s.recv(20).decode()
    c = n_find.findall(data)
    if len(c) > 0:
        n = c[0]
        print(n)
        alg(0, int(n))
    else:
        print(data)
        break;
s.close()
