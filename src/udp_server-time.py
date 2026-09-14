#server
import socket
from datetime import datetime

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 5550))
print("UDP Server is up and running.")
msg, addr = s.recvfrom(1024)
print("msg: ",msg.decode("UTF-8"), " addr: ",addr)
time = str(datetime.now())
response = time.encode("UTF-8")
s.sendto(response, addr)

s.close()