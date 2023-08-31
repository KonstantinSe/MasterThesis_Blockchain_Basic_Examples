import hashlib

data = "Rebe „Müller-Thurgau“ am 29.06.2023 in Meißen, Sachsen geerntet"
hash = hashlib.sha256(data.encode()).hexdigest()
print(f"Der SHA-256-Hash des Strings lautet: {hash}")