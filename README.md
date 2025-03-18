# Projeto Cliente-Servidor em Python

Este projeto implementa um sistema cliente-servidor em Python que envia três questões de múltipla escolha para um cliente após este se conectar. O cliente deve responder às questões, e o servidor retorna com o número de questões acertadas, mostrando em uma lista o acerto/erro de cada questão.

## Estrutura do Projeto

O projeto é composto por dois arquivos principais:
- `server.py`: Código do servidor que envia as questões e avalia as respostas.
- `client.py`: Código do cliente que recebe as questões, envia as respostas e recebe os resultados.

## Questões de Exemplo

As questões de exemplo utilizadas no projeto são:
1. Qual é a capital da Itália?
   - A) Roma
   - B) Paris
   - C) Lisboa
   - D) Londres

2. Qual é a capital da França?
   - A) Roma
   - B) Paris
   - C) Lisboa
   - D) Londres

3. Qual é a capital de Portugal?
   - A) Roma
   - B) Paris
   - C) Lisboa
   - D) Londres

## Como Executar

### Passo 1: Executar o Servidor

1. Abra um terminal.
2. Navegue até o diretório onde o arquivo `server.py` está localizado.
3. Execute o seguinte comando:
   ```bash
   python server.py
