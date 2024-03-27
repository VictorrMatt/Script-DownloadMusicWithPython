import os
import random
from pytube import YouTube, Search
from moviepy.editor import *


def ConvertMp4ToMp3(mp4, mp3):
    """
    Convert the given mp4 file to mp3 format.

    Parameters:
        mp4 (str): Path to the input mp4 file.
        mp3 (str): Path to save the output mp3 file.
    """
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()


def getTheFirstResult(title):
    """
    Get the video ID of the first result from YouTube search.

    Parameters:
        title (str): The title of the video to search.

    Returns:
        str: Video ID of the first search result.
    """
    allResults = Search(title)
    return allResults.results[0].video_id  # ID from the First Result


def downloadAndConvertVideoToAudio(title, folderName):
    """
    Download a YouTube video by its title, convert it to mp3 format, and save it in the specified folder.

    Parameters:
        title (str): The title of the YouTube video.
        folderName (str): The name of the folder to save the audio file.
    """
    URL = "https://www.youtube.com/watch?v="
    videoId = getTheFirstResult(title)

    yt = YouTube(URL + videoId)
    stream = yt.streams.get_by_itag(140)

    VIDEO_FILE_PATH = fr"{os.getcwd()}\{yt.title}.mp4"
    AUDIO_FILE_PATH = fr"{os.getcwd()}\{folderName}\{yt.author} - {yt.title}.mp3"

    stream.download()
    ConvertMp4ToMp3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)

    os.remove(VIDEO_FILE_PATH)  # Delete Mp4 after the conversion


# Creating folder to save music
directoryName = "MusicsByPython_" + str(random.randint(0, 100))
path = os.path.join(os.getcwd(), directoryName)
os.mkdir(path)

# Running
with open("songs.txt", encoding="utf-8") as f:
    for line in f:
        downloadAndConvertVideoToAudio(line, directoryName)
