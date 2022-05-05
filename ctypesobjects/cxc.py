from ctypes import *

charptr = POINTER(c_char)

test = CDLL('test.so')
test.initializetest.argtypes = []
test.initializetest.restype = charptr
test.searchtest.argtypes = [charptr]
test.searchtest.restype = c_int

buf = test.initializetest()
test.searchtest(buf)
print cast(buf, c_char_p).value