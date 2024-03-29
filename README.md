# YouTube to MP3 Converter

Este script em Python permite que você baixe vídeos do YouTube como arquivos de áudio MP3. Ele também organiza as músicas baixadas em pastas por artistas.

## Funcionalidades

1. **Criar Pasta para Salvar Músicas**
   - Função: `creatingFolderToSaveMusic()`
   - Cria uma pasta para salvar as músicas baixadas.
   - Retorna:
     - Nome da pasta criada.
     - Caminho da pasta criada.

2. **Converter MP4 para MP3**
   - Função: `convertMp4ToMp3(mp4, mp3)`
   - Converte um arquivo MP4 para o formato MP3.
   - Parâmetros:
     - `mp4` (str): Caminho do arquivo MP4 de entrada.
     - `mp3` (str): Caminho para salvar o arquivo MP3 de saída.

3. **Obter Primeiro Resultado da Busca**
   - Função: `getTheFirstResult(title)`
   - Obtém o ID do vídeo do primeiro resultado da busca no YouTube.
   - Parâmetros:
     - `title` (str): Título do vídeo a ser pesquisado.
   - Retorna:
     - ID do vídeo do primeiro resultado da busca.

4. **Baixar e Converter Vídeo para Áudio**
   - Função: `downloadAndConvertVideoToAudio(title, folderName)`
   - Baixa um vídeo do YouTube pelo título, converte-o para MP3 e salva na pasta especificada.
   - Parâmetros:
     - `title` (str): Título do vídeo do YouTube.
     - `folderName` (str): Nome da pasta para salvar o arquivo de áudio.

5. **Ler, Baixar e Organizar Músicas**
   - Função: `readingAndDownloadingAndThenUploadingSongsToTheDirectory(directoryName)`
   - Lê os títulos das músicas de um arquivo, baixa e converte para áudio, e salva na pasta especificada.
   - Parâmetros:
     - `directoryName` (str): Nome da pasta para salvar os arquivos de áudio.

6. **Organizar Músicas na Pasta**
   - Função: `organizeSongsInDirectory(musicDirectoryPath)`
   - Organiza as músicas na pasta movendo-as para pastas de artistas.
   - Parâmetros:
     - `musicDirectoryPath` (str): Caminho da pasta contendo as músicas.

## Uso

1. Clone este repositório para sua máquina local.
2. Instale as dependências necessárias (`pytube`, `moviepy`).
3. Crie um arquivo de texto chamado `songs.txt` e liste os títulos dos vídeos do YouTube que deseja converter para MP3, um por linha.
4. Execute o script.

## Observações

- O script baixa o áudio na melhor qualidade disponível (140).
- Os arquivos MP4 baixados são excluídos após a conversão para economizar espaço em disco.
- As músicas são organizadas em pastas por artistas.

## Aviso Legal

Este script destina-se apenas para uso pessoal. Certifique-se de ter os direitos necessários para baixar e usar o conteúdo antes de prosseguir.

Sinta-se à vontade para contribuir, relatar problemas ou sugerir melhorias!
