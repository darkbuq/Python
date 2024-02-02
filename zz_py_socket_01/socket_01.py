import socket
s = socket.socket()
print("connecting")
s.connect(("169.254.37.237",5024))
print("sending")
s.settimeout(10)
s.send("*IDN?\r\n")
print(s.recv(2048))