from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encode(message, keyword):
    text = bytes(message, encoding='ascii')
    password = bytes(keyword, encoding="ascii")

    salt = b'\xecB\xfd\xf6\xaaw\xf0\x91[&\x83\x04\xe5\xe2ek'

    kdf = PBKDF2HMAC(
        algorithm = SHA256(),
        length = 32,
        salt = salt,
        iterations = 100000,
    )

    key = urlsafe_b64encode(kdf.derive(password))

    f = Fernet(key)

    token = f.encrypt(text)
    return token


def decode(message, keyword):
    text = bytes(message, encoding='ascii')
    password = bytes(keyword, encoding="ascii")

    try:
        salt = b'\xecB\xfd\xf6\xaaw\xf0\x91[&\x83\x04\xe5\xe2ek'

        kdf = PBKDF2HMAC(
            algorithm = SHA256(),
            length = 32,
            salt = salt,
            iterations = 100000,
        )

        key = urlsafe_b64encode(kdf.derive(password))

        f = Fernet(key)

        plain_txt = f.decrypt(text)
        return plain_txt

    except: return "***SENHA INCORRETA***"*3