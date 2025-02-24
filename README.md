# Hashflow: Peer-to-Peer Chat Application

## CS 216: Introduction to Blockchain
### Assignment 2

---

## Team Information
- **Team Name:** Hashflow
- **Team Members:**
  - Kotha Ashrith Reddy             - 230001043
  - Buditi Deepak                      - 230001016
  - Avvaru Venkata Sai Deepak - 230001011
  - Vivek Tej Kanakam               - 230041014

---

## Project Description
This repository contains a Python-based peer-to-peer (P2P) chat application that meets the requirements specified in **Assignment 2** of **CS 216: Introduction to Blockchain**. It enables:

1. **Simultaneous Sending and Receiving of Messages** using multi-threading.
2. **Peer Discovery** and tracking, storing details of known peers.
3. **Querying Active Peers** and establishing **persistent connections**.
4. **Broadcasting Messages** to multiple peers at once.
5. **Disconnecting** from a specific peer or exiting the application gracefully.

---

## Features

1. **Network Control Panel Menu**  
   - **1. Start Messaging Session**: Initiate a direct messaging session with a chosen peer.  
   - **2. View Active Peers**: Display the list of known peers.  
   - **3. Connect to Peers**: Attempt direct connections to all known peers for efficient communication.  
   - **4. Broadcast Message**: Send a message to all known peers simultaneously.  
   - **5. Disconnect from a Peer**: End the connection to a specific peer.  
   - **0. Quit Application**: Safely exit the application.

2. **Persistent Peer Directory**  
   - Tracks both connected peers and peers from which messages have been received.

3. **Simultaneous Send/Receive**  
   - A dedicated thread listens for incoming messages (`handle_incoming_messages`), while the main thread handles user input and sends messages (`handle_outgoing_messages`).

4. **Exit and Inactivity Protocols**  
   - If a peer sends the message `exit`, it notifies and removes that peer from the network.
   - Optionally checks for and removes inactive peers via `remove_inactive_peers()`.

5. **Mandatory Server Connection**  
   - Per the assignment instructions, the code demonstrates sending an initial “hello” to the server at `10.206.5.228:6555`.
   - (You may extend this to include the other mandatory IP/port if required, e.g., `10.206.4.122:1255`.)

---

## Repository Structure
- **`p2p_chat.py`** (example name)  
  Contains the main code with:
  - Socket handling (TCP)  
  - Threads for sending/receiving  
  - Menu-driven user interface  
  - Peer directory and connection logic

- **`README.md`**  
  (This file) Provides instructions and documentation for setup, usage, and submission.

You may also include additional files if you choose to refactor or modularize the code.

---

## Installation & Prerequisites

1. **Python 3** (Recommended)
2. **Dependencies** (If any external libraries are used, list them here, e.g. `requirements.txt`)

To install dependencies (if applicable):
```bash
pip install -r requirements.txt
