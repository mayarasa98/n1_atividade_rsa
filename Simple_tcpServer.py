import socket
import random
from math import gcd

# ===== Funções auxiliares RSA =====
def is_prime(n, k=40):
    if n < 2:
        return False
    # primeiros primos para filtro rápido
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0 and n != p:
            return False
    # Miller-Rabin
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits=4096):
    while True:
        p = random.getrandbits(bits)
        p |= (1 << bits - 1) | 1  # garante bit mais alto e ímpar
        if is_prime(p):
            return p

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Sem inverso modular")
    return x % m

def generate_rsa_keys(bits=4096):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(e, phi) != 1:
        e = 3
    d = modinv(e, phi)
    return (e, n), (d, n)

# ===== Servidor =====
HOST = "10.1.70.35"
PORT = 1300

public, private = generate_rsa_keys(4096)
print("[Servidor] Chaves RSA 4096 bits geradas.")
print("\n--- CHAVE PÚBLICA DO SERVIDOR ---", public)
print("\n--- CHAVE PRIVADA DO SERVIDOR ---", private)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"[Servidor] Aguardando conexão em {HOST}:{PORT}...")

conn, addr = server.accept()
print(f"[Servidor] Cliente conectado: {addr}")

# Envia chave pública
conn.send(str(public).encode())

# Recebe chave pública do cliente
client_public = eval(conn.recv(8192).decode())
print("\n--- CHAVE PÚBLICA DO CLIENTE ---", client_public)

# Recebe mensagem criptografada
encrypted_msg = int(conn.recv(8192).decode())
decrypted_int = pow(encrypted_msg, private[0], private[1])
mensagem = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, "big").decode()
print(f"[Servidor] Mensagem recebida: {mensagem}")

# Responde em maiúscula
mensagem_maiuscula = mensagem.upper()
encrypted_response = pow(int.from_bytes(mensagem_maiuscula.encode(), "big"), client_public[0], client_public[1])

conn.send(str(encrypted_response).encode())
print("[Servidor] Resposta enviada.")
conn.close()