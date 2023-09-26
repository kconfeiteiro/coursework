% -----------------------------------------------------------------------
% Program Number: HW 10 #1
% Program Purpose: Look through excel sheet, plot the graph of the inputed
% name's popularity through the years 

% Created By: Krystian Confeiteiro 
% Created On: 11/07/20
% Last Modified On: 11/08/20            

% Credit To: 
% By submitting this program with my name, I affirm that the creation and 
% modifications of this program is primarily my own work.
%
% Comments:
% -----------------------------------------------------------------------

clc
clear 
close all

%read excel sheet 
[~,~,rawData] = xlsread('BabyNames.xlsx');

%data prep
namesColumn = rawData(2:end,1);
yearRow = cell2mat(rawData(1,3:end));
genderColumn = rawData(2:end,2);
nameDataArray = rawData(2:end,3:end);

%% split section so xlsread doesn't have to run everytime
%input for baby name, gender then validate
moreOrNo = 'y';
while (~strncmpi(moreOrNo,'n',1))
    %input for the name and validate
    nameInput = input('Enter a name: ','s');
    while isempty(nameInput) || isnumeric(nameInput) 
        nameInput = input('Error, enter a name: ','s');
    end
    
    %input for the gender and validate
    genderInput = input('Enter the babie''s gender (M/F): ','s');
    while isempty(genderInput) || isnumeric(genderInput) || (~strncmpi(genderInput,'m',1) && ~strncmpi(genderInput,'f',1)) 
        genderInput = input('Error, enter the babie''s gender (M/F): ','s');
    end
        %look through excell sheet for match
    for k = 1:length(namesColumn)
        if strcmpi(nameInput,namesColumn{k,:}) && strncmpi(genderInput,genderColumn{k,:},1)
            rowFound = k;
            finalNamesData = cell2mat(nameDataArray(rowFound,:));
            fprintf('The record is found for %s (%s).',namesColumn{rowFound},upper(genderColumn{rowFound}));
        end
    end
    
    %replace any zeros with a 1001 for the proper range
    for m = 1:length(finalNamesData)
        if finalNamesData(m) == 0
            finalNamesData(m) = 1001;
        end
    end
    
     %set graph parameters and plot graph, set parameters, label axis', label title
    plot(yearRow,finalNamesData,'bo-');
    if strncmpi(genderInput,'f',1) %if genderInput is f or female
        title(['Popularity of the name ',namesColumn{rowFound},' for baby girls, from 1890-2010']); %title for girls
    else %if genderInput is m or male
        title(['Popularity of the name ',namesColumn{rowFound},' for baby boys, from 1890-2010']); %title for boys
    end
    xlabel('Decade');
    ylabel('Ranking (1-1000) where 1 means the most popular');
    set(gca,'yDir','reverse'); %reverse y-axis
    set(gca,'yTick',0:100:1000); %y-axis range 
    set(gca,'ylim',[0,1000]); %y-axis limit
    
    %ask if they want to keep searching for names or to quiz and validate
    moreOrNo = input('\n\nWould you like to search again? (y/n): ','s');
    while isempty(moreOrNo) || (~strncmpi(moreOrNo,'n',1) && ~strncmpi(moreOrNo,'y',1))
        moreOrNo = input('Error, would you like to search again? (y/n): ','s');
    end
    if strncmpi(moreOrNo,'n',1)
        fprintf('\nThanks for using the program! Bye!\n');
    end
end