import socket as sck


host_ip = "192.168.88.75"
server_port = 4000     # server port number

c = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    # instantiate

print("Enter 'exit' to end the connection")
msg = input("->")   # take input

while True:

    c.sendto(msg.encode(), (host_ip, server_port))    # send message

    data = c.recv(4096)    # receive message

    print(f"Received from server: {data.decode()}")   # show response

    msg = input("->")   # again take input

    if msg == "exit":
        c.sendto(bytes(msg, 'utf-8'), (host_ip, server_port))  # send message
        print("Close the connection")
        break

c.close()   # close the connection


