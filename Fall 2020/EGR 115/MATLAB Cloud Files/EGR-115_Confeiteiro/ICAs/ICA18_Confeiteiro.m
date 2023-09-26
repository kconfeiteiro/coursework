% -----------------------------------------------------------------------
% Program Number: ICA 18
% Program Purpose: Print emojis 

% Created By:  Krystian Confeiteiro & Dominic 
% Created On: 11/05/20
% Last Modified On: ~

% Credit To: 
% By submitting this program with my name, I affirm that the creation and 
% modifications of this program is primarily my own work.
%
% Comments:
% -----------------------------------------------------------------------

clc
clear 
close all

%draw head 
theta = linspace(0,2*pi,50);
x = 0+7*cos(theta);
y = 7*sin(theta);
fill(x,y,'y');
hold on
    
%draw eyes 
eye1x = -3+1.5*cos(theta);
eye1y = 3+1.5*sin(theta);
fill(eye1x, eye1y,'w');

eye2x = 3+1.5*cos(theta);
eye2y = 3+1.5*sin(theta);
fill(eye2x,eye2y,'w');

hold on

%pupils
pupil1x = -3+0.75*cos(theta);
pupil1y = 3+0.75*sin(theta);
pupil2x = 2.5+0.75*cos(theta);
pupil2y = 2.5+0.75*sin(theta);
fill(pupil1x, pupil1y,'k');
fill(pupil2x, pupil2y,'k');
hold on

%draw mustache
mustache1 = linspace(-2*pi,2*pi,50);
d = 1/2*sin(mustache1);
plot(mustache1,d,'lineWidth',2);
hold on

%draw red nose
rNoseX = 0+0.75*cos(theta);
rNoseY = 1+0.75*sin(theta);
fill(rNoseX,rNoseY,'r');
hold on

%draw mouth
mouthx = 0+5*cos(theta);
mouthy = -3+2*sin(theta);
fill(mouthx, mouthy, 'k');
hold on

%angry eyebrows
eyebrow1 = linspace(-pi,pi,50);
eyebX = abs(eyebrow1)+0;
eyebY = abs(eyebrow1)+4;
plot(eyebX,eyebY,'lineWidth',4,'color', 'k');
hold on

eyebrow2 = linspace(-pi,pi,50);
eyeb2X = -abs(eyebrow1)+0;
eyeb2Y = abs(eyebrow1)+4;
plot(eyeb2X,eyeb2Y,'lineWidth',4,'color','k');
hold on



