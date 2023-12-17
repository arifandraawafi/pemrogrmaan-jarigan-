import socket

# Inisialisasi socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menetapkan alamat dan port server
server_address = ('localhost', 12345)

# Menghubungkan ke server
client_socket.connect(server_address)
print("Terhubung ke server di", server_address)

# Menerima pesan selamat datang dari server
welcome_message = client_socket.recv(1024).decode()
print(welcome_message)

# Loop untuk menebak angka
while True:
    guess = input("Tebak angka: ")
    client_socket.send(guess.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    if "Tebakan Anda benar!" in response:
        break

# Menutup koneksi
client_socket.close()
