% -----------------------------------------------------------------------
% Program Number: HW 5 Part 1
% Program Purpose: Prompt three attempts for a passcode 
% Created By: Krystian Confeiteiro 
%
% Created On: 09/24/20
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

passcode=39;
%prompt for password (loop) and validate
passcodeAttempt = input('Please enter the password: ');
count=3;
while (isempty(passcodeAttempt) || passcodeAttempt~=passcode) && count<3
    passcodeAttempt = input('Wrong password. Try again: ');
    
    count=count-1;
end





