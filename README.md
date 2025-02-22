# Hashflow
# Peer-to-Peer Chat Application

## CS 216: Introduction to Blockchain
### Assignment 1

## Team Information
- **Team Name:** Hashflow
- **Team Members:**
  - Kotha Ashrith Reddy - 230001043
  - Buditi Deepak- 230001016
  - Avvaru Venkata Sai Deepak - 230001011
  - Vivek Tej Kanakam - 230041014

## Project Description
A peer-to-peer chat application enabling simultaneous message sending and receiving, supporting multiple peers, and allowing peer discovery.

## Features
- **Simultaneous Send & Receive** (Multi-threading)
- **Peer Discovery & Tracking**
- **Custom Message Format:** `<IP_ADDRESS:PORT> <TEAM_NAME> <MESSAGE>`
- **Bonus: Persistent Peer Connection (`connect()` function)**

## Prerequisites
- Install dependencies:
  ```sh
  pip install -r requirements.txt  # For Python
  sudo apt install gcc  # For C programs
  ```

## How to Run
### Python Program:
```sh
python peer.py
```

## Usage
Upon starting, the following menu is displayed:
```
Enter your name: <Team Name>
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

