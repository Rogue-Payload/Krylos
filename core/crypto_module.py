# core/crypto_module.py

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hmac
import os
import base64
import logging

# Initialize logging
logger = logging.getLogger(__name__)

# Constants
KEY_LENGTH = 32  # 256 bits for AES-256
IV_LENGTH = 16   # 128-bit IV for AES
HASH_ITERATIONS = 100_000  # Recommended for PBKDF2
SALT_SIZE = 16

# Function to generate a secure random key
def generate_key(password, salt=None):
    """
    Generates a secure AES key from a password using PBKDF2 HMAC with SHA-256.
    
    Parameters:
        password (str): The password to derive the key from.
        salt (bytes, optional): Optional salt. If not provided, a new one will be generated.

    Returns:
        tuple: Generated AES key and salt used.
    """
    if salt is None:
        salt = os.urandom(SALT_SIZE)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=salt,
        iterations=HASH_ITERATIONS,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    logger.info("AES key generated successfully.")
    return key, salt

# Function to encrypt data
def encrypt_data(data, key):
    """
    Encrypts data using AES-256 in CBC mode with a random IV.
    
    Parameters:
        data (str): The plaintext data to encrypt.
        key (bytes): The AES encryption key.

    Returns:
        str: Base64-encoded ciphertext with the IV prepended.
    """
    iv = os.urandom(IV_LENGTH)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad data to be multiple of AES block size
    padded_data = data + " " * (16 - len(data) % 16)
    ciphertext = encryptor.update(padded_data.encode()) + encryptor.finalize()
    logger.info("Data encrypted successfully.")
    return base64.b64encode(iv + ciphertext).decode()

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    """
    Decrypts AES-256 encrypted data with a prepended IV.
    
    Parameters:
        encrypted_data (str): The base64-encoded ciphertext with prepended IV.
        key (bytes): The AES decryption key.

    Returns:
        str: Decrypted plaintext.
    """
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:IV_LENGTH]
    ciphertext = encrypted_data[IV_LENGTH:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    logger.info("Data decrypted successfully.")
    return decrypted_data.decode().strip()

# Function to create a SHA-256 hash of the data
def hash_data(data):
    """
    Generates a SHA-256 hash of the given data.
    
    Parameters:
        data (str): The data to hash.

    Returns:
        str: Hexadecimal SHA-256 hash.
    """
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(data.encode())
    hash_value = digest.finalize()
    logger.info("Data hashed successfully.")
    return hash_value.hex()

# Function to verify data integrity with HMAC
def verify_hmac(data, key, provided_hmac):
    """
    Verifies HMAC for data integrity.

    Parameters:
        data (str): The data to verify.
        key (bytes): The key used for HMAC.
        provided_hmac (str): The HMAC to verify against.

    Returns:
        bool: True if HMAC matches, False otherwise.
    """
    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    h.update(data.encode())
    try:
        h.verify(base64.b64decode(provided_hmac))
        logger.info("HMAC verification succeeded.")
        return True
    except Exception:
        logger.warning("HMAC verification failed.")
        return False
