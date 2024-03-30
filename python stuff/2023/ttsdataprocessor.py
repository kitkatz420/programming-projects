import librosa
import numpy as np


# Load audio file and corresponding transcript
audio_file = 'C:\\ttsproject\\dentures.wav'
transcript_file = 'C:\\ttsproject\\dentures.txt'
audio, sr = librosa.load(audio_file, sr=)
with open(transcript_file, 'r') as f:
    transcript = f.read().strip()


# Normalize volume levels
audio /= np.max(np.abs(audio))




# Compute spectrogram of audio data
spec = librosa.stft(audio, n_fft=20, hop_length=20)
spec_mag = np.abs(spec)


# Convert spectrogram to mel-scaled spectrogram
mel_basis = librosa.filters.mel(sr=sr, n_fft=20, n_mels=10)
mel_spec = np.dot(mel_basis, spec_mag)


# Log-transform mel-scaled spectrogram
log_mel_spec = np.log(mel_spec + 1e-6)
