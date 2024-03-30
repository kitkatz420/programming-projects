#from audio_preprocessor import *
#from audio_preprocessor import n_mels
import torch
import torch.nn as nn

n_mels=80

class AutoVC(nn.Module):
    def __init__(self):
        super(AutoVC, self).__init__()


        # define the encoder network
        self.encoder = nn.Sequential(
            nn.Conv1d(in_channels=n_mels, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(),
            nn.Conv1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(),
            nn.Conv1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(),
            nn.Conv1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(),
            nn.Conv1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(),
            nn.Conv1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(),
            nn.Conv1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(),
            nn.Conv1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),




           
            nn.LeakyReLU(),
            nn.Conv1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(),
            nn.Conv1d(in_channels=512, out_channels=128, kernel_size=7, stride=1, padding=3),
        )


        # define the decoder network
        self.decoder = nn.Sequential(
            nn.ConvTranspose1d(in_channels=128, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.ConvTranspose1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.ConvTranspose1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.ConvTranspose1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.ConvTranspose1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.ConvTranspose1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.ConvTranspose1d(in_channels=512, out_channels=512, kernel_size=7, stride=1, padding=3),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.ConvTranspose1d(in_channels=512, out_channels=1, kernel_size=7, stride=1, padding=3),
        )


        # define the speaker embedding network
        self.speaker_encoder = nn.Sequential(
            nn.Linear(in_features=512, out_features=256),
            nn.LeakyReLU(),
            nn.Linear(in_features=256, out_features=128),
            nn.LeakyReLU(),
            nn.Linear(in_features=128, out_features=64),
        )


        self.speaker_decoder = nn.Sequential(
            nn.Linear(in_features=64, out_features=128),
            nn.LeakyReLU(),
            nn.Linear(in_features=128, out_features=256),
            nn.LeakyReLU(),
            nn.Linear(in_features=256, out_features=512),
        )


    def forward(self, source_mel, target_mel, speaker_embedding):
        # encode the source mel spectrogram
        z_s = self.encoder(source_mel)


        # encode the target mel spectrogram
        z_t = self.encoder(target_mel)


        # concatenate the source and target encodings along the channel dimension
        z = torch.cat([z_s, z_t], dim=1)


        # pass the concatenated encoding through the speaker embedding network
        speaker_code = self.speaker_encoder(speaker_embedding)


        # concatenate the speaker code with the concatenated encoding
        z = torch.cat([z, speaker_code.unsqueeze(2).expand(-1, -1, z.size(2))], dim=1)


        # decode the concatenated encoding to obtain the target mel spectrogram
        output_mel = self.decoder(z)


        return output_mel
