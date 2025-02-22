# Hashflow
# Peer-to-Peer Chat Application

## CS 216: Introduction to Blockchain
### Assignment 1

## Team Information
- **Team Name:** Hashflow
- **Team Members:**
  - Kotha Ashrith Reddy             - 230001043
  - Buditi Deepak                      - 230001016
  - Avvaru Venkata Sai Deepak - 230001011
  - Vivek Tej Kanakam               - 230041014

## Project Description
A Decentralized peer-to-peer (P2P) chat application that allows seamless real-time communication between multiple users without reliance on a centralized server. It supports simultaneous message sending and receiving, peer discovery, and efficient connection management to facilitate effective networking.

## Features
- **Simultaneous Send & Receive** (Multi-threading)
- **Peer Discovery & Tracking**
- **Custom Message Format:**
- **Bonus: Persistent Peer Connection**

## Prerequisites
- Install dependencies:
  ```sh
  pip install -r requirements.txt  # For Python
  sudo apt install gcc  # For C programs
  ```

## How to Run
### C Program:
sh
gcc peer.c -o peer
./peer


### Python Program:
```sh
python peer.py
```

## Usage
Upon starting, the following menu is displayed:
```
Enter your name: <Name>
Enter your port number: <Port>
Server listening on port <Port>

***** Menu *****
1. Send message
2. Query active peers
3. Connect to active peers
0. Quit
```

### Sending Messages
1. Select `1` from the menu.
2. Enter the recipient's IP & port.
3. Type your message & press Enter.

### Querying Peers
1. Select `2` from the menu.
2. List of active peers is displayed.

### Connecting to Active Peers
1. Choose '3' from the menu.
2. The system retrieves the list of known peers from which messages have been received.
3. The program attempts to establish direct connections with these peers.
4. Once connected, peers can exchange messages more efficiently, reducing connection overhead.
5. The list of connected peers updates dynamically to reflect the new connections.

### Exiting
- Enter `0` to quit.
- Sending `exit` removes a peer from the list.

## Message Format
```
<IP_ADDRESS:PORT> <TEAM_NAME> <MESSAGE>
```
Example:
```
10.206.4.201:8080 blockchain Hello, you there?
```

## Bonus Feature: `connect()`
- Establishes persistent peer connections.
- Newly connected peers appear in the query list.

## Notes
- Use **fixed ports** instead of ephemeral ports.
- Avoid duplicate (IP:PORT) entries.

## References
1. [Socket Programming in C](https://www.geeksforgeeks.org/socket-programming-cc/)
2. [Linux IP Address Guide](https://www.ionos.com/digitalguide/hosting/technical-matters/get-linux-ip-address/)
3. [Threading in Python](https://docs.python.org/3/library/threading.html)
