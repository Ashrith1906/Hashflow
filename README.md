# Hashflow: A Peer-to-Peer Chat Application

## CS 216: Introduction to Blockchain

### Assignment 1

## Team Members
- **Kotha Ashrith Reddy** - 230001043  
- **Buditi Deepak** - 230001016  
- **Avvaru Venkata Sai Deepak** - 230001011  
- **Vivek Tej Kanakam** - 230041014  

## Overview
Hashflow is a peer-to-peer (P2P) chat application developed as part of **CS 216: Introduction to Blockchain (Assignment 2)**. It enables users to send and receive messages simultaneously, manage peer connections, and broadcast messages within a decentralized network.

## Features
- **Simultaneous Send & Receive:** Multi-threaded implementation to allow concurrent message transmission and reception.
- **Peer Discovery & Management:** Maintains a list of active peers and dynamically updates connections.
- **Direct Messaging:** Supports one-on-one communication between peers.
- **Broadcast Messaging:** Enables sending a message to all known peers at once.
- **Disconnect & Exit Handling:** Allows graceful disconnection from individual peers and the entire network.
- **Persistent Peer Directory:** Stores connected peers for efficient reconnections.

## Installation & Setup
### Prerequisites
- Python 3.x
- Basic understanding of TCP/IP networking

### Running the Application
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/hashflow-p2p-chat.git
   cd hashflow-p2p-chat
   ```
2. **Start the Chat Application**
   ```bash
   python p2p_chat.py
   ```
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
- **Exiting:** Sending `exit` notifies peers before disconnecting.

## References
- Assignment PDF (CS 216: Introduction to Blockchain - Assignment 2)
- [Python Socket Programming](https://docs.python.org/3/howto/sockets.html)
- [Threading in Python](https://docs.python.org/3/library/threading.html)

## Submission Details
- **Deadline:** 22nd February 2025, 11:30 PM
- **Submission:** Upload GitHub repository link to Moodle.

**Happy Chatting!** 🚀

