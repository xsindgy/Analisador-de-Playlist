import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf_backend
from datetime import datetime
import os

# exibir tempo tortal
def tempo_total_em_h(df):
    """Exibe a duração total da playlist em horas."""
    if 'Duration (ms)' not in df.columns:
        print('Coluna de duração não encontrada no arquivo CSV.')
        return

    total_ms = df['Duration (ms)'].sum()
    total_h = total_ms / 1000 / 60 / 60
    total_min = (total_ms / 1000 / 60) % 60

    print(f'\nDuração total da playlist: {int(total_h)}h {int(total_min)}min\n')

# artitas mais presentes
def artistas_presentes(df):
    """Exibe os artistas mais presentes na playlist em gráfico de barras."""
    contagem = df['Artista(s)'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    contagem.plot(kind='bar', ax=ax, color='steelblue')

    ax.set_title('Top 10 Artistas da Playlist', fontsize=14, fontweight='bold')
    ax.set_xlabel('Artista(s)')
    ax.set_ylabel('Quantidade de músicas')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def tabela_albums(df):
    """Exibe os top 5 álbuns mais presentes na playlist em gráfico de barras."""
    contagem = df.groupby('Álbum').size().reset_index(name='Nº de Músicas')

    artistas = df.groupby('Álbum')['Artista(s)'].apply(
        lambda x: ', '.join(sorted(set(x)))
    ).reset_index()

    generos = df.groupby('Álbum')['Gênero(s)'].apply(
        lambda x: ', '.join(sorted(set(x.dropna())))
    ).reset_index()

    tabela = contagem.merge(artistas, on='Álbum').merge(generos, on='Álbum')
    tabela = tabela.sort_values('Nº de Músicas', ascending=False).head(5).reset_index(drop=True)

    fig, (ax_bar, ax_table) = plt.subplots(
        2, 1, figsize=(12, 8),
        gridspec_kw={'height_ratios': [2, 1.5]}
    )

    ax_bar.bar(tabela['Álbum'], tabela['Nº de Músicas'], color='steelblue')
    ax_bar.set_title('TOP 5 ÁLBUNS DA SUA PLAYLIST', fontsize=14, fontweight='bold')
    ax_bar.set_xlabel('Álbum')
    ax_bar.set_ylabel('Nº de Músicas')
    ax_bar.tick_params(axis='x', rotation=20)

    ax_table.axis('off')
    tabela_plot = ax_table.table(
        cellText=tabela.values,
        colLabels=tabela.columns,
        cellLoc='center',
        loc='center'
    )
    tabela_plot.auto_set_font_size(False)
    tabela_plot.set_fontsize(9)
    tabela_plot.auto_set_column_width(col=list(range(len(tabela.columns))))

    plt.tight_layout()
    plt.show()

# configurações do pdf
def _fig_capa(df):
    """Gera a página de capa com resumo da playlist."""
    total_musicas = len(df)
    total_artistas = df['Artista(s)'].nunique()
    total_albums = df['Álbum'].nunique()

    duracao_texto = ''
    if 'Duration (ms)' in df.columns:
        total_ms = df['Duration (ms)'].sum()
        total_h = int(total_ms / 1000 / 60 / 60)
        total_min = int((total_ms / 1000 / 60) % 60)
        duracao_texto = f'Duração total: {total_h}h {total_min}min'

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    fig.patch.set_facecolor('#1a1a2e')

    data_hoje = datetime.now().strftime('%d/%m/%Y')

    ax.text(0.5, 0.85, 'Relatorio da Playlist', ha='center', va='center',
            fontsize=22, fontweight='bold', color='white', transform=ax.transAxes)

    ax.text(0.5, 0.72, f'Gerado em {data_hoje}', ha='center', va='center',
            fontsize=12, color='#aaaaaa', transform=ax.transAxes)

    resumo = (
        f'Total de musicas: {total_musicas}\n'
        f'Artistas unicos: {total_artistas}\n'
        f'Albums unicos: {total_albums}'
    )
    if duracao_texto:
        resumo += f'\n{duracao_texto}'

    ax.text(0.5, 0.45, resumo, ha='center', va='center',
            fontsize=14, color='white', transform=ax.transAxes,
            linespacing=2.0)

    plt.tight_layout()
    return fig


def _fig_artistas(df):
    """Gera e retorna a figura dos artistas mais presentes."""
    contagem = df['Artista(s)'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    contagem.plot(kind='bar', ax=ax, color='steelblue')
    ax.set_title('Top 10 Artistas da Playlist', fontsize=14, fontweight='bold')
    ax.set_xlabel('Artista(s)')
    ax.set_ylabel('Quantidade de musicas')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig


def _fig_albums(df):
    """Gera e retorna a figura dos top 5 álbuns."""
    contagem = df.groupby('Álbum').size().reset_index(name='Nr de Musicas')
    artistas = df.groupby('Álbum')['Artista(s)'].apply(
        lambda x: ', '.join(sorted(set(x)))
    ).reset_index()
    generos = df.groupby('Álbum')['Gênero(s)'].apply(
        lambda x: ', '.join(sorted(set(x.dropna())))
    ).reset_index()

    tabela = contagem.merge(artistas, on='Álbum').merge(generos, on='Álbum')
    tabela = tabela.sort_values('Nr de Musicas', ascending=False).head(5).reset_index(drop=True)

    fig, (ax_bar, ax_table) = plt.subplots(
        2, 1, figsize=(12, 8),
        gridspec_kw={'height_ratios': [2, 1.5]}
    )

    ax_bar.bar(tabela['Álbum'], tabela['Nr de Musicas'], color='steelblue')
    ax_bar.set_title('TOP 5 ALBUMS DA PLAYLIST', fontsize=14, fontweight='bold')
    ax_bar.set_xlabel('Album')
    ax_bar.set_ylabel('Nr de Musicas')
    ax_bar.tick_params(axis='x', rotation=20)

    ax_table.axis('off')
    tabela_plot = ax_table.table(
        cellText=tabela.values,
        colLabels=tabela.columns,
        cellLoc='center',
        loc='center'
    )
    tabela_plot.auto_set_font_size(False)
    tabela_plot.set_fontsize(9)
    tabela_plot.auto_set_column_width(col=list(range(len(tabela.columns))))

    plt.tight_layout()
    return fig


def _fig_generos(df):
    """Gera e retorna a figura dos gêneros mais presentes."""
    contagem = (
        df['Gênero(s)']
        .dropna()
        .str.split(', ')
        .explode()
        .value_counts()
        .head(10)
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    contagem.plot(kind='bar', ax=ax, color='mediumseagreen')
    ax.set_title('Top 10 Generos da Playlist', fontsize=14, fontweight='bold')
    ax.set_xlabel('Genero')
    ax.set_ylabel('Quantidade')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig


# gerar arquivos em pdf

def exportar_pdf(df):
    """Exporta um relatório completo com todos os gráficos em PDF."""
    nome_arquivo = f'relatorio_playlist_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'

    print('\nGerando relatorio PDF, aguarde...')

    with pdf_backend.PdfPages(nome_arquivo) as pdf:
        # Capa com resumo
        fig = _fig_capa(df)
        pdf.savefig(fig, facecolor=fig.get_facecolor())
        plt.close(fig)

        # Top 10 artistas
        fig = _fig_artistas(df)
        pdf.savefig(fig)
        plt.close(fig)

        #  Top 5 álbuns
        fig = _fig_albums(df)
        pdf.savefig(fig)
        plt.close(fig)

        # Top 10 gêneros
        fig = _fig_generos(df)
        pdf.savefig(fig)
        plt.close(fig)

    caminho = os.path.abspath(nome_arquivo)
    print(f'Relatorio gerado com sucesso!')
    print(f'Arquivo salvo em: {caminho}\n')