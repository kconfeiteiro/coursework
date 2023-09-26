% -----------------------------------------------------------------------
% Program Number: Modeling Problem Code submission
% Program Purpose: Predict transportation of students

% Created By:  Krystian Confeiteiro
% Created On:  11/13/20
% Last Modified On: 11/15/20

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
[~,~,rawData] = xlsread('TravelMode_Studentdata.xlsx');

%data preparation
campusColumn = rawData(2:end,3);
roomatesColumn = rawData(2:end,6);
carColumn = rawData(2:end,7);
bikeLockColumn = rawData(2:end,11);
boardColumn = rawData(2:end,13);


%input if student is on or off campus
campusOrNo = input('Do you live on campus? (yes/no): ','s');
while isempty(campusOrNo) || (~strncmpi(campusOrNo,'yes',1) && ~strncmpi(campusOrNo,'no',1)) || isnumerical(campusOrNo)
    campusOrNo = input('Error, Do you live on campus? (yes/no): ','s');
end
if strncmpi(campusOrNo,'yes',1) %if studentCampus == yes
    %input for if they have roomates
    roomatesOrNo = input('Do you have roomates? (yes/no): ','s');
    while isempty(roomatesOrNo) || (~strncmpi(roomatesOrNo,'yes',1) && ~strncmpi(roomatesOrNo,'no',1)) || isnumerical(roomatesOrNo)
        roomatesOrNo = input('Error, Do you live on campus? (yes/no): ','s');
    end
    if strncmpi(roomatesOrNo,'yes',1) %if they do have roomates
        %input if they own a bike
        bikeOrNo = input('Do you have a bike? (yes/no): ','s');
        if strncmpi(bikeOrNo,'yes',1) %if they do own a bike
            %input if the bike is registered
            registerOrNo = input('Is the bike registered? (yes/no): ','s');
            while isempty(registerOrNo) || (~strncmpi(registerOrNo,'yes',1) && ~strncmpi(registerOrNo,'no',1)) || isnumeric(registerOrNo)
                registerOrNo = input('Error, Is the bike registered? (yes/no): ','s');
            end
            if strncmpi(registerOrNo,'yes',1) %if the bike is registered
                %input if they have a bike lock
                lockOrNo = input('Do you have a bike lock? (yes/no): ','s');
                if strncmpi(lockOrNo,'no',1) %if they don't have a bike lock
                    %input if they want to buy a bike lock
                    lockWant = input('Do you want to purchase a lock? (yes/no): ','s');
                    while isempty(lockWant) || (~strncmpi(lockWant,'yes',1) && ~strncmpi(lockWant,'no',1)) || isnumeric(lockWant)
                        lockWant = input('Error, Do you want to purchase a lock? (yes/no): ','s');
                    end
                    if strncmpi(lockWant,'yes',1) %if they do
                        %print: the user will bike
                        fprintf('The user will bike.');
                    else %else (they do not)
                        %input if they will rent one
                        rentOrNo = input('Do you want to rent a lock? (yes/no): ','s');
                        while isempty(rentOrNo) || (~strncmpi(rentOrNo,'yes',1) && ~strnmpi(rentOrNo,'no',1)) || isnumeric(rentOrNo)
                            rentOrNo = input('Error, Do you want to rent a bike lock? (yes/no): ','s');
                        end
                        if strncmpi(rentOrNo,'no',1) %if they don’t
                            %input if they have board
                            boardOrNo = input('Do you have a skate/long board? (yes/no): ','s');
                            while isempty(boardOrNo) || (~strncmpi(boardOrNo,'yes',1) && ~strncmpi(boardOrNo,'no',1)) || isnumeric(boardOrNo)
                                boardOrNo = input('Error, Do you have a skate/long board? (yes/no): ','s');
                            end
                            if strncmpi(boardOrNo,'yes',1) %if yes
                                %print: they will use board
                                fprintf('The user will bike.');
                                %else
                            else
                                %print: they will walk
                                fprintf('The user will walk.');
                            end
                        else %else (they do not want to rent one)
                            %input if they have a board
                            boardOrNo2 = input('Do you have a skate/long board? (yes/no)','s');
                            while isempty(boardOrNo2) || (~strncmpi(boardOrNo2,'yes',1) && ~strcmpi(boardOrNo2,'no',1)) || isnumeric(boardOrNo2)
                                boardOrNo2 = input('Error, Do you have a short/long board? (yes/no): ','s');
                            end
                            if strncmpi(boardOrNo2,'no',1)%if they don’t have a board
                                %print: they will walk
                                fprintf('The user will walk.');
                            else %else (they do have board)
                                %print: they will user board
                                fprintf('The user will use a skate/long board.');
                            end
                        end
                    end
                end
            else %else (bike is not registered)
                %input if they have a board
                boardOrNo3 = input('Do you have a skate/long board? (yes/no): ','s');
                while isempty(boardOrNo3) || (~strncmpi(boardOrNo3,'yes',1) && ~strncmpi(boardOrNo3,'no',1)) || isnumeric(boardOrNo3)
                    boardOrNo3 = input('Error, do you have a skate/long board? (yes/no): ','s');
                end
                if strncmpi(boardOrNo3,'yes',1) %if they do
                    %print: the user will board
                    fprintf('The user will use a skate/long board.');
                else %else (they do not have board)
                    %print: the user will walk
                    fprintf('The user will walk.');
                end
            end
        end
    else %else (don’t have roomates)
        %input if they have a car
        carOrNo1 = input('Do you have a car? (yes/no): ','s');
        while isempty(carOrNo1) || (~strncmpi(carOrNo1,'yes',1) && ~strncmpi(carOrNo1,'no',1)) || isnumeric(carOrNo1)
            carOrNo1 = input('Error, do you have a car? (yes/no): ','s');
        end
        if strncmpi(carOrNo1,'yes',1) %if they do have a car
            %input if it is registered
            isRegistered = input('Is the car registered? (yes/no): ','s');
            while isempty(isRegistered) || (~strncmpi(isRegistered,'yes',1) && ~strncmpi(isRegistered,'no',1)) || isnumeric(isRegistered)
                isRegistered = input('Error, is your car registered? (yes/no): ','s');
            end
            if strncmpi(isRegistered,'yes',1) %if yes
                %print: the user will drive
                fprintf('The user will drive.');
            else %else (not registered)
                %input if they have a parking pass or want to buy one
                buyPass = input('Do you want to purcahse a parking pass? (yes/no): ','s');
                while isempty(buyPass) || (~strncmpi(buyPass,'yes',1) && ~strncmpi(buyPass,'no',1)) || isnumeric(buyPass)
                    buyPass = input('Error, do you want to purchase a parking pass? (yes/no): ','s');
                end
                if strncmpi(buyPass,'yes',1) %if they do
                    %print: the user will drive
                    fprintf('The user will drive.');
                end
            end
        end
        %else (they do not own bike)
        %input if they have a board
    else %else (do not live on campus)
        %input how far they are from campus
        howFar = str2double(input('How far away do you live off campus?: ','s'));
        while isnan(howFar) || mod(howFar,1)~=0
            howFar = str2double(input('Error, how far away do you live off campus?: ','s'));
        end
        if howFar >= 5 %if the distance is > 5 miles
            %input if they have a friend with a car
            friendWithCar = input('Do you have a friend with a car? (yes/no): ','s');
            while isempty(friendWithCar) || (~strncmpi(friendWithCar,'yes',1) && ~strncmpi(friendWithCar,'no',1)) || isnumeric(friendWithCar)
                friendWithCar = input('Error, do you have a friend with a car? (yes/no): ','s');
            end
            if strncmpi(friendWithCar,'yes',1) %if they do have a friend with a car
                %Print: The user will carpool to campus
                fprintf('The user will carpool to campus.');
            else %else (they do not have a friend with car)
                %Print: The user will use public transportation
                fprintf('The user will use public transportation.');
            end %end
        else %else (distance <= 5 miles)
            %Input if they own a car
            carOrNo = input('Do you own a car? (yes/no): ','s');
            while isempty(carOrNo) || (~strncmpi(carOrNo,'yes',1) && ~strncmpi(carOrNo,'no',1)) || isnumeric(carOrNo)
                carOrNO = input('Error, do you own a car? (yes/no): ','s');
            end
            if strncmpi(carOrNo,'yes',1) %if they do own a car
                %Input if they have a parking pass
                passOrNo = input('Do you have a parking pass? (yes/no): ','s');
                while isempty(passOrNo) || (~strncmpi(passOrNo,'yes',1) && ~strncmpi(passOrNo,'no',1)) || isnumeric(passOrNo)
                    passOrNo = input('Error, do you have a parking pass? (yes/no): ','s');
                end
                if strncmpi(passOrNo,'no',1) %if they do not
                    %Input if they do want a parking pass
                    passWant = input('Do you want a parking pass? (yes/no): ','s');
                    while isempty(passWant) || (~strncmpi(passWant,'yes',1) && ~strncmpi(passWant,'no',1)) || isnumeric(passWant)
                        passWant = input('Error, do you want a parking pass? (yes/no): ','s');
                    end
                    if strncmpi(passWant,'no',1) %If they do not want one
                        %Input do if they have a friend with car
                        friendWithCar2 = input('Do you have a friend with a car? (yes/no): ','s');
                        while isempty(friendWithCar2) || (~strncmpi(friendWithCar2,'yes',1) && ~strncmpi(friendWithCar2,'no',1)) || isnumeric(friendWithCar2)
                            friendWithCar2 = input('Error, do you have a friend with a car? (yes/no): ','s');
                        end
                        if strncmpi(friendWithCar2,'yes',1) %if yes
                            %Print: The user will carpool
                            fprintf('The user will carpool.');
                        else %else (they do not)
                            %input if they have a bike
                            bikeOrNo2 = input('Do you have a bike? (yes/no): ','s');
                            while isempty(bikeOrNo2) || (~strncmpi(bikeOrNo2,'yes',1) && ~strncmpi(bikeOrNo2,'no',1)) || isnumeric(bikeOrNo2)
                                bikeOrNo2 = input('Error, do you have a bike? (yes/no): ','s');
                            end
                            if strncmpi(bikeOrNo2,'yes',1) %if they do
                                %print: user will bike
                                fprintf('The user will bike.');
                            else %else (no bike)
                                %print: user will walk
                                fprintf('The user will bike.');
                            end
                        end
                    end
                else %else (they do want parking pass)
                    %Print: The user will drive
                    fprintf('The user will drive.');
                    %end
            else %else (they do not own a car)
                %Input if they have a friend with a car
                friendWithCar3 = input('Do you have a friend with a car? (yes/no): ','s');
                while isempty(friendWithCar3) || (~strncmpi(friendWithCar3,'yes',1) && ~strncmpi(friendWithCar3,'no',1)) || isnumeric(friendWithCar3)
                    friendWithCar3 = input('Error, do you have a friend with a car? (yes/no): ','s');
                end
                if strncmpi(friendWithCar3,'yes',1) %if they do have a friend with a car
                    %Print: The user will carpool
                    fprintf('The user will carpool.');
                end
                end
            end
        end
    end
end
