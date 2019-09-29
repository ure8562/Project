[x,fs,nb] = wavread('hi claps.wav');
L= 11488
% x�� ����
n = length(x);
%�ð��� ���� ǥ��
t = [0 : 1/fs : (n-1)/fs]';
%�ð� ������ �ҷ� ���� �����͸� �����ֱ�
%subplot(2,2,1); plot(t,x);
% ������ Ǫ���� ��ȯ
X = fft(x)/n;
%f�� ���� ���� ����
f = [0 : fs/n : (n-1)*fs/n]';
% �׸����� ���밪 �����ֱ�
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

t1=P1(100:1200);
t2=P1(1200:2300);
t3=P1(2300:3400);
t4=P1(3400:4500);
t5=P1(4500:5600);

mean(t1)
mean(t2)
mean(t3)
mean(t4)
mean(t5)

