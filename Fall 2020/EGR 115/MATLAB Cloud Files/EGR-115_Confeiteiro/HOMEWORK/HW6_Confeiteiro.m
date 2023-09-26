% -----------------------------------------------------------------------
% Program Number: Homework #6
% Program Purpose: Create various arrays based on the homework PDF

% Created By: Krystian Confeiteiro 
% Created On: 10/05/20
% Last Modified On: 10/05/20
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

%% problem 1
prob1 = [8,(10/4),12*14,52,tand(85),sqrt(26),0.15];

%% problem 2 
prob2 = [((sqrt(15))*(10^3)),(25/(14-6^2)),(log(35)/0.4^3),(sind(65)/cosd(80)),(cos(pi/20)^2)];
 
%% problem 3
prob3 = [25.5;(14*tand(28))/(2.1^2+11);factorial(6);(2.7)^3;0.0375;(pi/5)];

%% problem 4
prob4 = [(32/3.2^2);(sind(35))^2;6.1;log(29^2);0.00552;(log(29))^2;133];

%% problem 5
x = 0.85;
y = 12.5;
prob5 = [y;y^x;log(y/x);x*y;x+y];

%% problem 6
a = 3.5;
b = -6.4;
prob6 = [a,a^2, a/b, a*b, sqrt(a)];

%% problem 7
prob7 = [1:6:43];

%% problem 8
prob8 = linspace(98,2,11);

%% problem 9
prob9 = [26:-3.6:-10]';

%% problem 10
prob10 = linspace(-34,-7,9)';

%% problem 11 FIX
prob11 = [1:0:5];
prob11(1:5)=5

%% problem 12
prob12 = linspace(9,9,9);

%% problem 13
prob13 = [zeros(1,6) ,4.7];

%% problem 14
prob14 = [zeros(1,5),ones(1,3)*3.8];

%% problem 15
prob15 = [0:2:12,9:-3:0];

%% problem 16
a = 2:3:17;
b = 3:4:15;
prob16 = [a,b];

%% problem 17 FIX
a = [2:3:17]';
b = [3:4:15]';
prob17 = [a;b];

%% problem 18 FIX
prob18a = [8:7:71];
%prob18b = [prob18a(1,3),prob18a(end-3,:)];

%% problem 19
prob19 = [5:4:49];
prob19a = prob19(:,2:2:end); %even index
prob19b = prob19(:,1:2:end); %odd index

%% problem 20
prob20 = [0:3:27];
prob20a = prob20(end:-1:1); %reversed

%% problem 21
prob21 = [130:-20:10;linspace(1,12,7);12:10:72];

%% problem 22
prob22 = [linspace(5,3,3);linspace(5,3,3);linspace(5,3,3)];

%% problem 23
prob23 = [ones(1,5)*7;ones(1,5)*7];

%% problem 24
prob24 = [zeros(1,4),8;zeros(1,4),7;zeros(1,4),6];

%% problem 25
prob25 = [zeros(1,5);zeros(1,5);zeros(1,2),5:-1:3;zeros(1,2),2:-1:0];

%% problem 26 FINISH
%prob26 = [zeros(1,5);zeros(1,2),1:10:20;zeros(1,2),

%% problem 27 
a27 = [3,-1,5,11,-4,2];
b27 = [7,-9,2,13,1,-2];
c27 = [-2,4,-7,8,0,9];

prob27a = [a27(1,:);b27(1,:);c27(1,:)];
prob27b = [a27(1,:);b27(1,:);c27(1,:)]';

%% problem 28
a28 = [3,-1,5,11,-4,2];
b28 = [7,-9,2,13,1,-2];
c28 = [-2,4,-7,8,0,9]; 

prob28a = [a28(1,end-3:end);b28(1,end-3:end);c28(1,end-3:end)];
prob28b = [a28(1,1:3);b28(1,1:3);c28(1,1:3)];

%% problem 29
a29 = [3,9,-0.5,3.6,1.5,-0.8,4];
b29 = [12,-0.8,6,2,5,3,-7.4];

prob29a = [a29(1,3:6);a29(1,4:7);b29(1,2:5)];
prob29b = [a29(1,2:7);b29(1,1:3),b29(1,5:7)];

%% problem 30
a30 = [36:-2:26;24:-2:14;12:-2:2];

prob30a = a30(2,:);
prob30b = a30(:,6);
prob30c = [a30(3,1:2),a30(1,3:end)];

%% problem 31 
a31 = [1:1:18];
b31 = reshape(a31,[3,6]);

prob31a = [b31(:,1),b31(:,3),b31(:,5)];
prob31b = [b31(2,2:5),b31(:,3)'];
prob31c = [b31(1,3:5),b31(3,2:4)];

%% problem 32
c32 = [1.5:0.5:5;9.6:-0.5:6.1];
d32 = reshape(c32,[4,4]);

prob32a = [d32(1,:),d32(3,:)]';
prob32b = [d32(:,2);d32(:,4)]';
prob32c = [d32(1,1:2),d32(2,2:end),d32(4,1:3)];

%% problem 33
%e33 = [0,zeros(1,5)+5; 0.1:0.2:0.9; 12:-3:-3; 6:1:11]

%prob33a = [e33()

%% problem 34

%% problem 35
prob34a = [ones(2,2),zeros(2,2)];
prob34b = [eye(2,2),zeros(2,2),ones(2,2)];
prob34c = [ones(1,4);zeros(2,4)];
prob34d = [eye(2,2),ones(2,2),zeros(2,1)];
prob34e = [ones(2,4);eye(2,2),zeros(2,2)];
prob34f = [zeros(2,1),ones(2,3),zeros(2,1);zeros(2,4),ones(2,1)];

%% problem 36
a = eye(2,2);
b = ones(2,2);
c = zeros(2,2);

prob36 = [a(),b(),c();c(),b(),a()];

%% problem 37 NOT SURE HOW TO COMPLETE
a37 = ones(2,3)







