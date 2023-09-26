% -----------------------------------------------------------------------
% Program Number: HW 8 Part 2
% Program Purpose: Find how many times it takes the program to get a
% fullhouse and output it.
%
% Created By: Krystian Confeiteiro
% Created On: 10/19/20
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


%repeat rolling dice until full house
fullhouse = 0; %not fullhouse
fullhouseCount = 0;
while fullhouse==0
    diceR = randi(6,1,5); %roll 5 6-sided dice
    for k = 1:6
        count(k) = sum(diceR==k);
    end
    
    fullhouseFind1 = find(count==2);
    fullhouseFind2= find(count==3);
    if ~isempty(fullhouseFind1) & ~isempty(fullhouseFind2)  %full house
        %is there a 2 and a 3 in the count?
        fullhouse = 1;
    end
    fullhouseCount=fullhouseCount+1;
end

%output # times to get a fullhouse
fprintf('\nThe program had to run %d times to get a fullhouse.\n\n',fullhouseCount);




