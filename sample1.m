clear

[x,fs,nb] = wavread('ORGANCH2.wav');


N=length(data);
F1=0:fs/N:fs-fs/N;
FFT_data=fft(data);

figure;

plot(F1(1:N),abs(FFT_data(1:N)));

xlabel('Frequency')
ylabel('Amplitude')
 
axis([0 100 0 100])

grid on
