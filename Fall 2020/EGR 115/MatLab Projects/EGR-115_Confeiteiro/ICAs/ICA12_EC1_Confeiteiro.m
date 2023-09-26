% -----------------------------------------------------------------------
% Program Number: ICA 12 Extra Credit 1
% Program Purpose: Collect n quiz grades from user, validate, and store
% grades
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

%input quiz grades from user and count quizzes entered
quizCount=0;
for k = 1:length(quizGrade)
    quizInput(k) = input('Please enter a quiz grade: \n');
    while isempty(quizInput(k)) || mod(quizInput(k),1)~=0 %validation
        quizInput(k) = input('Invalid grade, please enter a positive grade number: \n');
    end 
    quizCount=quizCount+1;
    fprintf('\nHere are the %.0f quiz grade(s) entered: \n%.0f',quizCount,quizGrades);
end





