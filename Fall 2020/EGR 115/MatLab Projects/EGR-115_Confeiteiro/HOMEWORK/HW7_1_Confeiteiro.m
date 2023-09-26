% -----------------------------------------------------------------------
% Program Number: HW 7 NUM 1
% Program Purpose: Get inputed grades from user and calculate final grade.

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

%find number of quiz grades, n
nQuizGrades = input('Enter the number of Quiz grades you have: ');
while isempty(nQuizGrades) || nQuizGrades<=5 || nQuizGrades>=10
   nQuizGrades = input('Error, enter the amount of Quiz grades you have (5-10): '); 
end
fprintf('\n');

%input the quiz grades
quizArray = [];
for k = 1:nQuizGrades
    fprintf('Please enter your grade for Quiz #%.0f (out of 10): ',k);
    quizGrades = input('');
    while isempty(quizGrades) || quizGrades<0 || quizGrades>100 || mod(quizGrades,1)~=0
        fprintf('Error, enter your grade for Quiz #%.0f (out of 10): ',k);
        quizGrades = input('');
    end
    quizArray(end+1)=quizGrades;
end
fprintf('\n');

%calculate quiz grades out of 10
quizAvg = (sum(quizArray)-min(quizArray))/(nQuizGrades-1);


%input final exam and midterm grades
count1 = 4;
midtermTotal = 0;
midtermArray = [];
for m = 1:count1
    fprintf('Please enter your grade for Midterm #%.0f (0-100): ',m);
    midtermGrades = input('');
    while isempty(midtermGrades) || midtermGrades<=0 || midtermGrades>100 %validation for midterms
        fprintf('Error, re-enter your grade for Midterm #%.0f: ', m);
        midtermGrades = input('');
    end
    midtermArray(end+1)=midtermGrades;
end
fprintf('\n');

finalexamGrade = input('Please enter your grade for the final exam: ');
while isempty(finalexamGrade) || finalexamGrade<=0 || finalexamGrade>100 %validation for final exam grade
    finalexamGrade = input('ERROR - Please enter your grade for the final exam: ');
end
fprintf('\n');

%calculate midterm avg
midtermAvg = mean(midtermArray,'all');

%weighted averages
if midtermAvg>finalexamGrade
    finalGrade = (.3*(quizAvg/10))+((.5*midtermAvg)/100)+(.2*finalexamGrade/100);
else
    finalGrade = (.3*(quizAvg/10))+((.2*midtermAvg)/100)+(.5*finalexamGrade/100);
end
finalGrade = 100*finalGrade;

%gradeLetter
if finalGrade>=90
    gradeLetter = 'A';
elseif finalGrade>=80
    gradeLetter = 'B';
elseif finalGrade>=70
    gradeLetter = 'C';
elseif finalGrade>=60
%     gradeLetter = 'D';
else %finalGrade>
    gradeLetter = 'F';
end

%print quiz, midterm, and final grade(s) arrays
fprintf('------------------------------------------------------------------\nQuiz Grades:\t')
for q=1:nQuizGrades
    fprintf('%.0f/10\t',quizArray(q));
end
fprintf('\nMidterm grades:\t');
for m=1:count1
    fprintf('%.0f/100\t',midtermArray(m));
end
fprintf('\nFinal exam grade: %.02f',finalexamGrade);

%output final grade and letter grade
fprintf('\n\nYour final grade is %.02f%% \nYou will recieve a %s.\n',finalGrade,gradeLetter);