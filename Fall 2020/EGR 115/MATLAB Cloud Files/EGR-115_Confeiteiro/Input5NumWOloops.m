clc
clear
close all

% using str2num 
%input 5 positive numbers without a loop and 
N = input('Enter the 5 numbers: ','s');
N = str2num(N);
Nzero = any(mod(N,);
Nnonzero = all(N>0);
while length(N)>5 && Nzero~=1 || Nnonzero==1
    N = input('Error, please enter the numbers again: ','s');
    N = str2num(N);
end

fprintf('\nThe numbers you entered were: ');
for k = 1:length(N)
    fprintf('%d ',N(k));
end
fprintf('\n\n');
