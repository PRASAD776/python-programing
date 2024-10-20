import socket
import threading
import tkinter as tk
from tkinter import filedialog, Text, messagebox, simpledialog
from PIL import Image, ImageTk
import os
import shutil
import random

# -------------------- Networking Constants -------------------- #
# You can choose any port > 1024 that is free on your system
DEFAULT_PORT = 5000
BUFFER_SIZE = 4096

# -------------------- Global Variables -------------------- #
peers = []  # List to keep track of connected peer sockets
shared_files_dir = 'shared_files'  # Directory to store shared files

# -------------------- Helper Functions -------------------- #
def display_message(message):
    """Display a message in the chat window."""
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{message}\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)  # Auto-scroll to the end

def send_message():
    """Send a text message to all connected peers."""
    message = message_entry.get("1.0", tk.END).strip()
    if message:
        display_message(f"You: {message}")
        message_entry.delete("1.0", tk.END)
        for peer in peers:
            try:
                peer.sendall(f"MESSAGE:{message}".encode('utf-8'))
            except:
                pass  # Optionally handle broken connections

def share_file():
    """Share a file with all connected peers."""
    file_path = filedialog.askopenfilename()
    if file_path:
        filename = os.path.basename(file_path)
        display_message(f"You shared a file: {filename}")
        shutil.copy(file_path, os.path.join(shared_files_dir, filename))
        for peer in peers:
            try:
                with open(file_path, 'rb') as f:
                    peer.sendall(f"FILE:{filename}".encode('utf-8'))
                    while True:
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            break
                        peer.sendall(bytes_read)
                # Indicate end of file transfer
                peer.sendall("END_OF_FILE".encode('utf-8'))
            except:
                pass  # Optionally handle broken connections

