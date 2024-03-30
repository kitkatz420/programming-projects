from pydub import AudioSegment
from multiprocessing import Pool
import os

def convert_mp3_to_wav(mp3_file, wav_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)

    # Export the audio as WAV
    audio.export(wav_file, format='wav')

def process_file(mp3_file):
    wav_file = os.path.splitext(mp3_file)[0] + '.wav'
    convert_mp3_to_wav(mp3_file, wav_file)

if __name__ == '__main__':
    # Specify the input directory containing MP3 files
    input_file = input("what is your mp3 file named leave out the .mp4 part ")
    output_file = input("what is your wav file to be named ")
    input_name = input_file + ".mp4"
    output_name = output_file + ".wav"
    input_directory = "C:\\Users\\cats\\Documents\\mp3"

    # Get a list of all MP3 files in the input directory
    mp3_files = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith('.mp3')]

    # Specify the number of processes to run concurrently
    num_processes = 4

    # Create a multiprocessing pool
    pool = Pool(processes=num_processes)

    # Process the MP3 files using multiple processes
    pool.map(process_file, mp3_files)

    # Close the pool
    pool.close()
    pool.join()
