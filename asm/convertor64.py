import binascii
string = "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"
i = 0
p = ""
while i < len(string):
    data = "0x" + binascii.hexlify(string[i:i+8][::-1].encode()).decode().rjust(16, '0')
    p = "mov rbx, " + data + "\npush rbx\n" + p
    i += 8
print(p)