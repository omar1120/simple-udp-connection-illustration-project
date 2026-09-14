#client
import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Client is running.")
data = "hello server set my time"
msg = data.encode("UTF-8")
s.sendto(msg, ("127.0.0.1", 5550))
Rmsg, add = s.recvfrom(1024)
Rmsg = str(Rmsg.decode("UTF-8"))
print("current time is:",Rmsg)

s.close()