import torch
import librosa
import numpy as np
from tensorflow.keras import models

# Load the AutoVC model
autoencoder = models.load_model("path/to/your/model")

# Load the input audio file
audio_file, sr = librosa.load("path/to/your/audio/file.wav" + input + ".wav", sr=16000)

# Extract MFCC features from the input audio
mfccs = librosa.feature.mfcc(audio_file, sr=sr, n_mfcc=40)

# Normalize the MFCCs
mfccs_norm = (mfccs - mfccs.mean()) / mfccs.std()

# Convert the MFCCs to a tensor
mfccs_tensor = torch.tensor(mfccs_norm, dtype=torch.float32)

# Generate synthesized speech from the input audio
synth_mfccs = autoencoder.predict(mfccs_tensor.unsqueeze(0))

# Convert the synthesized MFCCs back to their original shape
synth_mfccs = synth_mfccs.squeeze().detach().numpy()

# Rescale the synthesized MFCCs to their original range
synth_mfccs = (synth_mfccs * mfccs.std()) + mfccs.mean()

# Convert the synthesized MFCCs back to audio
synth_audio = librosa.feature.inverse.mfcc_to_audio(synth_mfccs, sr=sr)

# Write the synthesized audio to a file
librosa.output.write_wav("path/to/output/" + input + ".wav", synth_audio, sr=sr)













