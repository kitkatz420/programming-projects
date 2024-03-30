import os
import sys
import subprocess
def convert_mp4_to_wav(mp4_file, wav_file):
    ''' convert mp4 to wav '''
    command = 'ffmpeg -i ' + mp4_file + ' -acodec pcm_s16le -ac 1 -ar 16000 ' + wav_file
    subprocess.call(command, shell=True)
def main():
    ''' main function '''
    if len(sys.argv) != 3:
        print('Usage: python mp4_to_wav.py <mp4_file> <wav_file>')
        sys.exit(1)
    mp4_file = sys.argv[1]
    wav_file = sys.argv[2]
    if not os.path.exists(mp4_file):
        print('Error: mp4 file does not exist.')
        sys.exit(1)
    convert_mp4_to_wav(mp4_file, wav_file)
if __name__ == '__main__':
    main()

