%~~~~~~MAIN PROGRAM~~~~~~~~~~ 

%PTOMT FOR seconds; validate
seconds = input('Enter the amount of seconds you would like to convert: ');
while isempty(seconds) || mod(seconds,1)~=0 || seconds<500
    seconds = input('\nError, please enter the seconds: ');
end

%call function 
[h,m,s]=sec2hms(seconds);

%output the result
fprintf('%d seconds is %d hours %d seconds %d minutes.\n\n',seconds,h,m,s);