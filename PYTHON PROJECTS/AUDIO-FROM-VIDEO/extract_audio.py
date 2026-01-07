# Install moviepy if not already installed
# pip install moviepy

from moviepy import VideoFileClip

# Load the video file
cvt_video = VideoFileClip("vid.mp4")

# Extract the audio
ext_audio = cvt_video.audio

# Write the audio to an MP3 file
ext_audio.write_audiofile("extracted_audio.mp3")
