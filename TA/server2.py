import socket
import random

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menetapkan alamat dan port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Mendengarkan koneksi
server_socket.listen(1)
print("Server mendengarkan di", server_address)

# Membangkitkan angka acak
secret_number = random.randint(1, 10)

# Menerima koneksi dari klien
client_socket, client_address = server_socket.accept()
print("Menerima koneksi dari", client_address)

# Mengirimkan pesan selamat datang ke klien
client_socket.send("Tebak angka yang muncul antara 1 dan 10.".encode())

# Fungsi untuk memproses tebakan klien
def process_guess(guess):
    guess = int(guess)
    if guess == secret_number:
        return "Tebakan Anda benar!"
    elif guess < secret_number:
        return "Angka terlalu kecil. Coba lagi."
    else:
        return "Angka terlalu besar. Coba lagi."

# Loop untuk menerima tebakan dari klien
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break

    response = process_guess(data)
    client_socket.send(response.encode())

# Menutup koneksi
client_socket.close()
server_socket.close()
