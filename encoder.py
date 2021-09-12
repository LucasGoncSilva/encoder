from tkinter import *
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def crypt():
    client_text = text_entry.get()
    text = bytes(client_text, encoding='ascii')

    client_password = password_entry.get()
    password = bytes(client_password, encoding="ascii")

    salt = b'\xecB\xfd\xf6\xaaw\xf0\x91[&\x83\x04\xe5\xe2ek'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))

    f = Fernet(key)

    token = f.encrypt(text)
    output_txt.set(f"{token}")


def decrypt():
    client_text = text_entry.get()
    text = bytes(client_text, encoding='ascii')

    client_password = password_entry.get()
    password = bytes(client_password, encoding="ascii")

    try:
        salt = b'\xecB\xfd\xf6\xaaw\xf0\x91[&\x83\x04\xe5\xe2ek'

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )

        key = base64.urlsafe_b64encode(kdf.derive(password))

        f = Fernet(key)

        token = f.decrypt(text)
        output_txt.set(f"{token}")

    except: output_txt.set("***SENHA  INVALIDA***"*3)



win = Tk()
win.title('Encoder')
win.configure(bg='black')


info = Label(
    win,
    text='INSIRA O TEXTO E A SENHA PARA (DES)CRIPTOGRAFAR',
    bg='black',
    fg='green2'
)
info.grid(column=10, row=10, padx=5, pady=5, )


rule1 = Label(
    win,
    text='*escreva sempre em minusculo',
    bg='black',
    fg='red'
)
rule1.grid(column=10, row=11)


rule2 = Label(
    win,
    text='*senha errada retorna "senha invalida"',
    bg='black',
    fg='red'
)
rule2.grid(column=10, row=12)


rule3 = Label(
    win,
    text='*primeiro campo "mensagem", segundo campo "senha"',
    bg='black',
    fg='red'
)
rule3.grid(column=10, row=13)


rule4 = Label(
    win,
    text='*nao utilize caracteres especiais',
    bg='black',
    fg='red'
)
rule4.grid(column=10, row=14)


rule5 = Label(
    win,
    text="*remova o b'<mensagem>' antes de descriptografar",
    bg='black',
    fg='red'
)
rule5.grid(column=10, row=15)


text_entry = Entry(
    win,
    width=64,
    bg='gray34',
    fg='white'
)
text_entry.grid(column=10, row=16, padx=5, pady=15)


password_entry = Entry(
    win,
    width=16,
    bg='gray34',
    fg='white',
    show='*'
)
password_entry.grid(column=10, row=17, padx=5, pady=15)


crypt_button = Button(
    win,
    text='Cript',
    command=crypt,
    bg='gray25',
    fg='green2'
)
crypt_button.grid(column=10, row=18)


decrypt_button = Button(
    win,
    text='Descript',
    command=decrypt,
    bg='gray25',
    fg='green2'
)
decrypt_button.grid(column=10, row=19)


output_txt = StringVar()
output_camp = Entry(
    win,
    textvariable=output_txt,
    state="readonly",
    width=64,
    bg='gray50',
    fg='black'
)
output_camp.grid(column=10, row=20, padx=5, pady=25)


win.mainloop()
