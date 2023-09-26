% -----------------------------------------------------------------------
% Program Number: HW 10 Part 2
% Program Purpose: Create a sine and cosine subplot

% Created By:  Krystian Confeiteiro
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



%create the first subplot 
theta = linspace(0,2*pi,50);
subplot(2,1,1);
plot(theta,sin(theta),'bo-');
set(gca, 'XTick', 0:pi/2:2*pi);
set(gca, 'XTickLabel', {'0','\pi/2','\pi','3\pi/2','2\pi'});
xlabel('Theta (\theta)');
ylabel('sin(\theta)');
grid on

%creat the second plot/subplot
subplot(2,1,2);
plot(theta,cos(theta),'mv-');
set(gca, 'XTick', 0:pi/2:2*pi);
set(gca, 'XTickLabel', {'0','\pi/2','\pi','3\pi/2','2\pi'});
xlabel('Theta (\theta)');
ylabel('cos(\theta)');
grid on