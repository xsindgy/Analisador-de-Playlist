# 🎵 Playlist Analyzer

> Analise sua playlist do Spotify direto pelo terminal — gráficos, estatísticas e relatório em PDF com poucos cliques!

---

## 📌 Sobre o projeto

O **Playlist Analyzer** é uma ferramenta de linha de comando feita em Python que lê os dados da sua playlist do Spotify exportados em `.CSV` e gera análises visuais completas.

### O que você pode descobrir sobre sua playlist:
- 🎤 Os **10 artistas** mais presentes
- 💿 Os **5 álbuns** com mais músicas
- 🎸 Os **gêneros musicais** dominantes
- ⏱️ A **duração total** da playlist em horas
- 📄 **Relatório completo em PDF** com todos os gráficos

---

## 🖥️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/xsindgy/analisador-playlist.git
cd analisador-playlist
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Exporte sua playlist do Spotify

Acesse [exportify.net](https://exportify.net), faça login com sua conta do Spotify e baixe a playlist desejada em `.CSV`.

![Exportify](screenshots/exportify.png)

### 4. Execute o programa

```bash
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

![Menu](screenshots/menu.png)

---

## 📸 Screenshots

### Código — Tratamento de erros ao carregar o arquivo
![Tratamento de erros](screenshots/tratamento_erros.png)

### Código — Limpeza de terminal
![Limpar terminal](screenshots/limpar_terminal.png)

### Código — Estrutura principal
![Main](screenshots/main_inicio.png)

### Código — Menu de opções
![Selecionar ação](screenshots/selecionar_acao.png)

### Resultado — Gráfico de álbuns
![Grafico albuns](screenshots/grafico_albuns.png)

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
|------------|-----|
| `pandas` | Leitura e manipulação dos dados CSV |
| `matplotlib` | Geração dos gráficos e exportação em PDF |

Instale tudo de uma vez:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito por [xsindgy](https://github.com/xsindgy)
