import socket

IP = "127.0.0.1"
PORT = 4000

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    print("Сервер запущен.")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключен клиент: {client_address}")

        data = client_socket.recv(1024).decode()
        print(f"Получено от клиента: {data}")

        try:
            result = eval(data)
        except Exception as e:
            result = f"Ошибка: {e}"

        client_socket.send(str(result).encode())
        client_socket.close()


start_server()
