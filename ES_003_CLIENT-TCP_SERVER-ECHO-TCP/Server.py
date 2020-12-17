import socket as sck


def server():
    # get the hostname
    host = "127.0.0.1"
    port = 6000  # initiate port

    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # get instance

    s.bind((host, port))  # bind host address and port

    s.listen()  # number of client can listen simultaneously

    conn, address = s.accept()  # accept new connection
    print(f"onnection from: {address}")

    while True:

        data = conn.recv(1024).decode()  # receive data
        print(f"from connected user {address}:  {data}")

        if not data or data == "exit":
            # if data is not received or data is the word 'exit' to end the connection break
            print("Close the connection")
            break

        conn.sendall(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server()
