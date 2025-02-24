import socket
import threading

# Dictionary to store known peers { (IP, Port): "Peer Name" }
peer_directory = {}
connected_peers = set()
thread_lock = threading.Lock()
TEAM_IDENTIFIER = "Hashflow"


def propagate_exit_notification(local_ip, local_port, exiting_peer):
    """Notify all connected peers about a peer's exit"""
    notification_message = f"{local_ip}:{local_port} {TEAM_IDENTIFIER} exit"
    
    with thread_lock:
        for peer in list(connected_peers):
            ip, port = peer
            if peer == exiting_peer:
                continue
                
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(5)
                    sock.connect((ip, port))
                    sock.send(notification_message.encode())
            except Exception as e:
                print(f"[Exit Propagation] Failed to notify {ip}:{port} - {str(e)[:30]}")


# Function to receive messages and track peers
def handle_incoming_messages(server_socket):
    while True:
        try:
            client_socket, address = server_socket.accept()
            message = client_socket.recv(1024).decode()
            
            # Extract sender details from message
            sender_details, team_name, actual_message = message.split(" ", 2)
            sender_ip, sender_port = sender_details.split(":")
            sender_port = int(sender_port)

            # Handle exit protocol
            if actual_message.lower() == "exit":
                with thread_lock:
                    peer_directory.pop((sender_ip, sender_port), None)
                    connected_peers.discard((sender_ip, sender_port))
                print(f"\n[System] {sender_ip}:{sender_port} exited network")
                propagate_exit_notification(sender_ip, sender_port, (sender_ip, sender_port))
                client_socket.close()
                continue

            # Store peer information in peer_directory (but not in connected_peers)
            with thread_lock:
                if (sender_ip, sender_port) not in peer_directory:
                    peer_directory[(sender_ip, sender_port)] = team_name

            print(f"\n{sender_ip}:{sender_port} {team_name} {actual_message}")
            client_socket.close()

        except Exception as e:
            print(f"\n[Error] Message handling: {e}")




# Function to send messages 
def handle_outgoing_messages(local_ip, local_port):


    # Send mandatory "hello" messages first (NEW CODE)
    mandatory_servers = [
        ("10.206.5.228", 6555)
    ]
    
    for server_ip, server_port in mandatory_servers:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((server_ip, server_port))
                formatted_hello = f"{local_ip}:{local_port} {TEAM_IDENTIFIER} hello"
                sock.send(formatted_hello.encode())
                print(f"[System] Sent mandatory hello to {server_ip}:{server_port}")
        except Exception as e:
            print(f"[Error] Failed to send hello to {server_ip}:{server_port} - {e}")



    while True:
        try:
            display_control_panel()
            user_choice = input("Select an option: ").strip()

            if user_choice == "1":
                recipient_ip = input("Enter recipient's IP address: ").strip()
                recipient_port = input("Enter recipient's port number: ").strip()

                if not recipient_port.isdigit():
                    print("[Error] Invalid port! Please enter a valid number.")
                    continue

                recipient_port = int(recipient_port)
                user_message = input("Enter your message: ").strip()
                formatted_message = f"{local_ip}:{local_port} {TEAM_IDENTIFIER} {user_message}"

                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    client_socket.connect((recipient_ip, recipient_port))
                    client_socket.send(formatted_message.encode())
                    print("[System] Message sent successfully!")
                except Exception as e:
                    print(f"[Error] Failed to send message to {recipient_ip}:{recipient_port} - {e}")
                finally:
                    client_socket.close()

            elif user_choice == "2":
                with thread_lock:
                    print("\n" + "-" * 40)
                    print(f"{'Active Peers':^40}")
                    print("-" * 40)
                    if peer_directory:
                        print(f"{'Peer Name':<15}{'IP Address':<15}{'Port':<10}")
                        print("-" * 40)
                        for (ip, port), name in peer_directory.items():
                            connection_status = "Connected" if (ip, port) in connected_peers else "Not Connected"
                            print(f"{name:<15}{ip:<15}{port:<10} ({connection_status})")
                    else:
                        print("No active peers found.")
                    print("-" * 40)

            elif user_choice == "3":
                print("\n[System] Connecting to known peers...")
                with thread_lock:
                    for (ip, port) in list(peer_directory.keys()):
                        if (ip, port) not in connected_peers:
                            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            try:
                                client_socket.connect((ip, port))
                                client_socket.send(f"{local_ip}:{local_port} {TEAM_IDENTIFIER} Connected".encode())
                                connected_peers.add((ip, port))
                                print(f"[System] Successfully connected to {ip}:{port}")
                            except Exception as e:
                                print(f"[Error] Failed to connect to {ip}:{port} - {e}")
                            finally:
                                client_socket.close()

            elif user_choice == "4":
                print("\n[System] Broadcasting message to all peers...")
                broadcast_message(local_ip, local_port)

            elif user_choice == "5":
                disconnect_ip = input("Enter peer's IP address to disconnect: ")
                disconnect_port = int(input("Enter peer's port number to disconnect: "))

                with thread_lock:
                    if (disconnect_ip, disconnect_port) in connected_peers:
                        connected_peers.remove((disconnect_ip, disconnect_port))
                        print(f"[System] Disconnected from {disconnect_ip}:{disconnect_port}")
                    else:
                        print(f"[Error] No active connection found for {disconnect_ip}:{disconnect_port}")

            elif user_choice == "0":
                print("[System] Exiting application... Goodbye!")
                break

            else:
                print("[Error] Invalid choice! Please select a valid option.")

        except Exception as e:
            print(f"\n[Error] Issue in sending messages: {e}")


