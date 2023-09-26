% -----------------------------------------------------------------------
% Program Number: Final Project, FINAL DRAFT
%
% Program Purpose: Hangman game that tells them the rules, asks if they
% want to play against a computer or a friend, completes the game then
% asks if they want to play again, and lastly prints the final message if
% they are done or takes them back to play again.
%
% Created By: Krystian Confeiteiro
% Created On: 10/22/20
% Last Modified On: 12/05/20
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

%loop until user wants to stop
moreOrNo = 'y';
while ~strncmpi(moreOrNo,'no',1)
    clc
    %welcome prompt and rules
    fprintf('--------------------------------------------------------------------------------------------------------------\n');
    fprintf('\t\t\t\t\t* ------------------- *\n\t\t\t\t\t* Welcome to Hangman! *\n\t\t\t\t\t* ------------------- *\n');
    fprintf('\nFun fact: The TV show "Wheel of Fortune" is based of off Hangman, it uses a roulette-style wheel that players \n          spin for cash & prizes!'); 
    fprintf('\n\n\t\t\t\t\t\tRULES: \n\t\t\t\t\t     |+~~~~~~~+| \n\n1.) Choose to play against the computer or a friend. If you are playing against a friend, enter a word to guess! \n2.) Guess a letter. If you are correct, keep guessing. ');
    fprintf('If guess incorrectly, a part of the hangman will be added until \n    it is complete! If you guess the word or all the letters before your attempts run out, you win!.');
    fprintf('\n\nPress any key to continue...');
    fprintf('\n--------------------------------------------------------------------------------------------------------------\n\n');
    pause();
    clc
    
    %print classic game loading screen then clear screen!
    fprintf('Your game is loading');pause(0.2);fprintf('.');pause(0.2);fprintf('.');pause(0.2);fprintf('.');
    fprintf('\nYour game is loading');pause(0.2);fprintf('.');pause(0.2);fprintf('.');pause(0.2);fprintf('.');
    fprintf('\nYour game is loading');pause(0.2);fprintf('.');pause(0.2);fprintf('.');pause(0.2);fprintf('.');
       
    clc
        
    %input to play against the computer or another person, validate
    %random list of words and choose random word
    [~,~,hangmanWords] = xlsread('HangmanWords.xlsx'); %<SM:READ>
    
    %ask if they want to use random guess or input their own word (+validation)
    fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
    fprintf('\t\t\t\t* ------------------- *\n\t\t\t\t* Welcome to Hangman! *\n\t\t\t\t* ------------------- *\n');
    fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
    playerType = input('\nDo you want a randomly generated word or use your own word of choice?\nEnter ''computer'' for a computer generated word or ''player'' for your own word: ','s');
    while (~strcmpi(playerType, 'computer') && ~strcmpi(playerType, 'player')) %<SM:BOP> %<SM:WHILE>
        playerType = input('\nERROR, Enter ''computer'' for a computer generated word or ''player'' to enter your word of choice: ','s');
    end
    clc
    
    %play vs computer or use a word of choice
    if strcmpi(playerType, 'computer') %<SM:IF> %<SM:STRING> %rand computer word
        wordGuess = hangmanWords{randi(10),randi(4)}; %<SM:RANDGEN> %<SM:RANDUSE> %<SM:REF>
        wordGuess = lower(wordGuess);
        for j=1:length(wordGuess)  %<SM:FOR> %converts words to dashes
            correctLetters(j)= '-'; 
        end
        
    elseif strcmpi(playerType, 'player') %user's word of choice
        fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        fprintf('\t\t\t\t* ------------------- *\n\t\t\t\t* Welcome to Hangman! *\n\t\t\t\t* ------------------- *\n');
        fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        
        %input word of choice and validate and convert to lowercase
        wordGuess = input('Enter your word of choice: ','s');
        wordGuess = lower(wordGuess);
        while isempty(wordGuess) || min(isletter(wordGuess))==0 %<SM:NEST> %validation
            wordGuess = char(input('Error, please enter a word to start the game!: ','s'));
            wordGuess = lower(wordGuess);
        end
        clc
        %replace the letters of the word with dashes
        for k = 1:length(wordGuess)
            correctLetters(k) = '-';
        end
    end
    
    %print header again
    fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
    fprintf('\t\t\t\t* ------------------- *\n\t\t\t\t* Welcome to Hangman! *\n\t\t\t\t* ------------------- *\n');
    fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
    clc
    
    %print box to start the game
    %draw handman pole/noose (this will be printed first)
    box_X = [0 3 0 0 0 3 3 3];
    box_Y = [0 0 0 10 10 10 0 10];
    plot(box_X,box_Y,'color','k','lineWidth',4); %<SM:PLOT>
    hold on
    
    %prompt for guesss, validate and crosscheck with word
    wrongGuessCount = 0;
    wrongGuesses = [''];  
    while  wrongGuessCount<7 && contains(correctLetters,'-')  %repeat while the count<7 and the word is complete
        clc
        %print header again
        fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        fprintf('\t\t\t\t* ------------------- *\n\t\t\t\t* Welcome to Hangman! *\n\t\t\t\t* ------------------- *\n');
        fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        
        %print dashes to begin guessing
        fprintf('\n\nWORD: ');
        fprintf('%s\t',correctLetters);
        fprintf('\n');
        
        %prompt for guess, validate, crosscheck with word
        guessU = input('Guess a letter: ','s'); %prompt guesses & validate
        while isempty(guessU) || length(guessU)>1 || min(isletter(guessU))==0
            guessU = input('\nError, guess a letter: ','s');
        end
        
        %crosscheck the guess
        if ~isempty(strfind(wordGuess,guessU)) %if it matches
            %say # of letters in the word and # of guesses left
            if length(strfind(wordGuess,guessU))>1 %print for multiple letters (plural)
                fprintf('\nThere where %d ''%s''s in the word!\n',count(wordGuess,guessU),guessU);
            else %print for a single letter (singular)
                fprintf('\nThere was 1 ''%s'' in the word!...\n',guessU);
            end
            
            %print the correct guesses and the rest of the dashes
            lettersFound = strfind(wordGuess,guessU);
            correctLetters(lettersFound) = guessU;
            fprintf('\nWORD: %s ',correctLetters);
            
        else %else (does not match)
            %say 0 letters in the word and # of guesses left
            fprintf('\nThere where 0 %s''s in the word...\n', guessU);
            
            %add the wrong guess to the wrong guesses list and print them
            wrongGuesses(end+1) = guessU; %<SM:AUG> 
            fprintf('Wrong guesses: ');
            for j = 1:length(wrongGuesses)
                fprintf('%s - ',wrongGuesses(j));
            end
            
            %count the number of guesses
            wrongGuessCount = wrongGuessCount+1; %<SM:PDF_PARAM> %<SM:RTOTAL>
            
            %call function to "build" the hangman after each wrong guess
            [plotThis] = hangmanPlotting(wrongGuessCount); %<SM:PDF_RETURN> %<SM:PDF_CALL>
        end
        
        %allow the user to see their guess, if correct/incorrect
        fprintf('\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        fprintf('\nPress any key to continue...');
        pause();
    end
    
    %print final staments if win or lose
    if ~contains(correctLetters,'-') %count<7 & word matches
        clc
        fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        fprintf('\nYOU WON!! \n-\nCongratulations, well played! \n\nPress any key to continue...');
        fprintf('\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        pause();
    elseif wrongGuessCount==8 && contains(correctLetters,'-') %count=7 and word does not match
        clc
        fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        fprintf('\nYOU LOSE... Try again. \n-\n-\nPress any key to continue...');
        fprintf('\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        pause();
    end
    clc
    
    %ask if the user wants to play again after the game ends +validate
    fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
    fprintf('\t\t\t\t* ------------------- *\n\t\t\t\t* Welcome to Hangman! *\n\t\t\t\t* ------------------- *\n');
    fprintf('\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ');
    moreOrNo = input('\nDo you want to play again? Enter ''yes'' to play again or ''no'' to end the game!: ','s');
    while isempty(moreOrNo) || (~strncmpi(moreOrNo,'yes',1) && ~strncmpi(moreOrNo,'no',1)) || min(isletter(moreOrNo))==0
        moreOrNo = input('Error, do you want to play again? Enter ''yes'' to play again or ''no'' to end the game!: ','s');
    end
    fprintf('\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
    
    %print the end message if they are done!
    if strncmpi(moreOrNo,'no',1)
        clc
        fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        fprintf('\t\t\t\t* ------------------- *\n\t\t\t\t* Welcome to Hangman! *\n\t\t\t\t* ------------------- *\n');
        fprintf('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n');
        fprintf('\nThank you for playing! I hope you enjoyed your game!\n\n');
    end
    clf %clears the Hangman figure and allows them to play again. 
end

%citation for the fun fact: Hangman. (n.d.). Retrieved December 06, 2020, from https://wiki.kidzsearch.com/wiki/Hangman

































