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

main_color = '#fff'
secundary_color = '#4717f6'
alert_color = '#f00'



win = Tk()
win.title('Encoder')
win.configure(bg=main_color)


image = PhotoImage(file = 'icon.png')

win.iconphoto(True, image)


info = Label(
    win,
    text='INSIRA O TEXTO E A SENHA PARA (DES)CRIPTOGRAFAR',
    bg=main_color,
    fg=secundary_color
)
info.grid(column=10, row=10, padx=5, pady=5)


rule1 = Label(
    win,
    text='*evite escrever em maiúsculo',
    bg=main_color,
    fg=alert_color
)
rule1.grid(column=10, row=11)


rule2 = Label(
    win,
    text='*senha incorreta retornará "senha inválida"',
    bg=main_color,
    fg=alert_color
)
rule2.grid(column=10, row=12)


rule3 = Label(
    win,
    text='*no primeiro campo "mensagem", no segundo campo "senha"',
    bg=main_color,
    fg=alert_color
)
rule3.grid(column=10, row=13)


rule4 = Label(
    win,
    text='*não utilize caracteres especiais (ãàêè...)',
    bg=main_color,
    fg=alert_color
)
rule4.grid(column=10, row=14)


rule5 = Label(
    win,
    text="*remova o b'<mensagem>' antes de enviar o token",
    bg=main_color,
    fg=alert_color
)
rule5.grid(column=10, row=15)


text_entry = Entry(
    win,
    width=64,
    bg='#ddd',
    fg=secundary_color
)
text_entry.grid(column=10, row=16, padx=5, pady=15)


password_entry = Entry(
    win,
    width=16,
    bg='#ddd',
    fg=secundary_color,
    show='*'
)
password_entry.grid(column=10, row=17, padx=5, pady=15)


crypt_button = Button(
    win,
    text='Cript',
    command=crypt,
    bg=secundary_color,
    fg=main_color
)
crypt_button.grid(column=10, row=18)


decrypt_button = Button(
    win,
    text='Descript',
    command=decrypt,
    bg=secundary_color,
    fg=main_color
)
decrypt_button.grid(column=10, row=19)


output_txt = StringVar()
output_camp = Entry(
    win,
    textvariable=output_txt,
    state="readonly",
    width=64,
    fg='black'
)
output_camp.grid(column=10, row=20, padx=5, pady=25)


win.mainloop()
