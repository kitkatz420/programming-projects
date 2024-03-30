import torch
import torchaudio
import torchaudio.transform as T 
from waveglow.denoiser import Denoiser 
from waveglow.glow import WaveGlow
import torch.nn as nn

#user_file = input
#user_path = "C:\\Users\\cats\\Documents\\mp3" + input + ".wav"

class YourTextToSpeechModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, num_layers):
        super(YourTextToSpeechModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, text):
        embedded = self.embedding(text)
        output, _ = self.lstm(embedded)
        output = self.fc(output[:, -1, :])
        waveform = torch.tanh(output)
        return waveform.squeeze()

# load the text-to-speech (TTS model)
tts_model = YourTextToSpeechModel()

#set the desired text for synthesis
text = "hello bitches"

#generate the speech waveform from the text using tts model
synthesized_waveform = tts_model(text)

#set the sample rat eof the of the synthesized waveform
sample_rate = 22050 

#Load the audio file using torchaudio
waveform, sample_rate = torchaudio.load("C:\\Users\\cats\\Documents\\mp3" + input("output file name") + ".wav")#wav path

#Apply the Short-Time Fourier Transform (STFT) using torchaudio
stft = T.Spectrogram()(waveform)

#Convert the spectrogram into a logarithmic scale
log_spectrogram = torch.log10(stft + 1e-9)

#do further processing or use the spectrogram in your TTS model

#pass the normalized the spectrogram through the neural vocoder
normalized_spectrogram = (log_spectrogram - log_spectrogram.max())/(log_spectrogram.min())

#load the pre-trained WaveGlow model
waveglow = WaveGlow()

# Load the pre-trained denoiser for WaveGlow (optional)
denoiser = Denoiser(waveglow)

# set the model to evalutation mode
waveglow.eval()


# pass the normalized spectrogram through the WaveGlow model to synthesize the waveform
with torch.no_grad():
    synthesized_waveform = waveglow.infer(normalized_spectrogram)

if denoiser is not None:
    synthesized_waveform = denoiser(synthesized_waveform)

#optinally, convert the synthesized waveform to audio and save it
torchaudio.save('C:\\Users\\cats\\Documents\\mp3' + input + '.wav', synthesized_waveform[0].cpu(), sample_rate)
