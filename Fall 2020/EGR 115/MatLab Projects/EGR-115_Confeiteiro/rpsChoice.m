function [rps] = rpsChoice(rpsI)
% Purpose: convert a numeric value into a string for rock-papers-scissors
% game
%
% syntax: [rps] = rpsChoice(r
% Input variables:
% rpsI: what the user is inputting (1, 2, or 3)
%
% Output variables:
% rps: 'rock', 'papers', or 'scissors'
%
% Created By: Krystian Confeiteiro
% Section #: 10
% Created On: 10/20/20
% Last Modified On:
%
% Credit to: the Smart Dude
% By submitting this program with my name, I affirm that the creation and
% modification of this program is primarily my own work.
% Comments:
% -------------------------------------------
% NO clear;clc;close all

if rpsI == 1 %rock
    rps = 'rock';
elseif rpsI == 2 %papers
    rps = 'papers';
else %scissors
    rps = 'scissors';
end

end