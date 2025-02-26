import socket
import tkinter as tk
from tkinter import messagebox

IP = "127.0.0.1"
PORT = 4000

def send_data_to_server():
    expression = entry.get()

    if expression:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        client_socket.send(expression.encode())

        result = client_socket.recv(1024).decode()
        client_socket.close()

        messagebox.showinfo("Результат", f"Результат вычисления: {result}")
    else:
        messagebox.showwarning("Ошибка", "Введите выражение")


root = tk.Tk()
root.title("Клиент для вычислений")

label = tk.Label(root, text="Введите математическое выражение:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Отправить", command=send_data_to_server)
button.pack(pady=10)

root.mainloop()
