import torch
import numpy as np

def generate_speech(model, source_mel, target_mel):
    # convert mel spectrograms to tensors
    source_mel_tensor = torch.from_numpy(np.expand_dims(source_mel, axis=0)).float()
    target_mel_tensor = torch.from_numpy(np.expand_dims(target_mel, axis=0)).float()

    # pass mel spectrograms through AutoVC model to generate speaker embedding
    with torch.no_grad():
        source_embedding = model.encoder(source_mel_tensor)
        target_embedding = model.encoder(target_mel_tensor)
        speaker_embedding = model.speaker_embedding(source_embedding, target_embedding)

    # generate speech from speaker embedding using AutoVC decoder
    with torch.no_grad():
        generated_mel = model.decoder(speaker_embedding)
        generated_mel = generated_mel.squeeze().cpu().numpy()

    return generated_mel