# Hashflow: A Peer-to-Peer Chat Application

## CS 216: Introduction to Blockchain

### Assignment 1

## Team Members
- **Kotha Ashrith Reddy** - 230001043  
- **Buditi Deepak** - 230001016  
- **Avvaru Venkata Sai Deepak** - 230001011  
- **Vivek Tej Kanakam** - 230041014  

## Overview
A Decentralized peer-to-peer (P2P) chat application that allows seamless real-time communication between multiple users without reliance on a centralized server. 
It enables : 
- **Simultaneous Send & Receive:** Multi-threaded implementation to allow concurrent message transmission and reception.
- **Peer Discovery & Management:** Maintains a list of active peers and dynamically updates connections.
- **Direct Messaging:** Supports one-on-one communication between peers.
- **Broadcast Messaging:** Enables sending a message to all known peers at once.
- **Disconnect & Exit Handling:** Allows graceful disconnection from individual peers and the entire network.
- **Persistent Peer Directory:** Stores connected peers for efficient reconnections.

## Key Features
![WhatsApp Image 2025-02-24 at 11 42 32 PM](https://github.com/user-attachments/assets/e1af2a5e-a54f-41cb-87f3-1ba5a3e439eb)


## Bonus Task Implementation
- **`handle_incoming_messages(server_socket)`** → Stores sender details in `peer_directory` upon receiving a message.  
- **`handle_outgoing_messages(local_ip, local_port)`** → Implements **Option 3: Connect to Peers**, establishing connections and sending a "Connected" message.  
- **`display_control_panel()`** → Adds menu option to connect to peers.  
- **`remove_inactive_peers()`** → Removes unreachable peers from `peer_directory`.  

This ensures dynamic peer discovery, connection, and active peer tracking as required by the **Bonus Task**.

## Installation & Setup
### Prerequisites
- Python 3.x
- Basic understanding of TCP/IP networking

### Running the Application
1. **Clone the Repository and Run the file**
2. - Clone the repository into your device and run the given python file. Then you will enter port number for the peer. Now you will see the menu for interacting with the network.   
3. **Interact Using the Menu**
   - `1` - Start Messaging Session
   - `2` - View Active Peers
   - `3` - Connect to Peers
   - `4` - Broadcast Message
   - `5` - Disconnect from a Peer
   - `0` - Quit Application

## How It Works
- **Upon Startup:** The application requests a **port number** from the user and displays the **local IP address**.
- **Sending Messages:** Messages are formatted as:  
  ```
  <IP_ADDRESS:PORT> <TEAM_NAME> <MESSAGE>
  ```
- **Receiving Messages:** A separate thread listens for incoming messages.
- **Exiting form network of other peers:** Sending `exit` message notifies the connected peers before disconnecting form their active peer network.

## References
- [Python Socket Programming](https://docs.python.org/3/howto/sockets.html)
- [Threading in Python](https://docs.python.org/3/library/threading.html)
