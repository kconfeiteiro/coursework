function [circumference,area] = ovalCal(a,b)
% Purpose:
% syntax: [circumference,area] = ovalCal(intA,intB)
% Input variables:
% a: major axis of the ellipse
% b: minor axis of the ellipse
%
% Output variables:
% circumference: the circumference of the ellipse
% area: the area of the ellipse
%
% Created By: Krystian Confeiteiro
% Section #: 10
% Created On: 10/20/20
% Last Modified On:
%
% Credit to: the Smart Dude
% By submitting this program with my name, I affirm that the creation and
% modification of this program is primarily my own work.
% Comments:
% -------------------------------------------
% NO clear;clc;close all

%calculate the circumference of the ellipse
circumference = pi*(3*(a+b)-sqrt((3*a+b)*(a+3*b)));

%calculate the area of the ellipse
area = pi*a*b;
end