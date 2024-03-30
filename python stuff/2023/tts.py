import numpy as np
import torch
import argparse


# Define command line arguments
parser = argparse.ArgumentParser(description='Generate speech from text using TTS model')
parser.add_argument('--input_text', type=str, required=True, help='Input text to synthesize')
parser.add_argument('--output_file', type=str, required=True, help='Path to output audio file')
parser.add_argument('--model_file', type=str, required=True, help='Path to pre-trained TTS model checkpoint')


# Load pre-trained TTS model
model = torch.load(args.model_file)


# Preprocess input text
input_ids = model.text_to_sequence(args.input_text)


# Generate speech from input text using TTS model
with torch.no_grad():
    output_mel = model.generate(input_ids)
    output_mel = output_mel[0].cpu().numpy()
    output_wav = librosa.feature.inverse.mel_to_audio(output_mel, sr=22050, hop_length=256, n_fft=1024)


# Save output audio file
librosa.output.write_wav(args.output_file, output_wav, sr=22050)