from tkinter import *

from functions import encode, decode


def crypt():
    message = text_entry.get()
    keyword = password_entry.get()

    output_txt.set(f"{encode(message, keyword)}")


def decrypt():
    message = text_entry.get()
    keyword = password_entry.get()

    output_txt.set(f"{decode(message, keyword)}")

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
    text='* Apenas letras minúsculas e sem acentuação serão cifradas corretamente',
    bg=main_color,
    fg=alert_color
)
rule1.grid(column=10, row=11)


rule2 = Label(
    win,
    text='* No primeiro campo "mensagem", no segundo campo "senha"; saída no terceito campo',
    bg=main_color,
    fg=alert_color
)
rule2.grid(column=10, row=12, padx=5)


rule3 = Label(
    win,
    text="* Remova o b'<mensagem>' antes de enviar o token",
    bg=main_color,
    fg=alert_color
)
rule3.grid(column=10, row=13)


text_entry = Entry(
    win,
    width=64,
    bg='#ddd',
    fg=secundary_color
)
text_entry.grid(column=10, row=14, padx=5, pady=15)


password_entry = Entry(
    win,
    width=16,
    bg='#ddd',
    fg=secundary_color,
    show='*'
)
password_entry.grid(column=10, row=15, padx=5, pady=15)


crypt_button = Button(
    win,
    text='Cript',
    command=crypt,
    bg=secundary_color,
    fg=main_color
)
crypt_button.grid(column=10, row=16)


decrypt_button = Button(
    win,
    text='Descript',
    command=decrypt,
    bg=secundary_color,
    fg=main_color
)
decrypt_button.grid(column=10, row=17)


output_txt = StringVar()
output_camp = Entry(
    win,
    textvariable=output_txt,
    state="readonly",
    width=64,
    fg='black'
)
output_camp.grid(column=10, row=18, padx=5, pady=25)


win.mainloop()
