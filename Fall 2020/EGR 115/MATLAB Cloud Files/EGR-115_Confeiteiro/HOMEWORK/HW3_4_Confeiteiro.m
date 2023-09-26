% -----------------------------------------------------------------------
% Program Number: Homework #3 Part 4
% Program Purpose:
% Created By: Krystian Confeiteiro 
%
% Created On: 09/14/20
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


%Welscome prompt
fprintf('**********Welcome to Project Planning!**********\n');

%Prompt for name
name = input('\nWhat is your name? ', 's');

%Prompt for length, width of room, and width of door (feet)
Roomlength = input(['\nHi ' name ', \nPlease enter the length of your room in feet: ']);
RoomWidth = input('\nPlease enter the width of the room in feet: ');
DoorWidth = input('\nPlease enter the width of the door in feet: ');

%Calculate the size of the room
RoomSize = Roomlength*(RoomWidth+DoorWidth);

%Calulate the number of wood plank covers needed
WoodPlanks = ceil((RoomSize/(23.17))+(RoomSize*.10));

%Calcualte the number of baseboards needed
Baseboards = ceil(((Roomlength*RoomWidth)/16)+((Roomlength*RoomWidth)*(.05))) ;

%Calculate labor costs
PlankLaborCosts = (2*RoomSize);
BoardLaborCosts = (1*Baseboards);


%Display all the costs, materials,
fprintf('\nThe size of your room is %.02f sqft.\n', RoomSize);
fprintf('Each case of wood planks covers 23.17 sqft, you will need %d cases. \nThe labor will cost $%.02f. ', WoodPlanks, PlankLaborCosts);
fprintf('Each baseboard covers 16ft, you will need %d pieces of baseboards. \nThe labor will cost $%.02f. \n', Baseboards, BoardLaborCosts); 













