# import required modules
from os import path
from pydub import AudioSegment

# assign files
input_file = input()
output_file = input("what would you like to name the file")
input_name = output_file + ".mp3"
output_name = output_file + ".wav"
# convert mp3 file to wav file
sound = AudioSegment.from_mp3(input_name)
sound.export(output_name, format="wav")
