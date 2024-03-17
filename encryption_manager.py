from cryptography.fernet import Fernet

key = b'hB9z5aKST2nR20WxUbQXfihgAnvHzJ1RlSimgP3-Nkw='  # 32-byte key FOR TESTING ONLY
#key = Fernet.generate_key()

cipher_suite = Fernet(key)

def encrypt_password(password):
    """Encrypts a password."""
    # Ensure the password is in bytes
    if isinstance(password, str):
        password = password.encode()
    encrypted_password = cipher_suite.encrypt(password)
    return encrypted_password

def decrypt_password(encrypted_password):
    """Decrypts a password."""
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password