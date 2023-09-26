% -----------------------------------------------------------------------
% Program Number: ICA 16
% Program Purpose: Match user input with array element and print respective
% grades

% Created By:  Krystian Confeiteiro
% Created On: 10/27/20
% Last Modified On: ~

% Credit To:
% By submitting this program with my name, I affirm that the creation and
% modifications of this program is primarily my own work.
%
% Comments:
% -----------------------------------------------------------------------

clc
clear
close all


%load data
load grades;

%prompt for choice, 1 for name and 2 for ID; validate the choice
choice = str2double(input('\nChoose to enter your name(1) or ID(2): ','s'));
while isnan(choice) || choice>2 || choice<1 || mod(choice,1)~=0
    choice = input('Error, enter ''1'' for name and ''2'' for ID: ','s');
end

IDcolumn = grades(2:end,2);
namesColumn = grades(2:end,1);
rowFound = [];
if choice == 1 %if 1 for name
    name = input('Enter your name: ','s'); %prompt for name
    %look for the row that has a matching name
    for k = 1:length(namesColumn(:,1))
        isName = strcmpi(name,namesColumn{k,1});
        if isName == 1
            rowFound = [k];
        end
    end
else % if 2 for ID
    %prompt for ID and validate for number
    inputID = input('Enter your ID: ');
    while isempty(inputID) || isnan(inputID)
        inputID = fprintf('Error, please re-enter your ID: ');
    end
    
    %look for row that has a matching ID
    for k = 1:length(namesColumn(:,1))
        if inputID == IDcolumn{k,1}
            rowFound = [k];
        end
    end
end
fprintf('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n');  
fprintf('Your exam grades: ');
    if isempty(rowFound) %row not found
        %print failure message
        fprintf('\nError, name not found');
    else %row found
        %slice out 4 exam grades
        examVec = cell2mat(grades(rowFound+1,3:end));
        
        %print 4 exam grades
        for m = 1:length(examVec)          
            fprintf('%d  ',examVec(m));
        end
        
        %print mean grade
        examMean = mean(examVec);
        fprintf('\nand your grade average is %.01f%%.\n\n',examMean);
    end







