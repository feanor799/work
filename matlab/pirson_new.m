clear all % очистить память

x=randn([1,200]); %%случайная выборка
n=length(x); % количество данных
xmin=x(1); % минимальное значение
xmax=x(n); % максимальное значение
fprintf('Объем выборки n=%d\n',n)
fprintf('xmin=%14.7f\n',xmin)
fprintf('xmax=%14.7f\n',xmax)
Mx=mean(x); % математическое ожидание
fprintf('Выборочное математическое ожидание Mx=%14.7f\n',Mx)
Dx=var(x); % дисперсия
fprintf('Дисперсия Dx=%14.7f\n',Dx)
Sx=std(x); % среднеквадратичное отклонение
fprintf('Среднеквадратичное отклонение Sx=%14.7f\n',Sx)
Ax=skewness(x,0); % несмещенная асимметрия
fprintf('Асимметрия Ax=%14.7f\n',Ax)
Ex=kurtosis(x,0)-3; % несмещенный эксцесс
fprintf('Эксцесс Ex=%14.7f\n',Ex)
p=[0.9;0.95;0.99;0.999]; % задаём доверительные вероятности
q=1-p; % уровни значимости
k=round(n^0.5); % число интервалов для построения гистограммы
d=(xmax-xmin)/k; % ширина каждого интервала
del=(xmax-xmin)/20; % добавки влево и вправо
xl=xmin-del;
xr=xmax+del; % границы интервала для построения графиков
fprintf('Число интервалов k=%d\n',k)
fprintf('Ширина интервала h=%14.7f\n',d)
figure % создаем новую фигуру
hist(x,k) % построили гистограмму
dlist={'Exponential';'Normal';'Uniform'};
dlistr={'экспоненциальное';'нормальное';'равномерное'};
dparname={{'mu'};{'mu' 'sigma'};{'a' 'b'}};
ndist=length(dlist); % количество распределений
for idist=1:ndist, % подбираем параметры для всех распределений
  phatone=mle(x,'distribution',dlist{idist});
  phat{idist}=phatone; % запомнили
end
disp('Параметры различных распределений по ПМП:')
for idist=1:ndist, % печатаем параметры для всех распределений
  fprintf('%s распределение:',dlistr{idist});
  parname=dparname{idist}; % список параметров
  phatone=phat{idist}; % значения параметров
  for ipar=1:length(parname), % печатаем параметры
    fprintf('  %s=%14.10f;',parname{ipar},phatone(ipar));
  end
  fprintf('\n');
end
[Fi,xi]=ecdf(x); % эмпирическая функция распределения
figure % создаем новую фигуру
ecdfhist(Fi,xi,k) % построили нормированную гистограмму


for idist=1:ndist, % рисуем теоретические распределения
  phatone=phat{idist}; % значения параметров
  com=['pdf(''' dlist{idist} ''',xpl']; % команда 
  for ipar=1:length(phatone), % добавляем параметры
    com=[com ',' sprintf('%d',phatone(ipar))];
  end
  com=[com ')']; % сформировали команду
  ypl=eval(com); % выполнили команду - вычислили f(x)
  plot(xpl,ypl,'k-') % добавили на график
  [ym,iym]=max(ypl); % максимум на графике
  h=text(xpl(iym),ym,dlist{idist}); % название распределения
  set(h,'FontName','Times New Roman Cyr','FontSize',10)
end
hold off % выключили задержку
set(get(gcf,'CurrentAxes'),...
  'FontName','Times New Roman Cyr','FontSize',10)
title('\bfЭмпирическая и теоретические\rm \itf\rm(\itx\rm)') % заголовок
xlim([xl xr]) % границы по оси OX
xlabel('\itx') % метка оси x
ylabel('\itf\rm(\itx\rm)') % метка оси y
qq=[]; % критические уровни значимости
for idist=1:ndist, % критерий Колмогорова
  phatone=phat{idist}; % значения параметров
  com=['cdf(''' dlist{idist} ''',x']; % команда 
  for ipar=1:length(phatone), % добавляем параметры
    com=[com ',' sprintf('%d',phatone(ipar))];
  end
  com=[com ')']; % сформировали команду
  Fx=eval(com); % выполнили команду - вычислили F(x)
  [hkolm,pkolm,kskolm,cvkolm]=kstest(x,[x Fx],0.1,0);
  qq=[qq pkolm]; % критические уровни значимости
end
[maxqq,bdist]=max(qq); % выбрали лучшее распределение
fprintf(['Критерий согласия Колмогорова:\n',...
  'Лучше всего подходит %s распределение;\n'...
  'критический уровень значимости для него = %8.5f\n'], ...
  dlistr{bdist},maxqq);
figure % создаем новую фигуру
cdfplot(x); % эмпирическая функция распределения
phatone=phat{bdist}; % параметры наилучшего распределения
com=['cdf(''' dlist{bdist} ''',xpl']; % команда 
for ipar=1:length(phatone), % добавляем параметры
  com=[com ',' sprintf('%d',phatone(ipar))];
end
com=[com ')']; % сформировали команду
del=(xmax-xmin)/20; % добавки влево и вправо
xl=xmin-del;
xr=xmax+del; % границы интервала для построения графиков
xpl=linspace(xl,xr,1000); % абсциссы для графиков
Fxpl=eval(com); % вычислили F(x) для наилучшего распределения
hold on % для рисования на этом же графике
plot(xpl,Fxpl,'r'); % дорисовали F(x)
hold off
set(get(gcf,'CurrentAxes'),...
  'FontName','Times New Roman Cyr','FontSize',10)
title(['\bfПодобрано ' dlistr{bdist} ' распределение'])
xlabel('\itx') % метка оси x
ylabel('\itF\rm(\itx\rm)') % метка оси y
ab=[]; % статистики и критические значения
for idist=1:ndist, % критерий Пирсона
  phatone=phat{idist}; % значения параметров
  com=['chi2test(x'',n/10,0.1,''' dlist{idist} '''']; % команда 
  for ipar=1:length(phatone), % добавляем параметры
    com=[com ',' sprintf('%d',phatone(ipar))];
  end
  com=[com ')']; % сформировали команду
  [a1,b1]=eval(com); % выполнили команду - провели тест Пирсона
  ab=[ab;[a1 b1]]; % статистики и критические уровни значимости
end
[maxdab,bdistp]=max(diff(ab')'); % выбрали лучшее распределение