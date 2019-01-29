clc
%input data from file
filename = ('RowingInputData.xlsx');
testData = xlsread(filename)

%----asignment fis-------
clc
a = newfis('assignment');

%----inputs--------------

%catch 
a = addvar(a, 'input', 'Catch Angle (degrees)', [55 70]);
%finish angle
a = addvar(a, 'input', 'Finish Angle (degrees)', [35 48]);
%max force angle
%a = addvar(a, 'input', 'Peak Force Angle (degrees)', [0 100]);
%force 
%a = addvar(a, 'input', 'Peak Force (Newtons)', [0 80]);
%Power
a = addvar(a, 'input', 'Power (Watts)', [130 490]);
%Power @ 22
%a = addvar(a, 'input', 'Power @ r22(Watts)', [130 320]);
%Power @ 34
%a = addvar(a, 'input', 'Power @ r34(Watts)', [210 500]);
%rating
a = addvar(a, 'input', 'Rating (Stroke/Minute)', [17 34]);
%weight
a = addvar(a, 'input', 'Weight (kg)', [55 100]);

%-----input variables-------------------
%catch variables
a = addmf(a, 'input', 1, 'Novice', 'trapmf', [0 55 60.5 61]);
a = addmf(a, 'input', 1, 'Intermediate', 'gaussmf', [0.7 62.1]);
a = addmf(a, 'input', 1, 'National', 'gaussmf', [0.7 64.8]);
a = addmf(a, 'input', 1, 'International', 'trapmf', [66 67.4 70 70]);
%finish angle
a = addmf(a, 'input', 2, 'Novice', 'trapmf', [0 35 38 39]);
a = addmf(a, 'input', 2, 'Intermediate', 'gaussmf', [0.8 40.25]);
a = addmf(a, 'input', 2, 'National', 'gaussmf', [0.8 42.5]);
a = addmf(a, 'input', 2, 'International', 'trapmf', [43.5 45 48 48]);
%peak force angle

%power
%a = addmf(a, 'input', 3, 'Lwt Women', 'trimf', [140 206 274]);
%a = addmf(a, 'input', 3, 'Opem Women', 'trimf', [157 246 335]);
%a = addmf(a, 'input', 3, 'Lwt Men', 'trimf', [196 293 390]);
%a = addmf(a, 'input', 3, 'Opem Men', 'trimf', [210 349 490]);

a = addmf(a, 'input', 3, 'Low', 'trapmf', [130 130 170 180]);
a = addmf(a, 'input', 3, 'Medium Low', 'gaussmf', [18 202]);
a = addmf(a, 'input', 3, 'Medium High', 'gaussmf', [18 267]);
a = addmf(a, 'input', 3, 'High Low', 'gaussmf', [18 332]);
a = addmf(a, 'input', 3, 'High', 'gaussmf', [18 397]);
a = addmf(a, 'input', 3, 'Very High', 'trapmf', [430 440 490 490]);


%Power @ 22
%a = addmf(a, 'input', 4, 'Novice', 'trapmf', [130 130 175 210]);
%a = addmf(a, 'input', 4, 'Intermediate', 'trapmf', [154 189 209 243]);
%a = addmf(a, 'input', 4, 'National', 'trapmf', [169 213 233 276]);
%a = addmf(a, 'input', 4, 'Inernational', 'trapmf', [183 247 320 320]);

%Power @ 34
%a = addmf(a, 'input', 5, 'Novice', 'trapmf', [210 210 280 342]);
%a = addmf(a, 'input', 5, 'Intermediate', 'trapmf', [236 304 324 391]);
%a = addmf(a, 'input', 5, 'National', 'trapmf', [255 337 357 440]);
%a = addmf(a, 'input', 5, 'Inernational', 'trapmf', [274 381 500 500]);

%rating
a = addmf(a, 'input', 4, 'Low', 'trapmf', [0 17 21.5 22]);
a = addmf(a, 'input', 4, 'Medium', 'gaussmf', [1 24]);
a = addmf(a, 'input', 4, 'High', 'trapmf', [26 28 34 34]);
%a = addmf(a, 'input', 4, 'Very High', 'trapmf', [36 38 40 40 ]);

%wieght
a = addmf(a, 'input', 5, 'Lwt Women', 'trapmf', [55 55 59 62.5]);
a = addmf(a, 'input', 5, 'Lwt Men', 'trimf', [70 72.5 75]);
a = addmf(a, 'input', 5, 'Open Women', 'gaussmf', [3.5 70]);
a = addmf(a, 'input', 5, 'Open Men', 'trapmf', [75 95 100 100]);

%----------------outputs-----------------
a = addvar(a, 'output', 'Quality of Rowing(%)', [0 100]);
%----------------outputs varibles--------
a = addmf(a, 'output', 1, 'Novice', 'gaussmf', [10 0]);
a = addmf(a, 'output', 1, 'Intermediate', 'gaussmf', [8 40]);
a = addmf(a, 'output', 1, 'National', 'gaussmf', [8 60]);
a = addmf(a, 'output', 1, 'International', 'gaussmf', [10 100]);

