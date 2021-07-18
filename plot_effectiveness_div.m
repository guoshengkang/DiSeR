clf;clear
% DCG vs. n
x=linspace(0,20,5);
y1=[0.21194912,0.19158352,0.2094175,0.22977357,0.22953479];
y2=[0.03625638,0.0206474,0.01692383,0.01705312,0.01709296];
y3=[0.29199984,0.22723792,0.21570304,0.254704,0.22421325];
y4=[0.2841235,0.21806386,0.23804087,0.28920259,0.24593586];
y5=[0.07516367,0.09990937,0.09902192,0.10553582,0.10581745];
y6=[0.1945413,0.15105552,0.10924673,0.18702012,0.14217918];
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
xlabel('\fontname{Times New Roman}(a) Diversity vs. |S|')
ylabel('\fontname{Times New Roman}Diversity')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','\fontname{Times New Roman}DiSeR','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'1600','1800','2000','2200','2400'}); 
% DCG vs. d
x=4:8;
y1=[0.20428472,0.25162893,0.34951138,0.36711671,0.36266908];
y2=[0.03625638,0.02767379,0.04572904,0.09348967,0.07905116];
y3=[0.25807479,0.39148218,0.48042991,0.48905079,0.40991439];
y4=[0.293745,0.40085412,0.48855263,0.51215164,0.49375847];
y5=[0.07516367,0.11686508,0.18192977,0.20190252,0.20802267];
y6=[0.1945413,0.09604033,0.11278902,0.13073098,0.11093915];
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
xlabel('\fontname{Times New Roman}(b) Diversity vs. d')
ylabel('\fontname{Times New Roman}Diversity')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','\fontname{Times New Roman}DiSeR','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'4','5','6','7','8'}); 
% DCG vs. k
x=3:7;
y1=[0.2384073,0.22004441,0.24368588,0.21437911,0.23137407];
y2=[0.02852208,0.02993653,0.03625638,0.05410068,0.06149732];
y3=[0.22137456,0.28608092,0.25698791,0.27142213,0.28793973];
y4=[0.26012733,0.28073755,0.28224182,0.2416688,0.25604957];
y5=[0.10314476,0.08622779,0.07516367,0.08833679,0.08290572];
y6=[0.1179194,0.16537957,0.1945413,0.20858321,0.23071714];
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
xlabel('\fontname{Times New Roman}(c) Diversity vs. top-k')
ylabel('\fontname{Times New Roman}Diversity')
legend('\fontname{Times New Roman}DSL-RS','\fontname{Times New Roman}DSL-KNN','\fontname{Times New Roman}DQCSR-CC','\fontname{Times New Roman}DQCSR-CR','\fontname{Times New Roman}DiQoS','\fontname{Times New Roman}DiSeR','Location', 'Best')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'3','4','5','6','7'}); 