import socket
import json

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    for _ in range(3):
        question_data = client_socket.recv(1024).decode()
        question = json.loads(question_data)
        print(question['question'])
        for option in question['options']:
            print(option)
        answer = input("Sua resposta: ").strip().upper()
        client_socket.sendall(answer.encode())

    result_data = client_socket.recv(1024).decode()
    result = json.loads(result_data)
    print(result['message'])
    print("Resultados:", result['results'])
    client_socket.close()

if __name__ == "__main__":
    start_client()