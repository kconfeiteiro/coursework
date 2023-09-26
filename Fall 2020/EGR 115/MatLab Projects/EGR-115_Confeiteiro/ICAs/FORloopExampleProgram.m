%lab 8 practice
%looking for and counting twin primes

clc
clear 
close all

count=0;
fprintf('The twin primes are: \n\n');
%looping throuh all numbers 1:198, this is num1
for num1 = 1:198
    %num2 is 2 more than num1
    num2 = num1+2;
    %check if both are primes; isprime()
    if isprime(num1) && isprime(num2)
        %if yes, print num1 and num2; count+1
        fprintf('%5d\t%5d\n', num1, num2);
        count=count+1;
    end
end
%print count
