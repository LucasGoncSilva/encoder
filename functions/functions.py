from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


warning = 'OPERAÇÃO INVÁLIDA; EVITE ELEMENTOS COMO "ã", "â", "é", "ç" E OUTROS CARACTERES ESPECIAIS.'


def encode(message, keyword):
    try:
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
        return str(token)[2:-1]

    except:
        return f'{warning}\n\nMensagem: {message}\nSenha: {keyword}'


def decode(message, keyword):
    token = bytes(message, encoding='ascii')
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

        plain_txt = f.decrypt(token)
        return str(plain_txt)[2:-1]

    except: return "** SENHA INCORRETA OU TEXTO NÃO CODIFICADO **"