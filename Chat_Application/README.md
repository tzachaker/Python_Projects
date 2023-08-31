# Chat Application User Manual

Welcome to the user manual for the Chat Application repository. This guide outlines the functionality and usage of the Python-based chat application, which employs both TCP and UDP protocols. The repository comprises a server and a client component designed for seamless message and file exchange.

## Server
### System Requirements
- Python 3.x
  
### Overview
The server script (server.py) serves as the backbone of the chat application. It establishes a TCP socket, allowing it to listen for incoming connections from clients. Multiple clients can connect simultaneously, enabling them to engage in real-time conversations. The server takes note of all connected clients, storing their respective nicknames.

### Getting Started
To set up the chat server, execute the following command on your chosen machine:
python server.py

Upon execution, the server will display a message confirming its readiness to manage incoming connections. Clients can now establish connections using the provided client script.

### Supported Commands
The server is equipped to handle various commands from clients, including:

- broadcast: Sending messages to all connected clients.
- online: Requesting a list of clients currently online.
- user name,message: Sending private messages to specific users.
- files: Retrieving a list of available files on the server.
- download,<file_name>: Initiating the download of a file from the server.
  
### Important Note
For clients to connect from different devices, the server must be hosted on a machine with a publicly accessible IP address or domain name.

## Client
### System Requirements
- Python 3.x
- Tkinter (Python GUI library)
  
### Overview
The client script (client.py) offers an intuitive graphical interface powered by Tkinter. This interface allows clients to effortlessly connect to the chat server, communicate with other clients, request online client lists, and download shared files.

### Getting Started
Launch the client script on your machine using the following command:
python client.py

Upon execution, the script will prompt you to provide the IP address of the server. Leaving this field blank will result in a connection attempt to a local server. Enter your desired nickname and click the "Connect" button to join the chat.

Messaging is straightforward: use the input box to type messages. For directing messages to specific users, follow the format "person name,text" (e.g., "John,Hello John, how are you?").

Utilize the "Online List" button to obtain a list of online clients and the "Files List" button to retrieve a list of available server files. To download shared files, use the format "download,file_name.type" (e.g., "download,image.jpg").

### Essential Points
- The client script supports one connection at a time. For multiple clients, run separate instances of the script.
- Closing the application window will result in an automatic disconnection.
  
## UDP Section
In both server and client scripts, the UDP (User Datagram Protocol) section facilitates file transfer between the two components. UDP's inherent lack of connection requires a basic algorithm to ensure reliable data transfer:
- File Division: The server segments files into smaller packets, storing them as a list.
- UDP Sockets: Both server and client create two UDP sockets for sending and receiving data.
- UDP Send and Receive Loops: The server sends packets to the client, awaiting acknowledgment for each.
- ACK Mechanism: If acknowledgment doesn't occur within a timeout, the server retransmits packets.
- End of Transfer: The server dispatches a specific packet to signal the file transfer's completion.
- File Reconstruction: The client pieces together the file from received packets.
  
### Important Note:
While UDP suffices for some data transfer scenarios, its lack of certain features makes it less suitable for larger or less reliable networks. In such cases, TCP or alternative protocols may be more appropriate.

Enjoy exploring and experimenting with the Chat Application simulation!
