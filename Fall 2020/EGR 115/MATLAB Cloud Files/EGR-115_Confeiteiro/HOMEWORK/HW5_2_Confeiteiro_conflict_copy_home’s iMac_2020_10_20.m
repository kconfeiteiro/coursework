% -----------------------------------------------------------------------
% Program Number: HW 5 Part 2
% Program Purpose: Countdown clock for user input
%
% Created By: Krystian Confeiteiro 
%
% Created On: 09/24/20
% Last Modified On: 09/28/20
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

%prompt user for amount of minutes, validate
timer=input('Enter start time in minutes (value>=1): ');
fprintf('\n%02d:00\n',timer); %show intial time
while isempty(timer) || timer<1 && mod(timer,1)==0 %validate
    timer=input('\nAn invalid time was entered. \nPlease enter a start time (min): ');
end

for countdownMinutes=timer-1:-1:0 %minutes
    for countdownSeconds = 59:-1:0 %seconds
        fprintf('%02d:%02d\n', countdownMinutes, countdownSeconds); %output countdown
        pause(1); 
    end        
end
