function [plotThis] = hangmanPlotting(wrongGuessCount)
%HANGMANPLOTTING Summary of this function goes here
% Detailed explanation goes here:
%   I am coding a hangman game for my final project and I am making this
%   function to make the coding more efficient and simplify the program.
%
% Purpose: Get a number (number of guesses) and return a part of the
% hangman character until it is completed
%
% syntax: [plotThis] = hangmanPlotting(wrongGuessCount)
% Input variables:
% wrongGuessCount: The count of the guesses that the user has done
%
% Output variables:
% plotThis: Plot the part of the hangman
%
% Created By: Krystian Confeiteiro
% Section #: 10
% Created On: 11/19/20
% Last Modified On: 11/20/20
%
% Credit to: the Smart Dude
% By submitting this program with my name, I affirm that the creation and
% modification of this program is primarily my own work.
% Comments:
% -------------------------------------------

if wrongGuessCount == 1
    lVX = [2 2]; %large vertical pole X
    lVY = [8 0]; %large vertical pole Y
    hpX = [1 2.5]; %large horizontal pole X
    hpY = [8 8]; %large horizonal pole Y
    svpX = [1 1]; %small vertical pole X
    svpY = [6 8]; %small vertical pole Y
    plotThis = plot(lVX,lVY,hpX,hpY,svpX,svpY,'color', 'k','lineWidth', 3); %large vertical pole
elseif wrongGuessCount == 2
    %draw head
    theta = linspace(-2*pi,2*pi,50);
    headX = 1+0.18*cos(theta);
    headY = 5.5+0.5*sin(theta);
    plotThis = plot(headX, headY,'color','k','lineWidth',4); %head
elseif wrongGuessCount == 3
    %draw body
    bodyX = [1 1];
    bodyY = [5 3];
    plotThis = plot(bodyX,bodyY,'color','k','lineWidth',3); %body
elseif wrongGuessCount == 4
    %draw left leg
    leftLegX = [0.75 1];
    leftLegY = [2 3];
    plotThis = plot(leftLegX,leftLegY,'color','k','lineWidth',3); %left leg
elseif wrongGuessCount == 5
    %draw right leg
    rightLegX = [1 1.25];
    rightLegY = [3 2];
    plotThis = plot(rightLegX,rightLegY,'color','k','lineWidth',3); %right leg
elseif wrongGuessCount == 6
    %draw left arm
    leftArmX = [0.75 1];
    leftArmY = [3.5 4.4];
    plotThis = plot(leftArmX,leftArmY,'color','k','lineWidth',3); %left arm
else %wrongGuessCount == 7
    %draw right arm
    rightArmX = [1 1.25];
    rightArmY = [4.4 3.5];
    plotThis = plot(rightArmX,rightArmY,'color','k','lineWidth',3); %right arm
end
end

