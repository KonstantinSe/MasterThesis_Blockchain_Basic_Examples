from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# Schlüsselpaar wird generiert
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()
print(public_key)
print(private_key)
# Nachricht, die verschlüsselt werden soll
message = b"Geheime Nachricht"

# Nachricht mit dem öffentlichen Schlüssel verschlüsseln
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Verschlüsselte Nachricht:", ciphertext)

# Nachricht mit dem privaten Schlüssel entschlüsseln
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Entschlüsselte Nachricht:", decrypted_message)