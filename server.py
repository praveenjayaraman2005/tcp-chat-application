import socket

server = socket.socket()
server.bind(('127.0.0.1', 5000))
server.listen(1)
print("Server waiting for client...")

client_socket, addr = server.accept()
print("Connected to:", addr)

while True:
        
        # Receive message from client
        msg = client_socket.recv(1024).decode()
        print("Client:", msg)

        # Exit condition
        if msg.lower() == "exit":   
            print("Client ended the chat.")
            break

        # Send reply
        reply = input("You: ")
        client_socket.send(reply.encode())

        if reply.lower() == "exit":
            print("Chat ended.")
            break

client_socket.close()
server.close()
