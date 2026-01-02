from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
from dotenv import load_dotenv

load_dotenv()   # 👈 THIS LINE FIXES EVERYTHING

KEY = os.getenv("AES_SECRET_KEY")

if KEY is None:
    raise ValueError("AES_SECRET_KEY not found in .env file")

KEY = KEY.encode()

def encrypt(data):
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data, AES.block_size))
    return iv + encrypted

def decrypt(data):
    iv = data[:16]
    encrypted = data[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted), AES.block_size)
