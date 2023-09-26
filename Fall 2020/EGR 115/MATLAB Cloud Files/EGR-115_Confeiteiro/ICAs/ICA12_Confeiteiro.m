% -----------------------------------------------------------------------
% Program Number: ICA 12 
% Program Purpose: Determine BMI for random heights and weigths and ouput
% them in an array
%
% Created By: Krystian Confeiteiro
% Created On: 10/08/20
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

%generate Nrandom, randomWeights, and randomheights
Nsample = randi([10,40]);
weightPounds = randi([100,200],Nsample, 1);
heightInches = randi([60,80],Nsample,1);

%calculate BMI via element-by-element math
BMI = (703*weightPounds./(heightInches.^2));

%print title for chart
fprintf('\nMass(lb)   Height(inch)     \t BMI   \t\tCategory');
fprintf('\n--------   ------------         -------        -----------');

%traverse loop
count = 0;
for  k = 1:length(BMI)
    if BMI(k)<15.5 %underweight
        category = 'Underweight'; 
    elseif BMI(k)<25 %normal
        category = 'Normal';
        count=count+1; %count normal 
    elseif BMI(k)<30 %overweight
        category = 'Overweight';
    else %obese
        category = 'Obese';
    end
    fprintf('\n\n %.0f\t\t%.0f\t\t%.02f\t\t%s',weightPounds(k),heightInches(k),BMI(k),category);
end

%output final message (percentage normal out of n participants)
percentageNormal = (count/Nsample)*100;
fprintf('\n\n-------------------------------------------------------------------------------\n');
fprintf('Out of the %d subjects, %.02f%% of them were of normal weight.\n\n',Nsample, percentageNormal);