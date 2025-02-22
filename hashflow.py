import socket
import threading

# Dictionary to store known peers { (IP, Port): "Peer Name" }
peer_directory = {}
connected_peers = set()
thread_lock = threading.Lock()
TEAM_IDENTIFIER = "Hashflow"

# Function to receive messages and track peers
def handle_incoming_messages(server_socket):
    while True:
        try:
            client_socket, address = server_socket.accept()
            message = client_socket.recv(1024).decode()
            try:
                sender_details, team_name, actual_message = message.split(" ", 2)
                sender_ip, sender_port = sender_details.split(":")
                sender_port = int(sender_port)

                if actual_message == "PING":
                    client_socket.close()
                    continue

                with thread_lock:
                    if (sender_ip, sender_port) not in peer_directory:
                        peer_directory[(sender_ip, sender_port)] = team_name

                print(f"\n Message from {sender_ip}:{sender_port} ({team_name}) → {actual_message}")
                
            except Exception as e:
                print(f"\n[Error] Received malformed message: {message}")

            client_socket.close()
        except Exception as e:
            print(f"\n[Error] Issue in receiving messages: {e}")

# Function to send messages with the given format
def handle_outgoing_messages(local_ip, local_port):
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
                                client_socket.send(f"{local_ip}:{local_port} {TEAM_IDENTIFIER} Hello!".encode())
                                connected_peers.add((ip, port))
                                print(f"[System] Successfully connected to {ip}:{port}")
                            except Exception as e:
                                print(f"[Error] Failed to connect to {ip}:{port} - {e}")
                            finally:
                                client_socket.close()

            elif user_choice == "4":
                print("\n[System] Checking for inactive peers...")
                remove_inactive_peers()

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
    print("\n" + "-" * 40)
    print(f"{'Network Control Panel':^40}")
    print("-" * 40)
    print("1. Start Messaging Session")
    print("2. View Active Peers")
    print("3. Connect to Peers")
    print("4. Broadcast Message")
    print("5. Disconnect from a Peer")
    print("0. Quit Application")
    print("-" * 40)

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
