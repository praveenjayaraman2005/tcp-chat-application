import socket

client = socket.socket()
client.connect(('127.0.0.1', 5000))
print("Connected to server. Type 'exit' to stop.\n")

while True:
    # Send message
    msg = input("You: ")
    client.send(msg.encode())

    if msg.lower() == "exit":
        print("Chat ended.")
        break

    # Receive reply from server
    reply = client.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == "exit":
        print("Server ended the chat.")
        break

client.close()
