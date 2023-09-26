% -----------------------------------------------------------------------
% Program Number: ICA 13
% Program Purpose: Logical operators

% Created By: Krystian Confeiteiro 
% Created On: 10/15/20
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

%hardcode gradebook
gradebook = [82 2; 83 1; 100 2; 83 1; 75 1;97 1; 76 1;71 2;97 1; 84 2;71 1; 86 1;78 2];

%find the # of females who recieved an A, find the percentage
femaleA = sum((gradebook(:,1)>90) & gradebook(:,2)==1);
percentageFemale = (femaleA/sum(gradebook(:,2)==1))*100;

%find the # of males who received an A, find the percentage
maleA = sum((gradebook(:,1)>90) & gradebook(:,2)==2);
percentageMale = (maleA/sum(gradebook(:,2)==2))*100;

%find the indicies of who recieved and A and save it to a vector 
vectorA = find(gradebook(:,1)>90);

%print % of females and males that recived an A & total students that
%recieved an A
fprintf('\nOut of the entire class, %.0f%% males and %.0f%% females recived A''s.\n\nStudents that recieved an A:\t',percentageMale,percentageFemale);
for k = 1:length(vectorA)
    fprintf('%d\t',vectorA(k)); %print the students that recieved an A
end
fprintf('\n\n');