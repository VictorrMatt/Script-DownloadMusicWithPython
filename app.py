import yt_dlp
import os
import shutil
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def safe_filename(filename):
    return "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).rstrip()

def creatingFolderToSaveMusic():
    try:
        directoryName = "MusicsByPython_" + str(random.randint(0, 100))
        musicDirectoryPath = os.path.join(os.getcwd(), directoryName)
        os.mkdir(musicDirectoryPath)
        return directoryName, musicDirectoryPath
    except Exception as e:
        logging.error(f"Error creating music folder: {e}")
        raise

def downloadAudioAsMp3(title, folderName):
    try:
        title = title.strip()
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(os.getcwd(), folderName, '%(artist)s - %(title)s.%(ext)s'),
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f"ytsearch:{title}", download=True)
            video = info_dict['entries'][0]
            
            logging.info(f"Downloaded: {title}")
    except Exception as e:
        logging.error(f"Error processing {title}: {e}")

def readingAndDownloadingSongsToTheDirectory(directoryName):
    try:
        with open("songs.txt", encoding="utf-8") as f:
            for line in f:
                downloadAudioAsMp3(line, directoryName)
    except FileNotFoundError:
        logging.error("songs.txt file not found")
    except Exception as e:
        logging.error(f"Error reading songs file: {e}")

def organizeSongsInDirectory(musicDirectoryPath):
    try:
        songs = os.listdir(musicDirectoryPath)

        for song in songs:
            if song.endswith('.mp3'):
                artist = song.split(' - ')[0]

                artistFolder = os.path.join(musicDirectoryPath, artist)
                if not os.path.exists(artistFolder):
                    os.makedirs(artistFolder)

                shutil.move(
                    os.path.join(musicDirectoryPath, song), 
                    os.path.join(artistFolder, song)
                )
    except Exception as e:
        logging.error(f"Error organizing songs: {e}")

# Running
try:
    directoryName, musicDirectoryPath = creatingFolderToSaveMusic()
    readingAndDownloadingSongsToTheDirectory(directoryName)
    organizeSongsInDirectory(musicDirectoryPath)
except Exception as e:
    logging.error(f"Script execution failed: {e}")