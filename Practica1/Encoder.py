import sys
from Helper import *

def cipher(func, numbytes, key=None):
    if key == None:
        key = get_caesar_key() if func == "caesar" else get_affine_key()
    enc = []
    for x in numbytes:
        if func == "caesar":
            val = caesar(x, key)
        else:
            val = affine(x, key[0], key[1])
        enc.append(val.to_bytes(1, 'big'))
    return enc
    
def caesar(x, k):
    return (x + k) % 256

def affine(x, a, b):
    return (a*x + b) % 256
        
if __name__ == '__main__':
    f = open(sys.argv[2], 'rb') #File name.
    filebytes = []
    byte = f.read(1)
    while byte:
        filebytes.append(byte[0])
        byte = f.read(1)
    if sys.argv[2] == "final.txt":
        filename = "file3.enc"
        output = cipher("caesar", filebytes, 1)
    elif sys.argv[2] == "garfield.jpg":
        filename = "file1.enc"
    else:
        filename = "file2.enc"
    output = cipher(sys.argv[1], filebytes)
    fo = open(filename, 'wb')
    for byte in output:
        fo.write(byte)
    fo.close()
