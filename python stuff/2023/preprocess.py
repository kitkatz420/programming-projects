import numpy as np
import librosa
import argparse
import os


# Define command line arguments
parser = argparse.ArgumentParser(description='Preprocess audio data for AutoVC and TTS models')
parser.add_argument('--input_dir', type=str, required=True, help='Path to directory containing input audio files')
parser.add_argument('--output_dir', type=str, required=True, help='Path to directory to save preprocessed audio files

