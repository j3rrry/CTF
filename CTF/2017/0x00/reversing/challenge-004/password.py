extrac = '01 16 79 44 04 64 12 5A  01'.split()
extrac = map(lambda x: int(x,16), extrac)
flag = '0x00CTF{'
flag = map(ord, flag)

password = ''.join([chr(i^j) for i,j in zip(extrac, flag)])

print password
