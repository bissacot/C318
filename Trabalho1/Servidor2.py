import socket
import json

# Questões de múltipla escolha
questions = [
    {"question": "Qual é a capital da Itália?", "options": ["A) Roma", "B) Paris", "C) Lisboa", "D) Londres"], "answer": "A"},
    {"question": "Qual é a capital da França?", "options": ["A) Roma", "B) Paris", "C) Lisboa", "D) Londres"], "answer": "B"},
    {"question": "Qual é a capital de Portugal?", "options": ["A) Roma", "B) Paris", "C) Lisboa", "D) Londres"], "answer": "C"}
]

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Servidor aguardando conexão...")

    conn, addr = server_socket.accept()
    print(f"Conectado a {addr}")

    correct_answers = 0
    results = []

    for q in questions:
        question_data = json.dumps(q)
        conn.sendall(question_data.encode())
        response = conn.recv(1024).decode().strip().upper()
        if response == q['answer']:
            correct_answers += 1
            results.append("Acerto")
        else:
            results.append("Erro")

    result_message = {
        "message": f"Você acertou {correct_answers} de {len(questions)} questões.",
        "results": results
    }
    conn.sendall(json.dumps(result_message).encode())
    conn.close()

if __name__ == "__main__":
    start_server()