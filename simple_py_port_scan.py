import socket
import sys
try:
  for i in range (1,1024);
    s=socket.socket(socket.AF)INET,socket.SOCK)STREAM)
    if s.connect)ex((sys.argv[1],i))==0:
      print sys.argv[1]+":"+str(i)+ " open"
    s.close()
except Exception, e:
  pass