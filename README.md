# 🎵 Playlist Analyzer

> Analise sua playlist do Spotify direto pelo terminal — gráficos, estatísticas e relatório em PDF com poucos cliques!

---

## 📌 Sobre o projeto

O **Playlist Analyzer** é uma ferramenta de linha de comando feita em Python que lê os dados da sua playlist do Spotify exportados em `.CSV` e gera análises visuais completas.

### O que você pode descobrir sobre sua playlist:

* 🎤 Os **10 artistas** mais presentes
* 💿 Os **5 álbuns** com mais músicas
* 🎸 Os **gêneros musicais** dominantes
* ⏱️ A **duração total** da playlist em horas
* 📄 **Relatório completo em PDF** com todos os gráficos

---

## 🖥️ Como usar

### 1. Clone o repositório

```
git clone https://github.com/xsindgy/analisador-playlist.git
cd analisador-playlist
```

### 2. Instale as dependências

```
pip install -r requirements.txt
```

### 3. Exporte sua playlist do Spotify

Acesse [exportify.net](https://exportify.net), faça login com sua conta do Spotify e baixe a playlist desejada em `.CSV`.

[![Exportify](https://github.com/xsindgy/Analisador-de-Playlist/raw/main/screenshots/Captura%20de%20tela%202026-04-25%20235004.png)](https://github.com/xsindgy/Analisador-de-Playlist/blob/main/screenshots/Captura%20de%20tela%202026-04-25%20235004.png)

### 4. Execute o programa

```
python main.py
```

### 5. Cole o caminho do arquivo CSV

Quando solicitado, cole o caminho do arquivo `.CSV` exportado.

> ⚠️ **Atenção:** Cole o caminho **sem aspas**!
>
> ✅ Correto: `C:\Users\filip\Downloads\minha_playlist.csv`
>
> ❌ Errado: `"C:\Users\filip\Downloads\minha_playlist.csv"`

### 6. Escolha o que deseja analisar

[![Menu](https://github.com/xsindgy/Analisador-de-Playlist/raw/main/screenshots/selecionara%C3%A7aodesejada.png)](https://github.com/xsindgy/Analisador-de-Playlist/blob/main/screenshots/selecionara%C3%A7aodesejada.png)

---

## 📸 Screenshots

### Código — Tratamento de erros ao carregar o arquivo

[![Tratamento de erros](https://github.com/xsindgy/Analisador-de-Playlist/raw/main/screenshots/tratamento%20de%20erros.png)](https://github.com/xsindgy/Analisador-de-Playlist/blob/main/screenshots/tratamento%20de%20erros.png)

### Código — Limpeza de terminal

[![Limpar terminal](https://github.com/xsindgy/Analisador-de-Playlist/raw/main/screenshots/limparterminal.png)](https://github.com/xsindgy/Analisador-de-Playlist/blob/main/screenshots/limparterminal.png)

### Código — Estrutura principal

[![Main](https://github.com/xsindgy/Analisador-de-Playlist/raw/main/screenshots/mainpyinicio.png)](https://github.com/xsindgy/Analisador-de-Playlist/blob/main/screenshots/mainpyinicio.png)

### Código — Menu de opções

[![Selecionar ação](https://github.com/xsindgy/Analisador-de-Playlist/raw/main/screenshots/selecionara%C3%A7aodesejada.png)](https://github.com/xsindgy/Analisador-de-Playlist/blob/main/screenshots/selecionara%C3%A7aodesejada.png)

### Resultado — Gráfico de álbuns

[![Grafico albuns](https://github.com/xsindgy/Analisador-de-Playlist/raw/main/screenshots/Captura%20de%20tela%202026-04-25%20234758.png)](https://github.com/xsindgy/Analisador-de-Playlist/blob/main/screenshots/Captura%20de%20tela%202026-04-25%20234758.png)

---

## 📁 Estrutura do projeto

```
analisador-playlist/
│
├── main.py           # Arquivo principal — menu e fluxo do app
├── funcoes.py        # Funções de análise e geração de gráficos
├── requirements.txt  # Dependências do projeto
├── README.md         # Documentação
└── screenshots/      # Imagens usadas no README
```

---

## 📦 Dependências

| Biblioteca | Uso |
| --- | --- |
| `pandas` | Leitura e manipulação dos dados CSV |
| `matplotlib` | Geração dos gráficos e exportação em PDF |

Instale tudo de uma vez:

```
pip install -r requirements.txt
```

---

## 🛠️ Tecnologias utilizadas

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/xsindgy/Analisador-de-Playlist/blob/main/LICENSE) para mais detalhes.

---

Feito por [xsindgy](https://github.com/xsindgy)
