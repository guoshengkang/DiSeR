clf;clear

% DCG vs. n
x=linspace(0,20,5);
y1=[0.04779088,0.11733624,0.12065032,0.11703348,0.11459132];
y2=[0.15625706,0.13415563,0.13815148,0.13619183,0.13618203];
y3=[0.13710398,0.14460792,0.12676268,0.16873219,0.17167496];
y4=[0.12917316,0.13790782,0.13720384,0.18143299,0.17018301];
y5=[0.1218952,0.10406753,0.1042408,0.06951199,0.06966539];
y6=[0.00547272,0.10205373,0.07139058,0.07821996,0.0614692];
Y=[y1;y2;y3;y4;y5;y6];
Y=Y';
subplot(1,3,1)
b=bar(Y,'group');
hold on;
set(b(1),'facecolor','y')
set(b(2),'facecolor','b')
set(b(3),'facecolor','c')
set(b(4),'facecolor','g')
set(b(5),'facecolor','m')
set(b(6),'facecolor','r')
grid on
xlabel('\fontname{Times New Roman}(a) RMSDE vs. |S|')
ylabel('\fontname{Times New Roman}RMSDE')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','\fontname{Times New Roman}DiSeR','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'1600','1800','2000','2200','2400'}); 
% DCG vs. d
x=4:8;
y1=[0.03986347,0.12980771,0.23732857,0.26517191,0.26696671];
y2=[0.15625706,0.10316911,0.08058668,0.03945793,0.03672543];
y3=[0.08909297,0.29119763,0.37458429,0.39198387,0.31603674];
y4=[0.13723825,0.2951396,0.38681143,0.41478356,0.40032297];
y5=[0.1218952,0.05584321,0.07879523,0.11133922,0.13121396];
y6=[0.00547272,0.04444325,0.02364881,0.05552593,0.04149351];
subplot(1,3,2)
Y=[y1;y2;y3;y4;y5;y6];
Y=Y';
b=bar(Y,'group');
hold on;
set(b(1),'facecolor','y')
set(b(2),'facecolor','b')
set(b(3),'facecolor','c')
set(b(4),'facecolor','g')
set(b(5),'facecolor','m')
set(b(6),'facecolor','r')
grid on
xlabel('\fontname{Times New Roman}(b) RMSDE vs. d')
ylabel('\fontname{Times New Roman}RMSDE')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','\fontname{Times New Roman}DiSeR','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'4','5','6','7','8'}); 
% DCG vs. k
x=3:8;
y1=[0.05755798,0.06102403,0.07687406,0.04635164,0.05001505];
y2=[0.16393177,0.16243645,0.15625706,0.14286836,0.13879179];
y3=[0.05449326,0.12660294,0.08776432,0.11471283,0.12746428];
y4=[0.11882721,0.1167197,0.11414708,0.07297104,0.09105996];
y5=[0.10092073,0.11350696,0.1218952,0.11604853,0.11959291];
y6=[0.08476915,0.07658439,0.00547272,0.03256226,0.0638108];
subplot(1,3,3)
Y=[y1;y2;y3;y4;y5;y6];
Y=Y';
b=bar(Y,'group');
hold on;
set(b(1),'facecolor','y')
set(b(2),'facecolor','b')
set(b(3),'facecolor','c')
set(b(4),'facecolor','g')
set(b(5),'facecolor','m')
set(b(6),'facecolor','r')
grid on
xlabel('\fontname{Times New Roman}(c) RMSDE vs. top-k')
ylabel('\fontname{Times New Roman}RMSDE')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','\fontname{Times New Roman}DiSeR','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'3','4','5','6','7'}); 