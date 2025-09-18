import socket
import random
from math import gcd

# ===== Funções auxiliares RSA =====
def is_prime(n, k=40):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0 and n != p:
            return False
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
        p |= (1 << bits - 1) | 1
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

# ===== Cliente =====
HOST = "10.1.70.35"
PORT = 1300

public, private = generate_rsa_keys(4096)
print("[Cliente] Chaves RSA 4096 bits geradas.")
print("\n--- CHAVE PÚBLICA DO CLIENTE ---", public)
print("\n--- CHAVE PRIVADA DO CLIENTE ---", private)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("[Cliente] Conectado ao servidor.")

# Recebe chave pública do servidor
server_public = eval(client.recv(8192).decode())
print("\n--- CHAVE PÚBLICA DO SERVIDOR ---", server_public)

# Envia chave pública do cliente
client.send(str(public).encode())

# Digita mensagem
mensagem = input("[Cliente] Digite a mensagem: ")
msg_int = int.from_bytes(mensagem.encode(), "big")

# Criptografa com chave pública do servidor
encrypted_msg = pow(msg_int, server_public[0], server_public[1])
client.send(str(encrypted_msg).encode())
print("[Cliente] Mensagem enviada.")

# Recebe resposta criptografada
encrypted_response = int(client.recv(8192).decode())
decrypted = pow(encrypted_response, private[0], private[1])
resp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big").decode()

print(f"[Cliente] Resposta recebida: {resp}")
client.close()