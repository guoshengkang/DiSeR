clf;clear
% DCG vs. n
x=linspace(0,20,5);
y1=[2.31362254,2.45254264,2.41229828,2.33354251,2.32426206];
y2=[2.84267968,2.89751882,2.9042019,2.9024112,2.9024612];
y3=[2.23762074,2.45446435,2.45720151,2.26476292,2.39948726];
y4=[2.20952938,2.44973684,2.40778292,2.10606962,2.3141038];
y5=[2.75800193,2.71502587,2.71300852,2.69646087,2.69514964];
y6=[2.37023633,2.53748233,2.45604935,2.57514543,2.63064577];
subplot(1,3,1)
plot(x,y1,'-k*','LineWidth',1.5,'MarkerFaceColor','k','MarkerSize',10)
hold on
plot(x,y2,'-bs','LineWidth',1.5,'MarkerFaceColor','b','MarkerSize',10)
hold on
plot(x,y3,'-co','LineWidth',1.5,'MarkerFaceColor','c','MarkerSize',10)
hold on
plot(x,y4,'-gd','LineWidth',1.5,'MarkerFaceColor','g','MarkerSize',10)
hold on
plot(x,y5,'-m^','LineWidth',1.5,'MarkerFaceColor','m','MarkerSize',10)
hold on
plot(x,y6,'-rp','LineWidth',1.5,'MarkerFaceColor','r','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(a) DCG Value vs. |S|')
ylabel('\fontname{Times New Roman}DCG Value')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','\fontname{Times New Roman}DiSeR','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'1600','1800','2000','2200','2400'}); 
% DCG vs. d
x=4:8;
y1=[2.34136426,2.29324925,1.99864921,1.89553118,1.87077429];
y2=[2.84267968,2.86394273,2.81254064,2.71575459,2.74326307];
y3=[2.24973307,2.08224185,1.89725967,1.7601256,1.89291368];
y4=[2.17368123,2.12435022,1.88764336,1.66903852,1.74340324];
y5=[2.75800193,2.65294846,2.47943564,2.38056406,2.39255485];
y6=[2.37023633,2.69651526,2.66774204,2.53685477,2.59981569];
subplot(1,3,2)
plot(x,y1,'-k*','LineWidth',1.5,'MarkerFaceColor','k','MarkerSize',10)
hold on
plot(x,y2,'-bs','LineWidth',1.5,'MarkerFaceColor','b','MarkerSize',10)
hold on
plot(x,y3,'-co','LineWidth',1.5,'MarkerFaceColor','c','MarkerSize',10)
hold on
plot(x,y4,'-gd','LineWidth',1.5,'MarkerFaceColor','g','MarkerSize',10)
hold on
plot(x,y5,'-m^','LineWidth',1.5,'MarkerFaceColor','m','MarkerSize',10)
hold on
plot(x,y6,'-rp','LineWidth',1.5,'MarkerFaceColor','r','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(b) DCG Value vs. d')
ylabel('\fontname{Times New Roman}DCG Value')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','\fontname{Times New Roman}DiSeR','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'4','5','6','7','8'}); 
% DCG vs. k
x=3:7;
y1=[1.68604569,2.05031908,2.31218235,2.61368947,2.80270888];
y2=[2.06868274,2.48045912,2.84267968,3.15639056,3.44918183];
y3=[1.68910949,1.92075219,2.34784593,2.53699613,2.72247524];
y4=[1.69782925,1.97259216,2.19853083,2.57258605,2.77681218];
y5=[1.97421898,2.3881261,2.75800193,3.06999299,3.38100909];
y6=[1.85932139,2.1853557,2.37023633,2.69460338,2.90910699];
subplot(1,3,3)
plot(x,y1,'-k*','LineWidth',1.5,'MarkerFaceColor','k','MarkerSize',10)
hold on
plot(x,y2,'-bs','LineWidth',1.5,'MarkerFaceColor','b','MarkerSize',10)
hold on
plot(x,y3,'-co','LineWidth',1.5,'MarkerFaceColor','c','MarkerSize',10)
hold on
plot(x,y4,'-gd','LineWidth',1.5,'MarkerFaceColor','g','MarkerSize',10)
hold on
plot(x,y5,'-m^','LineWidth',1.5,'MarkerFaceColor','m','MarkerSize',10)
hold on
plot(x,y6,'-rp','LineWidth',1.5,'MarkerFaceColor','r','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(c) DCG Value vs. top-k')
ylabel('\fontname{Times New Roman}DCG Value')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','\fontname{Times New Roman}DiSeR','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'3','4','5','6','7'}); 