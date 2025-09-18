# EC10 - Tópicos Avançados em Redes

## N1 - Atividade RSA (Criptografia Assimétrica)

### 👩‍💻 Integrantes
- Claudia Galindo Santos - 081210014 
- Mayara Silva Azevedo - 081210029
- Nadielly Oliveira Santos - 081210024

---

## 🔐 Comunicação Cliente-Servidor com RSA (4096 bits)

Este projeto demonstra uma comunicação **segura** entre um **cliente** e um **servidor** utilizando **Python**, **sockets** e **criptografia assimétrica RSA** com o esquema de cifra **PKCS#1 OAEP**.  
O objetivo é enviar mensagens de forma segura, garantindo **confidencialidade**, ou seja, apenas o destinatário legítimo consegue ler a mensagem.

---

## 📚 Conceitos Teóricos

### 1. Criptografia Assimétrica (RSA)
- Utiliza um **par de chaves**: pública e privada.
- Mensagens criptografadas com a **chave pública** só podem ser descriptografadas pela **chave privada** correspondente.
- Garante **sigilo** e **segurança na troca de informações**.

### 2. PKCS#1 OAEP
- É um **esquema de padding** para RSA.
- Aumenta a segurança contra ataques de **criptanálise**.
- Permite criptografar pequenas mensagens de forma segura.

### 3. Sockets TCP
- Protocolo **TCP/IP** para comunicação confiável.
- Permite conexão **direta entre cliente e servidor**.
- Garante que os dados cheguem na ordem correta.

---

## 📌 Funcionalidades do Projeto

- Geração automática de chaves **RSA de 4096 bits** para cliente e servidor.
- Troca de **chaves públicas** entre cliente e servidor.
- Envio de mensagens criptografadas:
  - Cliente envia uma mensagem segura.
  - Servidor descriptografa, processa (transforma em MAIÚSCULA) e retorna a resposta criptografada.
- Comunicação bidirecional **100% segura**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **socket** → comunicação TCP/IP.
- **PyCryptodome** → biblioteca de criptografia:
  - `RSA` → geração de chaves públicas/privadas.
  - `PKCS1_OAEP` → algoritmo de cifra assimétrica.

---

## 📂 Estrutura dos Arquivos

- `Simple_tcpClient.py` → código do **cliente**.
- `Simple_tcpServer.py` → código do **servidor**.

---

## ⚙️ Funcionamento Detalhado

### 1. Servidor

1. Gera **par de chaves RSA (4096 bits)**:
   - `server_private` → chave privada.
   - `server_public` → chave pública.
2. Cria um **socket TCP**, vincula ao endereço e porta definidos (`HOST`, `PORT`) e aguarda conexão.
3. Envia sua **chave pública** para o cliente.
4. Recebe a **chave pública do cliente**.
5. Recebe a **mensagem criptografada** do cliente.
6. **Descriptografa** a mensagem com sua chave privada.
7. Converte a mensagem recebida para **maiúscula**.
8. **Criptografa** a resposta usando a **chave pública do cliente**.
9. Envia a resposta criptografada ao cliente.

### 2. Cliente

1. Gera **par de chaves RSA (4096 bits)**:
   - `client_private` → chave privada.
   - `client_public` → chave pública.
2. Conecta ao servidor via **socket TCP**.
3. Recebe a **chave pública do servidor**.
4. Envia sua **chave pública** ao servidor.
5. Solicita uma **mensagem** ao usuário.
6. **Criptografa** a mensagem com a chave pública do servidor.
7. Envia a mensagem criptografada ao servidor.
8. Recebe a **resposta criptografada**.
9. **Descriptografa** a resposta com sua chave privada.
10. Exibe o resultado na tela.

---

## ▶️ Como Executar

### 1. Instale as dependências
```bash
pip install pycryptodome
```

### 2. Dê o comando que executa os arquivos de cliente e servidor
```bash
python Simple_tcpClient.py ## Cliente
python Simple_tcpClient.py ## Servidor
```