def share_image():
    """Share an image with all connected peers and display it in the chat."""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        filename = os.path.basename(file_path)
        image = Image.open(file_path)
        image.thumbnail((100, 100))  # Resize for display
        img_display = ImageTk.PhotoImage(image)
        chat_window.config(state=tk.NORMAL)
        chat_window.image_create(tk.END, image=img_display)  # Display image
        chat_window.insert(tk.END, f" You shared an image: {filename}\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.image = img_display  # Keep a reference
        shutil.copy(file_path, os.path.join(shared_files_dir, filename))  # Save shared image
        for peer in peers:
            try:
                with open(file_path, 'rb') as f:
                    peer.sendall(f"IMAGE:{filename}".encode('utf-8'))
                    while True:
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            break
                        peer.sendall(bytes_read)
                # Indicate end of image transfer
                peer.sendall("END_OF_IMAGE".encode('utf-8'))
            except:
                pass  # Optionally handle broken connections

def share_location():
    """Share a simulated location with all connected peers."""
    location = f"Latitude: {random.uniform(-90, 90):.2f}, Longitude: {random.uniform(-180, 180):.2f}"
    display_message(f"You shared a location: {location}")
    for peer in peers:
        try:
            peer.sendall(f"LOCATION:{location}".encode('utf-8'))
        except:
            pass  # Optionally handle broken connections

def connect_to_peer():
    """Connect to a peer using IP and Port."""
    peer_ip = simpledialog.askstring("Connect to Peer", "Enter peer IP address:")
    if not peer_ip:
        return
    peer_port = simpledialog.askinteger("Connect to Peer", "Enter peer port number:", initialvalue=DEFAULT_PORT)
    if not peer_port:
        return
    try:
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer.connect((peer_ip, peer_port))
        peers.append(peer)
        peers_listbox.insert(tk.END, f"{peer_ip}:{peer_port}")
        threading.Thread(target=receive_messages, args=(peer,), daemon=True).start()
        display_message(f"Connected to {peer_ip}:{peer_port}")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Failed to connect to {peer_ip}:{peer_port}\n{e}")

def handle_client(conn, addr):
    """Handle incoming messages from a connected peer."""
    peers.append(conn)
    peers_listbox.insert(tk.END, f"{addr[0]}:{addr[1]}")
    display_message(f"{addr[0]}:{addr[1]} has connected.")
    while True:
        try:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            decoded_data = data.decode('utf-8', errors='ignore')
            if decoded_data.startswith("MESSAGE:"):
                message = decoded_data.split(":", 1)[1]
                display_message(f"{addr[0]}:{addr[1]}: {message}")
            elif decoded_data.startswith("FILE:"):
                filename = decoded_data.split(":", 1)[1]
                filepath = os.path.join(shared_files_dir, filename)
                with open(filepath, 'wb') as f:
                    while True:
                        file_data = conn.recv(BUFFER_SIZE)
                        if file_data.endswith(b"END_OF_FILE"):
                            f.write(file_data[:-len("END_OF_FILE")])
                            break
                        f.write(file_data)
                display_message(f"{addr[0]}:{addr[1]} shared a file: {filename}")
            elif decoded_data.startswith("IMAGE:"):
                filename = decoded_data.split(":", 1)[1]
                filepath = os.path.join(shared_files_dir, filename)
                with open(filepath, 'wb') as f:
                    while True:
                        file_data = conn.recv(BUFFER_SIZE)
                        if file_data.endswith(b"END_OF_IMAGE"):
                            f.write(file_data[:-len("END_OF_IMAGE")])
                            break
                        f.write(file_data)
                # Display the image in the chat
                if os.path.exists(filepath):
                    image = Image.open(filepath)
                    image.thumbnail((100, 100))
                    img_display = ImageTk.PhotoImage(image)
                    chat_window.config(state=tk.NORMAL)
                    chat_window.image_create(tk.END, image=img_display)
                    chat_window.insert(tk.END, f" {addr[0]}:{addr[1]} shared an image: {filename}\n")
                    chat_window.config(state=tk.DISABLED)
                    chat_window.image = img_display  # Keep a reference
            elif decoded_data.startswith("LOCATION:"):
                location = decoded_data.split(":", 1)[1]
                display_message(f"{addr[0]}:{addr[1]} shared a location: {location}")
            else:
                display_message(f"Unknown data from {addr[0]}:{addr[1]}")
        except:
            break
    conn.close()
    if conn in peers:
        peers.remove(conn)
    peers_listbox.delete(0, tk.END)
    for peer in peers:
        try:
            peer_info = peer.getpeername()
            peers_listbox.insert(tk.END, f"{peer_info[0]}:{peer_info[1]}")
        except:
            pass
    display_message(f"{addr[0]}:{addr[1]} has disconnected.")

def receive_messages(peer):
    """Receive messages from a connected peer."""
    while True:
        try:
            data = peer.recv(BUFFER_SIZE)
            if not data:
                break
            decoded_data = data.decode('utf-8', errors='ignore')
            if decoded_data.startswith("MESSAGE:"):
                message = decoded_data.split(":", 1)[1]
                display_message(f"Peer: {message}")
            elif decoded_data.startswith("FILE:"):
                filename = decoded_data.split(":", 1)[1]
                filepath = os.path.join(shared_files_dir, filename)
                with open(filepath, 'wb') as f:
                    while True:
                        file_data = peer.recv(BUFFER_SIZE)
                        if file_data.endswith(b"END_OF_FILE"):
                            f.write(file_data[:-len("END_OF_FILE")])
                            break
                        f.write(file_data)
                display_message(f"Peer shared a file: {filename}")
            elif decoded_data.startswith("IMAGE:"):
                filename = decoded_data.split(":", 1)[1]
                filepath = os.path.join(shared_files_dir, filename)
                with open(filepath, 'wb') as f:
                    while True:
                        file_data = peer.recv(BUFFER_SIZE)
                        if file_data.endswith(b"END_OF_IMAGE"):
                            f.write(file_data[:-len("END_OF_IMAGE")])
                            break
                        f.write(file_data)
                # Display the image in the chat
                if os.path.exists(filepath):
                    image = Image.open(filepath)
                    image.thumbnail((100, 100))
                    img_display = ImageTk.PhotoImage(image)
                    chat_window.config(state=tk.NORMAL)
                    chat_window.image_create(tk.END, image=img_display)
                    chat_window.insert(tk.END, f" Peer shared an image: {filename}\n")
                    chat_window.config(state=tk.DISABLED)
                    chat_window.image = img_display  # Keep a reference
            elif decoded_data.startswith("LOCATION:"):
                location = decoded_data.split(":", 1)[1]
                display_message(f"Peer shared a location: {location}")
            else:
                display_message(f"Unknown data from peer.")
        except:
            break
    peer.close()
    if peer in peers:
        peers.remove(peer)
    peers_listbox.delete(0, tk.END)
    for p in peers:
        try:
            p_info = p.getpeername()
            peers_listbox.insert(tk.END, f"{p_info[0]}:{p_info[1]}")
        except:
            pass
    display_message("A peer has disconnected.")

def start_server(host, port):
    """Start the server to listen for incoming peer connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((host, port))
    except Exception as e:
        messagebox.showerror("Binding Error", f"Failed to bind to {host}:{port}\n{e}")
        return
    server.listen()
    display_message(f"Server listening on {host}:{port}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

# -------------------- GUI Setup -------------------- #
root = tk.Tk()
root.title("P2P Chat App")

# -------------------- Chat Display Area -------------------- #
chat_frame = tk.Frame(root)
chat_frame.pack(pady=10)

chat_window = tk.Text(chat_frame, bg="lightgrey", width=70, height=20, state=tk.DISABLED)
chat_window.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(chat_frame, command=chat_window.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_window.config(yscrollcommand=scrollbar.set)

# -------------------- Message Input -------------------- #
message_entry = Text(root, height=3)
message_entry.pack(padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message, width=10, bg="blue", fg="white")
send_button.pack(pady=5)

# -------------------- File/Media/Location Buttons -------------------- #
media_frame = tk.Frame(root)
media_frame.pack(pady=10)

file_button = tk.Button(media_frame, text="Share File", command=share_file, width=12, bg="green", fg="white")
file_button.grid(row=0, column=0, padx=10)

image_button = tk.Button(media_frame, text="Share Image", command=share_image, width=12, bg="purple", fg="white")
image_button.grid(row=0, column=1, padx=10)

location_button = tk.Button(media_frame, text="Share Location", command=share_location, width=12, bg="orange", fg="white")
location_button.grid(row=0, column=2, padx=10)

# -------------------- Connect to Peer Section -------------------- #
connect_frame = tk.Frame(root)
connect_frame.pack(pady=10)

connect_button = tk.Button(connect_frame, text="Connect to Peer", command=connect_to_peer, width=15, bg="cyan", fg="black")
connect_button.pack()

# -------------------- Connected Peers List -------------------- #
peers_frame = tk.Frame(root)
peers_frame.pack(pady=10)

peers_label = tk.Label(peers_frame, text="Connected Peers:")
peers_label.pack()

peers_listbox = tk.Listbox(peers_frame, height=5, width=50)
peers_listbox.pack()

# -------------------- Ensure 'shared_files' Directory Exists -------------------- #
if not os.path.exists(shared_files_dir):
    os.makedirs(shared_files_dir)

# -------------------- Start Server Thread -------------------- #
# Prompt the user to enter the host IP and port
def prompt_server_details():
    """Prompt the user to input the host IP and port."""
    host = simpledialog.askstring("Server Setup", "Enter your host IP address:", initialvalue=socket.gethostbyname(socket.gethostname()))
    if not host:
        host = '0.0.0.0'  # Listen on all interfaces if no input
    port = simpledialog.askinteger("Server Setup", "Enter the port number to listen on:", initialvalue=DEFAULT_PORT)
    if not port:
        port = DEFAULT_PORT
    threading.Thread(target=start_server, args=(host, port), daemon=True).start()

# Delay the prompt to ensure the GUI initializes properly
root.after(100, prompt_server_details)

# -------------------- Run the Application -------------------- #
root.mainloop()