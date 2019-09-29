import librosa
from scipy import signal
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

clap,sr1=librosa.load(path='PCMSoundSample.wav',sr=48000,mono=True,duration=8) 
#path -> 사운드파일경로 sr -> sample rate mono -> 사운드 채널수 duration -> 사운드길이

D=librosa.stft(clap,n_fft=2**11)
y_mag = np.abs(D)
y_mag_db=librosa.amplitude_to_db(y_mag,ref=np.max)
librosa.display.specshow(y_mag_db,y_axis='log',x_axis='time')
plt.title('Specctrogram')
plt.colorbar(label="dB")
plt.tight_layout()
plt.show()

step,sr2=librosa.load(path='walk_crop.wav')
D2=librosa.stft(step,n_fft=2**11)
y_mag2=np.abs(D2)
y_mag2_db=librosa.amplitude_to_db(y_mag2,ref=np.max)
librosa.display.specshow(y_mag2_db,y_axis='log',x_axis='time')
plt.title('Specctrogram')
plt.colorbar(label="dB")
plt.tight_layout()
plt.show()

org,sr3=librosa.load(path='ORGANCH2.wav')
D3=librosa.stft(org,n_fft=2**11)
y_mag3=np.abs(D3)
y_mag3_db=librosa.amplitude_to_db(y_mag3,ref=np.max)
librosa.display.specshow(y_mag2_db,y_axis='log',x_axis='time')
plt.title('Specctrogram')
plt.colorbar(label="dB")
plt.tight_layout()
plt.show()