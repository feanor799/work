clear all % �������� ������

x=randn([1,200]); %%��������� �������
n=length(x); % ���������� ������
xmin=x(1); % ����������� ��������
xmax=x(n); % ������������ ��������
fprintf('����� ������� n=%d\n',n)
fprintf('xmin=%14.7f\n',xmin)
fprintf('xmax=%14.7f\n',xmax)
Mx=mean(x); % �������������� ��������
fprintf('���������� �������������� �������� Mx=%14.7f\n',Mx)
Dx=var(x); % ���������
fprintf('��������� Dx=%14.7f\n',Dx)
Sx=std(x); % ������������������ ����������
fprintf('������������������ ���������� Sx=%14.7f\n',Sx)
Ax=skewness(x,0); % ����������� ����������
fprintf('���������� Ax=%14.7f\n',Ax)
Ex=kurtosis(x,0)-3; % ����������� �������
fprintf('������� Ex=%14.7f\n',Ex)
p=[0.9;0.95;0.99;0.999]; % ����� ������������� �����������
q=1-p; % ������ ����������
k=round(n^0.5); % ����� ���������� ��� ���������� �����������
d=(xmax-xmin)/k; % ������ ������� ���������
del=(xmax-xmin)/20; % ������� ����� � ������
xl=xmin-del;
xr=xmax+del; % ������� ��������� ��� ���������� ��������
fprintf('����� ���������� k=%d\n',k)
fprintf('������ ��������� h=%14.7f\n',d)
figure % ������� ����� ������
hist(x,k) % ��������� �����������
dlist={'Exponential';'Normal';'Uniform'};
dlistr={'����������������';'����������';'�����������'};
dparname={{'mu'};{'mu' 'sigma'};{'a' 'b'}};
ndist=length(dlist); % ���������� �������������
for idist=1:ndist, % ��������� ��������� ��� ���� �������������
  phatone=mle(x,'distribution',dlist{idist});
  phat{idist}=phatone; % ���������
end
disp('��������� ��������� ������������� �� ���:')
for idist=1:ndist, % �������� ��������� ��� ���� �������������
  fprintf('%s �������������:',dlistr{idist});
  parname=dparname{idist}; % ������ ����������
  phatone=phat{idist}; % �������� ����������
  for ipar=1:length(parname), % �������� ���������
    fprintf('  %s=%14.10f;',parname{ipar},phatone(ipar));
  end
  fprintf('\n');
end
[Fi,xi]=ecdf(x); % ������������ ������� �������������
figure % ������� ����� ������
ecdfhist(Fi,xi,k) % ��������� ������������� �����������


for idist=1:ndist, % ������ ������������� �������������
  phatone=phat{idist}; % �������� ����������
  com=['pdf(''' dlist{idist} ''',xpl']; % ������� 
  for ipar=1:length(phatone), % ��������� ���������
    com=[com ',' sprintf('%d',phatone(ipar))];
  end
  com=[com ')']; % ������������ �������
  ypl=eval(com); % ��������� ������� - ��������� f(x)
  plot(xpl,ypl,'k-') % �������� �� ������
  [ym,iym]=max(ypl); % �������� �� �������
  h=text(xpl(iym),ym,dlist{idist}); % �������� �������������
  set(h,'FontName','Times New Roman Cyr','FontSize',10)
end
hold off % ��������� ��������
set(get(gcf,'CurrentAxes'),...
  'FontName','Times New Roman Cyr','FontSize',10)
title('\bf������������ � �������������\rm \itf\rm(\itx\rm)') % ���������
xlim([xl xr]) % ������� �� ��� OX
xlabel('\itx') % ����� ��� x
ylabel('\itf\rm(\itx\rm)') % ����� ��� y
qq=[]; % ����������� ������ ����������
for idist=1:ndist, % �������� �����������
  phatone=phat{idist}; % �������� ����������
  com=['cdf(''' dlist{idist} ''',x']; % ������� 
  for ipar=1:length(phatone), % ��������� ���������
    com=[com ',' sprintf('%d',phatone(ipar))];
  end
  com=[com ')']; % ������������ �������
  Fx=eval(com); % ��������� ������� - ��������� F(x)
  [hkolm,pkolm,kskolm,cvkolm]=kstest(x,[x Fx],0.1,0);
  qq=[qq pkolm]; % ����������� ������ ����������
end
[maxqq,bdist]=max(qq); % ������� ������ �������������
fprintf(['�������� �������� �����������:\n',...
  '����� ����� �������� %s �������������;\n'...
  '����������� ������� ���������� ��� ���� = %8.5f\n'], ...
  dlistr{bdist},maxqq);
figure % ������� ����� ������
cdfplot(x); % ������������ ������� �������������
phatone=phat{bdist}; % ��������� ���������� �������������
com=['cdf(''' dlist{bdist} ''',xpl']; % ������� 
for ipar=1:length(phatone), % ��������� ���������
  com=[com ',' sprintf('%d',phatone(ipar))];
end
com=[com ')']; % ������������ �������
del=(xmax-xmin)/20; % ������� ����� � ������
xl=xmin-del;
xr=xmax+del; % ������� ��������� ��� ���������� ��������
xpl=linspace(xl,xr,1000); % �������� ��� ��������
Fxpl=eval(com); % ��������� F(x) ��� ���������� �������������
hold on % ��� ��������� �� ���� �� �������
plot(xpl,Fxpl,'r'); % ���������� F(x)
hold off
set(get(gcf,'CurrentAxes'),...
  'FontName','Times New Roman Cyr','FontSize',10)
title(['\bf��������� ' dlistr{bdist} ' �������������'])
xlabel('\itx') % ����� ��� x
ylabel('\itF\rm(\itx\rm)') % ����� ��� y
ab=[]; % ���������� � ����������� ��������
for idist=1:ndist, % �������� �������
  phatone=phat{idist}; % �������� ����������
  com=['chi2test(x'',n/10,0.1,''' dlist{idist} '''']; % ������� 
  for ipar=1:length(phatone), % ��������� ���������
    com=[com ',' sprintf('%d',phatone(ipar))];
  end
  com=[com ')']; % ������������ �������
  [a1,b1]=eval(com); % ��������� ������� - ������� ���� �������
  ab=[ab;[a1 b1]]; % ���������� � ����������� ������ ����������
end
[maxdab,bdistp]=max(diff(ab')'); % ������� ������ �������������