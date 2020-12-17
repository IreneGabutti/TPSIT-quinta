import socket as sck


def server():

    # get the hostname
    host = "192.168.88.91"
    port = 4000     # initiate port

    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    # get instance

    s.bind((host, port))    # bind host address and port

    while True:

        data, address = s.recvfrom(4096)    # receive message
        data = data.decode()
        print(f"from connected user:  {data}")

        if not data or data == "exit":
            # if data is not received or data is the word 'exit' to end the connection break
            print("Close the connection")
            break

        s.sendto(data.encode(), address)    # send data to the client

    s.close()    # close the connection


if __name__ == '__main__':
    server()