# Function to broadcast a message to all known peers
def broadcast_message(local_ip, local_port):
    with thread_lock:
        for (ip, port), name in peer_directory.items():
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                formatted_message = f"{local_ip}:{local_port} {TEAM_IDENTIFIER} Broadcast Message"
                client_socket.connect((ip, port))
                client_socket.send(formatted_message.encode())
                print(f"[System] Broadcasted message to {ip}:{port}")
            except Exception as e:
                print(f"[Error] Failed to broadcast message to {ip}:{port} - {e}")
            finally:
                client_socket.close()


# Function to check and remove inactive peers
def remove_inactive_peers():
    inactive_peers = []
    with thread_lock:
        for (ip, port) in list(peer_directory.keys()):
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(2)
            try:
                client_socket.connect((ip, port))
                client_socket.send(f"{ip}:{port} {TEAM_IDENTIFIER} PING".encode())
                client_socket.close()
            except:
                inactive_peers.append((ip, port))
                
        for peer in inactive_peers:
            peer_directory.pop(peer, None)
            print(f"[System] Removed inactive peer: {peer[0]}:{peer[1]}")


# Function to display the control panel
def display_control_panel():
    # Box drawing characters for borders
    top_left = '╔'
    top_right = '╗'
    bottom_left = '╚'
    bottom_right = '╝'
    vertical = '║'
    horizontal = '═'
    tee_right = '╠'
    tee_left = '╣'

    # Create the menu box
    border = top_left + horizontal * 40 + top_right
    separator = tee_right + horizontal * 40 + tee_left

    print(f"\n{border}")
    print(f"{vertical}{'Network Control Panel':^40}{vertical}")
    print(separator)
    print(f"{vertical} 1. Start Messaging Session{' ' * 13}{vertical}")
    print(f"{vertical} 2. View Active Peers{' ' * 19}{vertical}")
    print(f"{vertical} 3. Connect to Peers{' ' * 20}{vertical}")
    print(f"{vertical} 4. Broadcast Message{' ' * 19}{vertical}")
    print(f"{vertical} 5. Disconnect from a Peer{' ' * 14}{vertical}")
    print(f"{vertical} 0. Quit Application{' ' * 20}{vertical}")
    print(f"{bottom_left}{horizontal * 40}{bottom_right}")



# Main function
def start_peer_application():
    local_ip = socket.gethostbyname(socket.gethostname())  
    local_port_input = input("Enter the port number for your peer: ").strip()

    if not local_port_input.isdigit():
        print("[Error] Invalid port! Please enter a valid number.")
        return

    local_port = int(local_port_input)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((local_ip, local_port))
    server_socket.listen(5)
    print(f"[System] Local IP address: {local_ip}")
    print(f"[System] Server running on port {local_port}")


    receiver_thread = threading.Thread(target=handle_incoming_messages, args=(server_socket,))
    receiver_thread.daemon = True
    receiver_thread.start()

    handle_outgoing_messages(local_ip, local_port)

if __name__ == "__main__":
    start_peer_application()

    handle_outgoing_messages(local_ip, local_port)

if __name__ == "__main__":
    start_peer_application()
