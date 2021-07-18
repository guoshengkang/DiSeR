clf;clear
% DCG vs. n_top
x=linspace(0,20,5);
y1=[2.33545509,2.35047883,2.27143582,2.27680940,2.25067934];
subplot(2,3,1)
plot(x,y1,'-.bp','LineWidth',1.5,'MarkerFaceColor','b','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(a) DCG Value vs. n')
ylabel('\fontname{Times New Roman}DCG Value')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'2','2.5','3','3.5','4'}); 
% Div vs. n_top
x=4:8;
y1=[0.09278210,0.08646100,0.14579124,0.11321022,0.14343380];
subplot(2,3,2)
plot(x,y1,'-.bp','LineWidth',1.5,'MarkerFaceColor','b','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(b) Diversity vs. n')
ylabel('\fontname{Times New Roman}Diversity')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'2','2.5','3','3.5','4'}); 
% RMSDE vs. n_top
x=3:7;
y1=[0.10854028,0.11136154,0.14414500,0.10110114,0.13508945];
subplot(2,3,3)
plot(x,y1,'-.bp','LineWidth',1.5,'MarkerFaceColor','b','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(c) RMSDE vs. n')
ylabel('\fontname{Times New Roman}RMSDE')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'2','2.5','3','3.5','4'}); 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% DCG vs. lamda
x=linspace(0,20,5);
y1=[2.30166897,2.27143582,2.26322653,2.26473036,2.24757221];
subplot(2,3,4)
plot(x,y1,'-rp','LineWidth',1.5,'MarkerFaceColor','r','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(d) DCG Value vs. \it\lambda')
ylabel('\fontname{Times New Roman}DCG Value')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'0.5','0.6','0.7','0.8','0.9'}); 
% Div vs. lamda
x=4:8;
y1=[0.10673971,0.14579124,0.14611285,0.14329819,0.14414844];
subplot(2,3,5)
plot(x,y1,'-rp','LineWidth',1.5,'MarkerFaceColor','r','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(e) Diversity vs. \it\lambda')
ylabel('\fontname{Times New Roman}Diversity')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'0.5','0.6','0.7','0.8','0.9'}); 
% RMSDE vs. lamda
x=3:7;
y1=[0.09099887,0.14414500,0.14726306,0.15017605,0.15201132];
subplot(2,3,6)
plot(x,y1,'-rp','LineWidth',1.5,'MarkerFaceColor','r','MarkerSize',10)
grid on
xlabel('\fontname{Times New Roman}(f) RMSDE vs. \it\lambda')
ylabel('\fontname{Times New Roman}RMSDE')
set(gca,'looseInset',[0,25,0,5])
set(gca, 'XTicklabel',{'0.5','0.6','0.7','0.8','0.9'}); 

