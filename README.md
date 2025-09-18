# EC10 - Tópicos Avançados em Redes

## N1 - Atividade RSA (Criptografia Assimétrica)

### 👩‍💻 Integrantes
- Claudia Galindo Santos - 081210014 
- Mayara Silva Azevedo - 081210029
- Nadielly Oliveira Santos - 081210024

---

## 🔐 Comunicação Cliente-Servidor com RSA (4096 bits)

Este projeto demonstra uma comunicação **segura** entre um **cliente** e um **servidor** utilizando **Python**, **sockets** e **criptografia assimétrica RSA** implementada manualmente, sem bibliotecas externas.  
O objetivo é enviar mensagens de forma segura, garantindo **confidencialidade**, ou seja, apenas o destinatário legítimo consegue ler a mensagem.

---

## 📚 Conceitos Teóricos

### 1. Criptografia Assimétrica (RSA)
- Utiliza um **par de chaves**: pública e privada.
- Mensagens criptografadas com a **chave pública** só podem ser descriptografadas pela **chave privada** correspondente.
- Garante **sigilo** e **segurança na troca de informações**.

### 2. Sockets TCP
- Protocolo **TCP/IP** para comunicação confiável.
- Permite conexão **direta entre cliente e servidor**.
- Garante que os dados cheguem na ordem correta.

### 3. Implementação Manual do RSA
- Geração de **números primos grandes** (4096 bits) usando teste de primalidade Miller-Rabin.
- Cálculo de **chaves públicas e privadas** sem bibliotecas externas.
- Criptografia e descriptografia feita via **aritmética modular** (`pow`).

---

## 📌 Funcionalidades do Projeto

- Geração automática de chaves **RSA de 4096 bits** para cliente e servidor.
- Troca de **chaves públicas** entre cliente e servidor.
- Envio de mensagens criptografadas:
  - Cliente envia uma mensagem segura.
  - Servidor descriptografa, processa (transforma em MAIÚSCULA) e retorna a resposta criptografada.
- Comunicação bidirecional **100% segura**, sem dependências externas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **socket** → comunicação TCP/IP.
- **random e math** → geração de primos e operações matemáticas para RSA.
- **Funções próprias** → teste de primalidade, inverso modular, criptografia/descriptografia.

---

## 📂 Estrutura dos Arquivos

- `Simple_tcpClient.py` → código do **cliente**.
- `Simple_tcpServer.py` → código do **servidor**.

---

## ⚙️ Funcionamento Detalhado

### 1. Servidor

1. Gera **par de chaves RSA (4096 bits)**:
   - `private` → chave privada.
   - `public` → chave pública.
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
   - `private` → chave privada.
   - `public` → chave pública.
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

### 1. Dê o comando que executa os arquivos de cliente e servidor
```bash
python Simple_tcpServer.py ## Servidor
python Simple_tcpClient.py ## Cliente
```

# 📊 Análise do Tráfego com Wireshark

A imagem abaixo mostra a captura do tráfego TCP entre o Cliente (Alice) e o Servidor (Bob) utilizando o protocolo **RSA autoral**:

<img width="1890" height="939" alt="image" src="https://github.com/user-attachments/assets/75d492bb-481b-4e48-ad79-461ce05b2515" />

- **Fonte:** IP do cliente `10.1.70.36`  
- **Destino:** IP do servidor `10.1.70.35`  
- **Porta do servidor:** `1300`  
- **Protocolo:** TCP

## Observações importantes:

- Cada linha da captura representa um segmento TCP enviado ou recebido.  
- O **payload** (lado direito, em hexadecimal) mostra os dados **criptografados**, garantindo que a mensagem trocada entre cliente e servidor **não pode ser lida por terceiros**.  
- O fluxo demonstra o **handshake TCP inicial**, envio da mensagem criptografada e recebimento da resposta criptografada.  
- Apesar de o Wireshark capturar os pacotes, os dados da mensagem permanecem **cifrados**, evidenciando o funcionamento seguro do **RSA autoral** implementado.

📌 **Considerações finais:** a comunicação cliente-servidor está fluindo corretamente, e as mensagens estão protegidas contra interceptação.
