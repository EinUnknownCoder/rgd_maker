from cmath import exp
from openpyxl import load_workbook
from pytube import YouTube
from pydub import AudioSegment
import random
from datetime import datetime

wb = load_workbook(filename="songlist.xlsx", read_only=True)

sheet = wb["Songlist"]

playlist = []

#for x in range(2, 3):
for x in range(2, sheet.max_row + 1):

    url = sheet.cell(x, 1).value
    title = sheet.cell(x, 2).value
    artist = sheet.cell(x, 3).value
    start = sheet.cell(x, 5).value
    end = sheet.cell(x, 6).value

    print(" ".join([url, title, artist, str(start), str(end)]))

    yt = YouTube(url)

    print(yt.title)

    audio_stream = yt.streams.get_audio_only()

    print(audio_stream)

    file_name = artist + " - " + title + ".mp4"

    audio_stream.download("raw/", file_name)

    playlist.append(["raw/" + file_name, start, end])

wb.close()

print(playlist)

random.shuffle(playlist)

ending_song = AudioSegment.from_mp3("HandsUp.mp3")[20 * 1000:40 * 1000].fade_in(2000).fade_out(2000) + 4

starting_song = ending_song

export = starting_song

for x in playlist:
    
    print(x)

    start = x[1] - 10
    end = x[2] + 2
    song = AudioSegment.from_file(x[0])[start * 1000:end * 1000].fade_in(2000).fade_out(2000)

    export = export + song

export = export + ending_song

print("Exporting...")

export.export("export/" + str(datetime.now()) + ".mp3", format="mp3")