% -----------------------------------------------------------------------
% Program Number: HW 10 Part 3
% Program Purpose: Create the Batman symbol!!

% Created By:  Krytian Confeiteiro 
% Created On:  11/09/20
% Last Modified On: 11/09/20

% Credit To: 
% By submitting this program with my name, I affirm that the creation and 
% modifications of this program is primarily my own work.
%
% Comments:
% -----------------------------------------------------------------------

clc
clear 
close all

%left wing 
x1 = linspace(-7,-3,50);
y1 = ((3*sqrt((x1+7).*(7-x1)))/7);
plot(x1,y1,'r');
hold on
grid on 

x2 = linspace(-7,-4,50);
y2 = ((-3*sqrt((x2+7).*(7-x2)))/7);
plot(x2,y2,'r');

%graph parameters
set(gca,'XLim',[-7,7],'YLim',[-5,5],'XTick',-7:7,'YTick',-5:5);

%right wing
x3 = linspace(3,7,50);
y3 = ((3*sqrt((x3+7).*(7-x3)))/7);
plot(x3,y3,'r');
hold on

x4 = linspace(4,7,50);
y4 = ((-3*sqrt((x4+7).*(7-x4)))/7);
plot(x4,y4,'r');

%bottom curve
x5 = linspace(-4,4,50);
y5 = (abs(x5/2)-(((3*sqrt(33)-7)/112)*x5.^2)-3+(sqrt(1-(abs(abs(x5)-2)-1).^2)));
plot(x5,y5,'m');

%left shoulder  
x6 = linspace(-3,-1,50);
y6 = ((6*sqrt(10)/7)+1.5-0.5*abs(x6)-(6*sqrt(10)/14)*sqrt(4-(abs(x6)-1).^2));
plot(x6,y6,'b');


%right shoulder
x7 = linspace(1,3,50);
y7 = ((6*sqrt(10)/7)+1.5-0.5*abs(x7)-(6*sqrt(10)/14)*sqrt(4-(abs(x7)-1).^2));
plot(x7,y7,'b');

%head
plot([-1,-0.75],[1,3],'g'); %left side of head
plot([1,0.75],[1,3],'g'); %right side of head
plot([-0.75,-0.5],[3,2.5],'g'); %left inside of ear
plot([0.75,0.5],[3,2.5],'g'); %right inside of ear
plot([-0.5,0.5],[2.5,2.5],'g'); %left inside of ear

title('BATMAN','FontSize',20);





