

import librosa
import numpy as np


def preprocess_audio(audio_file, sr=22050, n_fft=2048, hop_length=256, n_mels=80):
    # load audio file
    audio, sr = librosa.load(audio_file, sr=sr)


    # compute mel spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(audio, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)


    # convert mel spectrogram to decibel scale
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)


    # normalize mel spectrogram
    mel_spectrogram_norm = (mel_spectrogram_db - mel_spectrogram_db.min()) / (mel_spectrogram_db.max() - mel_spectrogram_db.min())


    return mel_spectrogram_norm