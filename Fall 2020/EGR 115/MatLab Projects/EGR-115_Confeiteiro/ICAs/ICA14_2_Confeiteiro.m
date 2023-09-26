% -----------------------------------------------------------------------
% Program Number: ICA 14 Part 2
% Program Purpose: Rock

% Created By:
% Created On:
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

%welcome message
fprintf('Welcome to Rock-Papers-Sciccors!\n********************************\n');

%start the game and input rock(1), papers(2), or scissors(3) in a LOOP
moreYN = 'y';
while moreYN ~= 'n'
    %input the users choice for the game
    userChoice = input('\nTo play, choose rock(1), paper(2), or scissors(3): ');
    while isempty(userChoice) || userChoice>3 
        userChoice = input('\nError. Please choose rock(1), paper(2), or scissors(3): ');
    end
    
    %computers random choice
    computerChoice = randi(3);
    
    %first function call
    [rps] = rpsChoice(userChoice); %users choice 
    [rpsComputer] = rpsChoice(computerChoice); %computers choice
    
    %second function call
    [rpsW] = rpsWinner(userChoice,computerChoice); %find the winner
    
    %output winner 
    fprintf('\nYou chose %s, the computer chose %s. ',rps,rpsComputer);
    if rpsW == 1 %user wins
        fprintf('You win!');
    elseif rpsW == 2 %computer wins
        fprintf('You lost. Try again.');
    else  %game is draw
        fprintf('The game was a draw!');
    end
          
    %input to replay the game
    moreYN = input('\nDo you want to play again? (y/n): ','s');
    if moreYN == 'n' %end of loop
        fprintf('\n\nThanks for playing!\n\n');
    end
end

