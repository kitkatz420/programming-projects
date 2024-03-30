from moviepy.editor import *

sound = AudioFileClip("ruckus.mp4")
newsound = sound.subclip("00:02:45","00:06:45")   #audio from 13 to 15 seconds
newsound.write_audiofile("sound1.wav", 44100, 2, 2000,"pcm_s32le")




# Python code to convert video to audio
import moviepy.editor as mp
#import speech_recognition as sr

# Insert Local Video File Path
#clip = mp.VideoFileClip("ruckus.mp4")

# Insert Local Audio File Path
#clip.write_audiofile("sound2.wav",codec='pcm_s16le')
