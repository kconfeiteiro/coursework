% -----------------------------------------------------------------------
% Program Number: ICA6
% Program Purpose: Tell you whether a pH value is basic, neutral, or
% acidic.
%
% Created By: Krystian Confeiteiro
%
% Created On: 09/15/20
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


%Greetings prompt and display 
fprintf('***************Quadratic Root Finder ********************\n');
fprintf('                 ax^2 + bx + c = 0\n');


%Prompt for the coefficients
a = input('\nEnter the coefficient a: ');
b = input('Enter the coefficient b: ');
c = input('Enter the coefficient c: ');


%Calculate value inside square root
d =((b^2)-(4*a*c));

%Prompt for coefficiants if d >0, =0, or <0
if d>0 %2 roots
    r1 = (-b + sqrt(d))/(2*a);
    r2 = (-b - sqrt(d))/(2*a);
    fprintf('\nThe two roots are %.02f and %.02f. \n', r1, r2);
elseif d==0 %1 root
    r = -b/(2*a);
    fprintf('\nThe identical roots are %.02f. \n', r);
else %d<0, no real roots
    fprintf('\nThere are no real roots.\n');
end





















