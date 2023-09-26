% -----------------------------------------------------------------------
% Program Number: ICA 14 Part 1
% Program Purpose: Calculate the circumference of an ellipse
%
% Created By: Krystian Confeiteiro 
% Created On: 10/20/20
% Last Modified On: ~
%
% Credit To: 
% By submitting this program with my name, I affirm that the creation and 
% modifications of this program is primarily my own work.
%
% Comments:
% -----------------------------------------------------------------------

clc
clear 
close all

%input the major and minor axis and validate
a = input('Enter the major axis of the ellipse: '); %major axis
while isempty(a) || a<0
    a = input('\nError, please re-enter the major axis of the ellipse: ');
end

b = input('Enter the minor axis of the ellipse: ');
while isempty(b) || a<b || b<0
    b = input('\nError, please re-enter the minor axis of the ellipse: ');
end

%input what units the user wants
units = input('\nWhat are your units of choice?: ','s');

%call function 
[circumference,area] = ovalCal(a,b);

%output circumference and the units 
fprintf('The area of the ellipse is %.01f %s^2 and the circumference is %.01f %s.\n\n',area,units,circumference,units);
