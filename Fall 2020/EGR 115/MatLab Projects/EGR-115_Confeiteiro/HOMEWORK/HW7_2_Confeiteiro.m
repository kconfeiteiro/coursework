% -----------------------------------------------------------------------
% Program Number: HW 7 NUM 2
% Program Purpose: Look at vectors, find the months above average, 

% Created By: Krystian Confeiteiro
% Created On: 10/12/20
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

%define BOS and SEA vectors (inches)
BOS = [2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93];
SEA = [6.83, 3.69, 7.20, 2.68, 2.05, 3.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.84];


%display months, and inches of rain
fprintf('\n\t\t\tPRECIPITATION EACH MONTH (INCHES)\n\nJAN\tFEB\tMAR\tAPR\tMAY\tJUN\tJUL\tAUG\tSEP\tOCT\tNOV\tDEC');
fprintf('\n---------------------------------------------------------------------------------------------\n\n');
for m = 1:length(BOS)
    fprintf('%.02f\t',BOS(m));
end
fprintf('\n\n');
for p = 1:length(SEA)
    fprintf('%.02f\t',SEA(p));
end
fprintf('\n\n---------------------------------------------------------------------------------------------\n\n\n');

%find total and average pricipitation for each city
    %totals
BOStotal = sum(BOS, 'all');
SEAtotal = sum(SEA, 'all');

    %averages
BOSavg = mean(BOS, 'all');
SEAavg = mean(SEA, 'all');


%number of months precipitation was above average/below in each city
    % boston
count1=0; %count for above average
count2=0; %count for below avearge
for k = 1:length(BOS)
    if BOS(k)>BOSavg
        count1=count1+1; %count above avg
    else
        count2=count2+1; %count below avg
    end
end

    % seattle
count3=0; %count for above average
count4=0; %count for below average
for n = 1:length(SEA)
    if SEA(n)>SEAavg
        count3=count3+1; %count above avg
    else
        count4=count4+1; %count below avg
    end
end

%output # of months each city had higher than avg and the total and average
fprintf('\n\nSTATS:\n------\n');

fprintf('\nBostons''s average precipitation: %.02f inches\nSeattle''s average precipitation: %.02f inches',BOSavg,SEAavg);
fprintf('\n\nBoston''s total precipitation for the year: %.02f inches\nSeattle''s total precipitation for the year: %.02f inches\n\n',BOStotal,SEAtotal);


%months precipitation was higher in boston compared to seattle
if count1>count3
    fprintf('Out of the 12 months, Boston had %d months with higher than average precipitation compared to Seattle''s %d months.\n\n',count1,count3);
else
    fprintf('Out of the 12 months, Seattle had %d months with higher than average precipitation compared to Boston''s %d months.\n\n',count3,count1);
end
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
