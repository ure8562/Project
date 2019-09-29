[x,fs,nb] = wavread('PCMSoundSample.wav');
L=209494
% x의 길이
n = length(x);
%시간에 관한 표시
t = [0 : 1/fs : (n-1)/fs]';
%시간 축으로 불러 들이 데이터를 보여주기
%subplot(2,2,1); plot(t,x);
% 간단한 푸리에 변환
X = fft(x)/n;
%f에 관한 단위 설정
f = [0 : fs/n : (n-1)*fs/n]';
% 그림으로 절대값 보여주기
%subplot(2,2,2); plot(f,abs(X))
Y=fft(x);
P2=(abs(Y/L));

P1=P2(1:L/2+1);
P1(2:end-1)=2*P1(2:end-1);

F=fs*(0:(L/2))/L;
figure
plot(F,P1)
xlabel('(Hz)')
ylabel('Magnitude')

t1=P1(500:20000);
t2=P1(20000:40000);
t3=P1(40000:60000);
t4=P1(60000:80000);
t5=P1(80000:100000);

mean(t1)
mean(t2)
mean(t3)
mean(t4)
mean(t5)



