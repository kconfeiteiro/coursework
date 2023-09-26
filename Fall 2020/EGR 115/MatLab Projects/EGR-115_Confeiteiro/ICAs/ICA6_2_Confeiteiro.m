% -----------------------------------------------------------------------
% Program Number: ICA6 Question 2
% Program Purpose: To tell the user what SPF to use given their skin tone,
% duration of the event.
%
% Created By: Krystian Confeitiero 
%
% Created On: 09/15/20
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

%Prompt for indoor/outdoor, skin tone, start/end time
InOrOut = input('\nWill this event be indoor[1] or outdoors[2]?: ');
skinTone = input('\nWhat kind of skin tone do you have? (Very fair[1], fair[2], light[3], medium[4] or dark[5]): ');
startTime = input('\nWhat time will this event start? (military time): ');
endTime = input('What time will this event end? (military time): ');


%Calculate the duration of the event
eventTime = (endTime-startTime);

%Indoor/outdoor
if InOrOut == 1 %indoor 
    fprintf('\nBecause the event is indoors, you do not need to wear any suncreen. \n');
else %outdoor
    if eventTime == 1 
        if skinTone == 1 %very fair
            fprintf('It is reccomend you apply 30 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 2 %fair
            fprintf('It is reccomend you apply 15 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 3 %light
            fprintf('It is reccomend you apply 15 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 4 %medium 
            fprintf('It is reccomend you apply 8-14 SPF every two hours to ensure adequate protection. \n');
        else skinTone == 5 %dark
            fprintf('It is reccomend you apply 8-14 SPF every two hours to ensure adequate protection. \n');
        end                    
    elseif eventTime == 2
        if skinTone ==1 %very fair
            fprintf('It is reccomend you apply 30 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 2 %fair
            fprintf('It is reccomend you apply 30 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 3 %light
            fprintf('It is reccomend you apply 30 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 4 %medium
            fprintf('It is reccomend you apply 15 SPF every two hours to ensure adequate protection. \n');
        else %dark
            fprintf('It is reccomend you apply 8-14 SPF every two hours to ensure adequate protection. \n');
        end  
    elseif eventTime == 3
        if skinTone == 1 %very fair
            fprintf('It is reccomend you apply 50+ SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 2 %fair
            fprintf('It is reccomend you apply 50+ SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 3 %light
            fprintf('It is reccomend you apply 30 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 4 %medium
            fprintf('It is reccomend you apply 15 SPF every two hours to ensure adequate protection. \n');
        else  %dark
            fprintf('It is reccomend you apply 15 SPF every two hours to ensure adequate protection. \n');
        end  
    elseif eventTime == 4
        if skinTone ==1 %very fair
            fprintf('It is reccomend you apply 50-100 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 2 %fair
            fprintf('It is reccomend you apply 50+ SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 3 %light
            fprintf('It is reccomend you apply 30 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 4 %medium
            fprintf('It is reccomend you apply 30 SPF every two hours to ensure adequate protection. \n');
        else skinTone == 5 %dark
            fprintf('It is reccomend you apply 15 SPF every two hours to ensure adequate protection. \n');
        end  
    else eventTime == 5 %eventTime>=5
        if skinTone ==1 %very fair
            fprintf('It is reccomend you apply 50-100 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 2 %fair
            fprintf('It is reccomend you apply 50-100 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 3 %light
            fprintf('It is reccomend you apply 50-100 SPF every two hours to ensure adequate protection. \n');
        elseif skinTone == 4 %medium
            fprintf('It is reccomend you apply 50+ SPF every two hours to ensure adequate protection. \n');
        else skinTone == 5 %dark
            fprintf('It is reccomend you apply 26 SPF every two hours to ensure adequate protection. \n');
        end  
    end
end

























