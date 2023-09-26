% -----------------------------------------------------------------------
% Program Number: HW 5 Part 1
% Program Purpose: Prompt three attempts for a passcode 
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

%prompt for password (loop) and validate
passcodeAttempt=1;
passcode=input('Please enter the passcode: ');
while (isempty(passcode) || passcode~=39) && passcodeAttempt<3
    passcode=input('\nACCESS DENIED. Try again: ');
    passcodeAttempt=passcodeAttempt+1;
end

if passcode==39
    fprintf('\nACCESS GRANTED');
else %passcodeAttempt incorrect
    fprintf('ACCESS DENIED. You have no more attempts.\n');
end




