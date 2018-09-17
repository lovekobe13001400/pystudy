s = b'hello'

import binascii

#编码16进制原始字符串
h = binascii.b2a_hex(s)

print(h)


import base64

h = base64.b16encode(s)
print(h)

#解码
s = base64.b16decode(h)
print(s)
