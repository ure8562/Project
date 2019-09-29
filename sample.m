[x,fs,nb] = wavread('walk_crop.wav');


n = length(x);

t = [0 : 1/fs : (n-1)/fs]';

subplot(2,2,1); plot(t,x);

X = fft(x)/n;

f = [0 : fs/n : (n-1)*fs/n]';

subplot(2,2,2); plot(f,abs(X))










