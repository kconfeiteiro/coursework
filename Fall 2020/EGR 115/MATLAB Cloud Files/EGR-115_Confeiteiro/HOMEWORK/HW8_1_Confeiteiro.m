% -----------------------------------------------------------------------
% Program Number: HW 8 Part 1
% Program Purpose: Use randomly generated integers do and determine and sum
% of the differences between them and output them.
%
% Created By: Krystian Confeiteiro
% Created On: 10/19/20
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

%% with traversing (loops)
%generate the random integers
v = randi(15, 1, randi([3,8]));

%find difference of each element in order 
sumV = 0;
for k = 2:length(v)
    differenceT = abs(v(k)-v(k-1)); 
    sumV = sumV+differenceT;
end

%out locations visited and total distance travelled 
fprintf('\nThe locations you visited where  ');
for l = 1:length(v)
    fprintf('%d  ',v(l));
end
fprintf('\nand the total distance travelled was %d miles.\n\n',sumV);


%% without traversing

%calculate the distance walked 
distance = sum(abs(v(1:end-1)-v(2:end)));

%out locations visited and total distance travelled 
fprintf('\nThe locations you visited where  ');
for l = 1:length(v)
    fprintf('%d  ',v(l));
end
fprintf('\nand the total distance travelled was %d miles.\n\n',sumV);

