function [rpsW] = rpsWinner(userChoice,computerChoice)
% Purpose: Determine the winner of the rock-papers-scissors game
% syntax: [rpsW] = rpsWinner(userChoice,computerChoice)
%
% Input variables:
% userChoice: what the user chooses (1,2,3)
% computerChoice: the random number the computer generates
%
% Output variables:
% rpsW: the winner of the game
%
% Created By: Krystian Confeiteiro
% Section #: 10
% Created On: 10/20/20
% Last Modified On: ~
%
% Credit to: the Smart Dude
% By submitting this program with my name, I affirm that the creation and
% modification of this program is primarily my own work.
% Comments:
% -------------------------------------------
% NO clear;clc;close all

%if statement
if userChoice==computerChoice
    rpsW = 0; %tie
elseif userChoice==1 && computerChoice==2 || userChoice==3 && computerChoice==1 || userChoice==2 && computerChoice==3
    rpsW = 2; %computer wins
elseif userChoice==3 && computerChoice==2 || userChoice==2 && computerChoice==1 || userChoice==1 && computerChoice==3
    rpsW = 1; %user wins
end
end
