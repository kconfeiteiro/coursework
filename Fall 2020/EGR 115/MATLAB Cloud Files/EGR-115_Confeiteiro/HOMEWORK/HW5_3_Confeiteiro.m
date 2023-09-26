% -----------------------------------------------------------------------
% Program Number: HW 5 Part 3
% Program Purpose: Contain the square roots of values lying between two
% intergers
%
% Created By: Krystian Confeiteiro 
%
% Created On:  09/24/20
% Last Modified On: 09/27/20
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

%prompt for first two intergers and validate
int1=input('Enter the first (positive) interger: ');
while isempty(int1) || mod(int1,1)~=0
    int1=input('Error. Please enter a positive interger: ');
end

fprintf('Enter the second (positive) interger greater than %d: ',int1);
int2=input('');
while isempty(int2) || mod(int2,1)~=0 || int2<=int1
    int2=input('Error. Please enter a positive interger: ');
end

%-------------------------------------------------------------------------------------------------------------
fprintf('\n\t0.0000\t0.1000\t0.2000\t0.3000\t0.4000\t0.5000\t0.6000\t0.7000\t0.8000\t0.9000\n');
fprintf('\t----------------------------------------------------------------------------------\n');
%-------------------------------------------------------------------------------------------------------------

%calculate square roots 
for integer=int1:1:int2 %intergers
    fprintf('%2d\t',integer)
    for decimal=0:0.1:0.9 %decimals
        number = integer+decimal;
        fprintf('%.04f\t ',sqrt(number));   %print sqrt(number)
    end  
    fprintf('\n');
end





