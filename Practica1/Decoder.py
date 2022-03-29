import sys
from Helper import inverse

def decipher(func, numbytes, key):
    dec = []
    for x in numbytes:
        if func == "caesar":
            val = caesar(x, key)
        else:
            val = affine(x, key[0], key[1])
        dec.append(val.to_bytes(1, 'big'))
    return dec

def caesar(x, k):
    return (x - k) % 256

def affine(x, a, b):
    inv = inverse(a, 256) % 256
    subs = (x - b) % 256
    return (subs * inv) % 256

if __name__ == '__main__':
    f = open(sys.argv[2], 'rb')
    filebytes = []
    byte = f.read(1)
    while byte:
        filebytes.append(byte[0])
        byte = f.read(1)
    filename = sys.argv[2]+"_copy"
    if sys.argv[1] == "caesar":
        key = 185
    else:
        key = (211, 254)
    output = decipher(sys.argv[1], filebytes, key)
    fo = open(filename, 'wb')
    for byte in output:
        fo.write(byte)
    fo.close()
