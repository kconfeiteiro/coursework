% -----------------------------------------------------------------------
% Program Number: HW 7 NUM 3
% Program Purpose: Calculate the Fib sequence for a user given interval

% Created By: Krystian Confeiteiro 
% Created On: 10/12/20
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

%opening message
fprintf('\nComputing values in the Fibonacci Sequence.\nPlease provide the range of the indices to be displayed.\n\n');

%input for start and end of range
n = input('Enter the first integer: '); %first integer
while isempty(n) || mod(n,1)~=0
   n = input('\n\nError, please re-enter the first integer: '); 
end

fprintf('Enter the seond integer higher than %d: ',n);
m = input('');
while isempty(m) || mod(m,1)~=0
    fprintf('Error, your second integer must be higher than %d: ',n);
    m = input('');
end

%title of array
fprintf('\n\nSequence Location\t\tFibonacci Value');
fprintf('\n-----------------              ----------------\n');

%calculate and display the sequence 
fib = [0,1];
for k=3:m
    fib(k)=fib(k-1)+fib(k-2);
end


for k = n:m
  fprintf('\t%d\t\t\t%d ',k,fib(k))
  if isprime(fib(k))
      fprintf('(prime)');
  end
  fprintf('\n');    
end