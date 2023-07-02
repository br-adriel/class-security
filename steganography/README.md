# Esteganografia

Os arquivos dessa pasta consistem em dois scripts que realizam a inserção de um
texto em uma imagem, e alguns arquivos de exemplo dessa prática.

## Executando localmente

Para executar esses scripts em sua máquina você precisa ter o
[Python 3](https://www.python.org/) instalado.

Observação: os passos a seguir consideram que você está usando um sistema Linux,
caso você esteja usando um sistema Windows, basta pesquisar o comando
equivalente.

### Instalação

1. Faça o clone do repositório

    ```bash
    git clone https://github.com/br-adriel/class-security.git
    ```

2. Abra a pasta [`steganography`](../steganography/) no terminal

3. Crie um ambiente virtual python

    ```bash
    python3 -m venv .venv
    ```

4. Ative o ambiente virtual

    ```bash
    source .venv/bin/activate
    ```

5. Instale as dependências

    ```bash
    pip install -r requirements.txt
    ```

### Escondendo a mensagem em uma imagem PNG

O exemplo a seguir utiliza a imagem e mensagem utilizadas no exeperimento, para
realizar os procedimentos com outros arquivos, basta alterar os comandos
colocando os caminhos dos arquivos desejados.

1. Execute o script `hide.py` passando o caminho da imagem e o caminho do
arquivo de texto com a mensagem secreta:

    ```bash
    python3 ./hide.py labepi.png secret.txt
    ```

### Recuperando a mensagem a partir da imagem

O exemplo a seguir utiliza a imagem e mensagem utilizadas no exeperimento, para
realizar os procedimentos com outros arquivos, basta alterar os comandos
colocando os caminhos dos arquivos desejados.

1. Execute o script `show.py` passando o caminho da imagem com a mensagem
secreta, opcionalmente você pode passar um argumento para o nome do arquivo de
saída:

    ```bash
    python3 ./show.py secret.png nome_personalisado.txt
    ```
