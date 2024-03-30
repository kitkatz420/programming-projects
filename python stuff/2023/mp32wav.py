# import required modules
from os import path
from pydub import AudioSegment
import glob


maindir = "C:\\Users\\cats\\Documents"
# assign files
input_file = input("what is your mp3 file named leave out the .mp4 part ")
output_file = input("what is your wav file to be named ")
input_name = input_file + ".mp4"
output_name = output_file + ".wav"
# convert mp3 file to wav file
sound = AudioSegment.from_mp4(input_name)
sound.export(output_name, format="wav")
