# rgd_maker
[Trello](https://trello.com/b/GVCmj2GP/rdg-maker)

# Create MP4 for YouTube

``ffmpeg -loop 1 -framerate 1 -i image.png -i audio.mp3 -map 0:v -map 1:a -r 10 -vf "scale='iw-mod(iw,2)':'ih-mod(ih,2)',format=yuv420p" -movflags +faststart -shortest -fflags +shortest -max_interleave_delta 100M output.mp4``

[Documentation](https://stackoverflow.com/questions/64375367/python-convert-mp3-to-mp4-with-static-image)