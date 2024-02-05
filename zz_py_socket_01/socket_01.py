import socket

TCP_IP      = '169.254.4.61'  # or whatever address you'll find on the E4980A screen
TCP_PORT    = 5025
BUFFER_SIZE = 1024


#%%

def query(cmd):
    s.send(bytes(cmd+"\r\n",'ansi'))
    return s.recv(BUFFER_SIZE).decode('utf8')


#%%

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3.0)
s.connect((TCP_IP, TCP_PORT))

print(query("*IDN?"))

s.close()
### end of script