%--------i i i i i o w o
%rules for the catch and finish
%if catch or finish is good
rule1 =  [1 0 0 0 0 1 0.25 1];
rule2 =  [2 0 0 0 0 2 0.25 1];
rule3 =  [3 0 0 0 0 3 0.25 1];
rule4 =  [4 0 0 0 0 4 0.25 1];
rule5 =  [0 1 0 0 0 1 0.25 1];
rule6 =  [0 2 0 0 0 2 0.25 1];
rule7 =  [0 3 0 0 0 3 0.25 1];
rule8 =  [0 4 0 0 0 4 0.25 1];
%catch and wieght (extremes) 
%lwt women (women are shorter, less catch and reach)
%--------C F P R W o w o
rule9 = [3 0 0 0 1 4 0.25 1];
rule10 =[0 3 0 0 1 4 0.25 1];
%open weight men (men are taller easier to get longer catch and reach,
%novice mens are punish more for having a good bad catch
rule11 =[2 0 0 0 4 1 0.25 1];
rule12 =[0 2 0 0 4 1 0.25 1];
rule13 =[1 0 0 0 4 1 1 1];
rule14 =[0 1 0 0 4 1 1 1];

%lwt Women
rule15 = [0 0 1 1 1 2 1 1];
rule16 = [0 0 1 2 1 1 1 1];
rule17 = [0 0 2 1 1 4 1 1];
rule18 = [0 0 2 2 1 3 1 1];
rule19 = [0 0 2 3 1 2 1 1];
rule20 = [0 0 3 0 1 4 0.5 1];

%lwt men
rule21 = [0 0 1 0 3 1 0.5 1];

rule22 = [0 0 2 1 3 2 0 1];
rule49 = [0 0 2 2 3 2 0 1];

rule23 = [0 0 3 1 3 3 0.5 1];
rule24 = [0 0 3 2 3 1 0 1];
rule25 = [0 0 3 3 3 1 1 1];

rule26 = [0 0 4 1 3 4 0.5 1];
rule27 = [0 0 4 2 3 4 0.5 1];
rule28 = [0 0 4 3 3 3 0.5 1];

%open women
rule29 = [0 0 1 0 2 1 0.5 1];
rule30 = [0 0 1 1 2 2 1 1];
rule48 = [0 0 1 2 2 1 1 1];

rule31 = [0 0 2 1 2 4 0.5 1];
rule32 = [0 0 2 2 2 2 1 1];
rule33 = [0 0 2 3 2 1 1 1];

rule34 = [0 0 3 1 2 4 1 1];
rule35 = [0 0 3 2 2 4 0 1];
rule36 = [0 0 3 3 2 4 0.5 1];

%open men 
rule37 = [0 0 1 0 4 1 1 1];

rule38 = [0 0 2 1 4 2 1 1];
rule39 = [0 0 2 2 4 1 1 1];
rule40 = [0 0 2 3 4 1 1 1];

rule41 = [0 0 3 1 4 3 1 1];
rule42 = [0 0 3 2 4 1 1 1];
rule43 = [0 0 3 3 4 1 1 1];

rule44 = [0 0 4 1 4 4 1 1];
rule45 = [0 0 4 2 4 4 0.25 1];
rule46 = [0 0 4 3 4 3 1 1];

rule47 = [0 0 5 3 4 4 0.5 1];

%then rules

%or rules
%--------i i i i i o w o


%adding rules to fis
%making array
ruleList = [rule1; rule2; rule3; rule4;...
            rule5; rule6; rule7; rule8;...
            rule9; rule10; rule11; rule12;...
            rule13; rule14; rule15; rule16;...
            rule17; rule18; rule19; rule20;...
            rule21; rule22; rule23; rule24;...
            rule25; rule26; rule27; rule28;...
            rule29; rule30; rule31; rule32;...
            rule33; rule34; rule35; rule36;...
            rule37; rule38; rule39; rule40;...
            rule41; rule42; rule43; rule44;...
            rule45; rule46; rule47; rule48; rule49
];
a = addrule(a,ruleList);
rules = showrule(a)

%defuzzification method
a.defuzzMethod = 'mom';

%loops through test data and outputs
for i=1:size(testData,1)
        eval = evalfis([testData(i, 1), testData(i, 2), testData(i, 3), testData(i, 4), testData(i, 5)], a);
        fprintf('%d) Catch Angle: %.2f, Finish Angle: %.2f, Power: %.2f, Rating: %.2f, Weight: %.2f  => Out: %.2f \n\n',i,testData(i, 1),testData(i, 2),testData(i, 3),testData(i, 4),testData(i, 5), eval);  
        %xlswrite('output.xls', eval, 1, sprintf('E%d',i+1));
end



%-----------plotting the inputs----------
figure(1)
subplot(6,1,1), plotmf(a, 'input', 1)
subplot(6,1,2), plotmf(a, 'input', 2)
subplot(6,1,3), plotmf(a, 'input', 3)
subplot(6,1,4), plotmf(a, 'input', 4)
subplot(6,1,5), plotmf(a, 'input', 5)
subplot(6,1,6), plotmf(a, 'output',1) 