# TCP Chat (Socket Client/Server)

A minimal two-way chat between a Python TCP server and client, built directly on the `socket` module (no external libraries).

## How it works

- `server1.py` opens a TCP socket on `localhost:3000`, accepts a single client connection, then loops: reading a message from the client, printing it, and sending back an acknowledgement.
- `client1.py` connects to that server, then loops: reading a line typed by the user, sending it to the server, and printing the server's reply.

## Project structure

| File | Purpose |
|------|---------|
| `server1.py` | TCP server — accepts one client and echoes received messages |
| `client1.py` | TCP client — sends typed messages and prints the server's replies |

## Requirements

- Python 3.8+ (uses only the standard library — no packages to install)

## Run it

1. Start the server first, in one terminal:

   ```bash
   python server1.py
   ```

   It will print `Server is listening on port 3000...` and then wait for a connection.

2. In a second terminal, start the client:

   ```bash
   python client1.py
   ```

3. Type a message in the client terminal and press Enter. The server prints what it received, and the client prints the server's acknowledgement. Repeat as needed.

## Notes

- This server accepts only **one** client connection at a time (`listen(1)`), and closes once that client disconnects.
- Both processes must run on the same machine, since the client connects to `localhost`.

## Author

Elisee Biyong Enane
