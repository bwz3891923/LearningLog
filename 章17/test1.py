import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

x='This works! \U0001F44D'
print(x.translate(non_bmp_map))
