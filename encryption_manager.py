from cryptography.fernet import Fernet

key = b'0123456789abcdef0123456789abcdef'  # 32-byte key FOR TESTING ONLY
#key = Fernet.generate_key()

cipher_suite = Fernet(key)

def encrypt_password(password):
    """Encrypts a password."""
    # Ensure the password is bytes
    if isinstance(password, str):
        password = password.encode()
    encrypted_password = cipher_suite.encrypt(password)
    return encrypted_password

def decrypt_password(encrypted_password):
    """Decrypts a password."""
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password