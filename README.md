<h1>Encoder :newspaper: </h1>

<h4 align='justify'>Encoder (codificador em ingles, no contexto de criptografia) eh um programa, dispositivo ou equipamento capaz de criptografar informacoes utilizando uma chave escolhida pelo usuario.
Somente deve ser revelada a verdadeira mensagem utilizando exatamente a mesma chave utilizada para gerar o texto codificado, caso contrario, a mensagem revelada deve ser diferente de modo a nao haver ligacao com a mensagem original, ou nem mesmo sendo revelada mensagem alguma.</h4>

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

- [x] Codificacao de textos com senha
- [x] Decodificacao de textos com senha

<br>

<h2>Pre-requisitos :books: </h2>

<!-- Nenhuma ferramenta de pre-requisito necessaria. -->

<ul>
<li>Git</li>
<li>Interpretador Python</li>
</ul>

<br>

<h2>Utilizacao :crystal_ball: </h2>

<h3>Iniciando</h3>

Clone o repositorio e acesse a pasta criada para ele
```cmd
git clone git@github.com:LucasGoncSilva/encoder.git

cd encoder
```

Crie um ambiente virtual para instalar as dependencias do projeto e ative-o
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

No primeiro campo de entrada, escreva a mensagem que deseja codificadar, inserindo uma senha no segundo campo. Em seguida, pressione o botao para criptografar. O texto criptografado saira no campo de saida, localizado no final da janela.


---

<h3>Descriptografar</h3>

Insira o token no primeiro campo de entrada e a senha utilizada para gerar o token no segundo campo. Se a senha for valida, a mensagem original saira no campo de saida, porem, caso a senha seja incorreta, sera exibido "senha invalida".

:warning: retire a letra b do inicio juntamente com as aspas no inicio e no fim do token (texto de saida) :warning: