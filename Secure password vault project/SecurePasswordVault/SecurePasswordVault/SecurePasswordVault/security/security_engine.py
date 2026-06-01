import hashlib
import string
import secrets
from cryptography.fernet import Fernet 

class SecurityEngine:
    def __init__(self):
        self.key = b'uV9v_7qW4XN_E-ZfF1X_M2p5Z8kS_L3n5R7t9V1W3Y4=' 
        self.cipher = Fernet(self.key)
    def hash_master_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def encrypt_password(self, plain_text):
        return self.cipher.encrypt(plain_text.encode()).decode()

    def decrypt_password(self, cipher_text):
        return self.cipher.decrypt(cipher_text.encode()).decode()

    def generate_strong_password(self, length=14):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(chars) for _ in range(length))

    def check_strength(self, password):
        score = 0
        if len(password) >= 10: score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in string.punctuation for c in password): score += 1
        
        if score == 3: return "Strong "
        if score == 2: return "Medium "
        return "Weak "

    def caesar_demo(self, text, shift=3):
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += char
        return result