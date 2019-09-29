[x,fs,nb] = wavread('CLRZ.wav');
L=8532
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

t1=P1(100:850);
t2=P1(850:1750);
t3=P1(1750:2600);
t4=P1(2600:3450);
t5=P1(3450:4200);

mean(t1)
mean(t2)
mean(t3)
mean(t4)
mean(t5)

