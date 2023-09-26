function [h,m,s] = sec2hms(seconds)
% Purpose: Convert inputed seconds to HH MM SS format 
% syntax: [h,m,s] = sec2hms(seconds)
% Input variables:
% seconds = the amount of seconds the user wants to convert
%
% Output variables:
% h: total hours
% m: reamining minutes
% s: remaining seconds
%
% Created By: Krystian Confeiteiro
% Section #: 10
% Created On: 10/20/20
% Last Modified On: ~
%
% Credit to: the Smart Dude
% By submitting this program with my name, I affirm that the creation and
% modification of this program is primarily my own work.
% Comments:
% -------------------------------------------
% NO clear;clc;close all


%calculate hours, minutes, and seconds
h = floor(seconds*(1/3600)); %full hours
m = floor(mod(seconds,3600)/60); %full minutes from the remaining seconds
s = mod(seconds,60); %remaining seconds after full hours & full minutes
end