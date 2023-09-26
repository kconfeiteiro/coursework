% -----------------------------------------------------------------------
% Program Number: HW 5 Part 2
% Program Purpose: Countdown clock for user input
% Created By: Krystian Confeiteiro 
%
% Created On: 09/24/20
% Last Modified On:~
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
timerStart=input('Enter start time in minutes (value>=1): ');
for countdownMinutes=timerStart:1:0 %minutes
    while isempty(timerStart) || timerStart>=1 || mod(timerStart,1)
        timerStart=input('\nAn invalid time was entered. \nPlease enter a start time (min): ');
    end
end

for countdownSeconds=59:1:0
    
