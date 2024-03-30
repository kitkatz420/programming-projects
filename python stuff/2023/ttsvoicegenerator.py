from autovc import AutoVC
from audio_preprocessor import preprocess_audio
from tts_model_generator import generate_speech


# load the AutoVC model
model = AutoVC()


# preprocess the source and target audio files into mel spectrograms
source_mel = preprocess_audio("C:/Users/cats/Documents/"+ input("name your source audio no .wav: ") + ".wav")
target_mel = preprocess_audio("C:/Users/cats/Documents/" + input("name your target audio no.wav: ") + ".wav")


# generate speech using the AutoVC model
speaker_embedding = generate_speech(model, source_mel, target_mel)


# save the generated speech to an audio file
speaker_embedding.export("C:/Users/cats/Documents" + input("name of generated audio") + ".wav", format="wav")