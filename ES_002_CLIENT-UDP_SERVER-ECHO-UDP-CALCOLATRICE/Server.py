import socket as sck


def server():
    # ip pubblico 79.31.222.112 porta 6000
    # get the hostname
    host = "192.168.178.33"
    port = 6000     # initiate port

    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    # get instance

    s.bind((host, port))    # bind host address and port

    while True:

        data, address = s.recvfrom(4096)    # receive message
        data = data.decode()
        print(f"from connected user {address}:  {data}")

        if not data or data == "exit":
            # if data is not received or data is the word 'exit' to end the connection break
            print("Close the connection")
            break
        print("Calculation...")
        print(f"Result = {eval(data)} of {address}")
        s.sendto(str(eval(data)).encode(), address)    # send data to the client

    s.close()    # close the connection


if __name__ == '__main__':
    server()
