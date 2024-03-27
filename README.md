# Conversor de YouTube para MP3

Este script em Python permite que você baixe vídeos do YouTube como arquivos de áudio MP3. Ele utiliza a biblioteca `pytube` para obter detalhes dos vídeos do YouTube e `moviepy` para lidar com a conversão do formato MP4 para MP3.

## Pré-requisitos
- Python 3.x
- Pacotes Python necessários: `pytube`, `moviepy`

## Instalação
1. Clone este repositório para sua máquina local ou baixe o script diretamente.
2. Certifique-se de que o Python e os pacotes necessários estejam instalados.
3. Coloque o script no diretório desejado.

## Uso
1. Crie um arquivo de texto chamado `songs.txt` no mesmo diretório do script.
2. Em `songs.txt`, liste os títulos dos vídeos do YouTube que você deseja converter para MP3, cada um em uma nova linha.
3. Execute o script.
4. O script criará uma pasta chamada "MúsicasPorPython_X" (onde X é um número aleatório) no diretório do script.
5. Ele irá baixar cada vídeo do YouTube, converter para o formato MP3 e salvar na pasta criada.

## Exemplo de songs.txt
Despacito  
Shape of You  
Believer  


## Funções

1. **ConvertMp4ToMp3(mp4, mp3)**
   - Converte o arquivo MP4 fornecido para o formato MP3.
   - Parâmetros:
     - `mp4` (str): Caminho para o arquivo MP4 de entrada.
     - `mp3` (str): Caminho para salvar o arquivo MP3 de saída.

2. **getTheFirstResult(title)**
   - Recupera o ID do vídeo do primeiro resultado de uma busca no YouTube com base no título fornecido.
   - Parâmetros:
     - `title` (str): O título do vídeo a ser pesquisado.
   - Retorna:
     - `str`: ID do vídeo do primeiro resultado da busca.

3. **downloadAndConvertVideoToAudio(title, folderName)**
   - Baixa um vídeo do YouTube pelo seu título, converte-o para o formato MP3 e salva-o na pasta especificada.
   - Parâmetros:
     - `title` (str): O título do vídeo do YouTube.
     - `folderName` (str): O nome da pasta para salvar o arquivo de áudio.

## Observação
- O script baixa o áudio na melhor qualidade disponível (140).
- Ele exclui o arquivo MP4 baixado após a conversão para economizar espaço em disco.

## Aviso Legal
Este script destina-se apenas para uso pessoal. Certifique-se de ter os direitos necessários para baixar e usar o conteúdo antes de prosseguir.

Sinta-se à vontade para contribuir, relatar problemas ou sugerir melhorias!
