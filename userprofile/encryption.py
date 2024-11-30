import os
from cryptography.fernet import Fernet

ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', Fernet.generate_key())
fernet = Fernet(ENCRYPTION_KEY)

def encrypt_data(data:str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encryption_data: str) -> str:
    return fernet.decrypt(encryption_data.encode()).decode()