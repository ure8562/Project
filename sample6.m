[x,fs,nb] = wavread('HIGLAS12.wav');
L=20072
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

t1=P1(100:2000);
t2=P1(2000:4000);
t3=P1(4000:6000);
t4=P1(6000:8000);
t5=P1(8000:10000);

mean(t1)
mean(t2)
mean(t3)
mean(t4)
mean(t5)

