<h1>Encoder :lock: </h1>

<h4 align='justify'>Encoder (codificador em inglês, no contexto de criptografia) é um programa, dispositivo ou equipamento capaz de criptografar informações utilizando uma chave escolhida pelo usuário.
Somente será revelada a verdadeira mensagem utilizando exatamente a mesma chave utilizada para gerar o texto codificado, caso contrário, a mensagem revelada será diferente de modo a não haver ligação com a mensagem original, nem mesmo sendo revelada mensagem alguma.</h4>

<br>

<h2>Status do Projeto :chart_with_upwards_trend: </h2>

:heavy_check_mark: Finalizado com sucesso :heavy_check_mark:

<!-- :construction: Em andamento :construction: -->

<!-- :link: Confira [aqui](website). :link: -->

<br>

<h2>Tecnologias aplicadas :floppy_disk: :cloud: </h2>

<ul>
<li>TKinter (Python)</li>
</ul>

<br>

<h2>Features :star: </h2>

- [x] Codificação de textos com senha
- [x] Decodificação de textos com senha

<br>

<h2>Pré-requisitos :books: </h2>

<!-- Nenhuma ferramenta de pré-requisito necessaria. -->

<ul>
<li>Git</li>
<li>Interpretador Python</li>
</ul>

<br>

<h2>Utilização :crystal_ball: </h2>

<h3>Iniciando</h3>

Clone o repositório e acesse a pasta criada para ele
```cmd
git clone git@github.com:LucasGoncSilva/encoder.git

cd encoder
```

Crie um ambiente virtual para instalar as dependências do projeto e ative-o
```cmd
python -m venv venv_encoder

venv_encoder\Scripts\activate.bat
```

Execute o arquivo `encoder.py`
```cmd
python encoder.py
```


---

<h3>Criptografar</h3>

No primeiro campo de entrada, escreva a mensagem que deseja codificadar, inserindo uma senha no segundo campo. Em seguida, pressione o botão para criptografar. O texto criptografado sairá no campo de saida, localizado no final da janela.


---

<h3>Descriptografar</h3>

Insira o token no primeiro campo de entrada e a senha utilizada para gerar o token no segundo campo. Se a senha for válida, a mensagem original será exibida no campo de saida, porém, caso a senha seja incorreta, será exibido "senha inválida".

:warning: remova a letra b do inicio juntamente com as aspas no inicio e no fim do token (texto de saida na codificação) :warning: