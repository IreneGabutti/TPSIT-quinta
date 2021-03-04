import socket as sck
ip = '127.0.0.1'
port = 5000
s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)

s.connect((ip,port))
method = "POST"
url= "http://127.0.0.1:5000/log"
host="Host: http://127.0.0.1:5000"
content_type="Content_type: application/x-www-form-urlencoded"

version = "HTTP/1.1"
body = "username=paolo&password=come_stai"
content_length= f"Content_lenght: {len(body)}"


richiesta= method + " " + url + " " + version + "\n" + host + "\n" + content_type + "\n" + content_length + "\n" + "\n" + body

print(richiesta)  
s.sendall(richiesta.encode())
print(s.recv(4096).decode())