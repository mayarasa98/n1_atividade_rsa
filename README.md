# EC10 - Tópicos Avançados em Redes

## N1 - Atividade RSA (Criptografia Assimétrica)

### 👩‍💻 Integrantes
- Claudia Galindo Santos - 081210014 
- Mayara Silva Azevedo - 081210029
- Nadielly Oliveira Santos - 081210024

---

## 🔐 Comunicação Cliente-Servidor com RSA (4096 bits)

Este projeto demonstra uma comunicação **segura** entre um **cliente** e um **servidor** utilizando **Python**, **sockets** e **criptografia assimétrica RSA** com o esquema de cifra **PKCS#1 OAEP**.

---

## 📌 Funcionalidades

- Geração automática de chaves **RSA de 4096 bits** para cliente e servidor.
- Troca de **chaves públicas** entre cliente e servidor.
- Envio de mensagens criptografadas:
  - O cliente envia uma mensagem segura para o servidor.
  - O servidor descriptografa, processa (transforma em MAIÚSCULA) e retorna a resposta criptografada.
- Comunicação bidirecional **segura** com uso de chaves assimétricas.

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **socket** → comunicação TCP/IP.
- **PyCryptodome** → biblioteca de criptografia:
  - `RSA` → geração de chaves públicas/privadas.
  - `PKCS1_OAEP` → algoritmo para criptografia assimétrica segura.

---

## 📂 Estrutura dos Arquivos

- `Simple_tcpClient.py` → código do cliente.
- `Simple_tcpServer.py` → código do servidor.

---

## ⚙️ Como Funciona

### 1. Servidor
1. Gera **par de chaves RSA (4096 bits)**.
2. Inicia um **socket TCP** e aguarda conexão do cliente.
3. Envia sua **chave pública** para o cliente.
4. Recebe a **chave pública do cliente**.
5. Recebe a **mensagem criptografada** do cliente.
6. **Descriptografa** a mensagem com sua **chave privada**.
7. Converte a mensagem recebida para **maiúscula**.
8. **Criptografa** a resposta usando a **chave pública do cliente**.
9. Envia a resposta de volta ao cliente.

---

### 2. Cliente
1. Gera **par de chaves RSA (4096 bits)**.
2. Conecta ao servidor via **socket TCP**.
3. Recebe a **chave pública do servidor**.
4. Envia sua **chave pública** para o servidor.
5. Solicita uma **mensagem** ao usuário.
6. **Criptografa** a mensagem com a **chave pública do servidor**.
7. Envia a mensagem criptografada ao servidor.
8. Recebe a **resposta criptografada**.
9. **Descriptografa** a resposta com sua **chave privada**.
10. Exibe o resultado.

---

## ▶️ Como Executar

### 1. Instale as dependências
```bash
pip install pycryptodome

### 2. Dê o comando que executa os arquivos de cliente e servidor
python Simple_tcpClient.py ## Cliente
python Simple_tcpClient.py ## Servidor
