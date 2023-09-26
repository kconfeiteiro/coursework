%pH ranges

%Prompt for pH
pH = input('Enter the pH value: ');

%Check pH >7, =7, or <7 and print a message
if pH>7 %basic
    fprintf('It''s Basic.\n');
elseif pH==7 %neutral 
    fprintf('It''s neutral.\n');
else %ph<7, acidic
    fprintf('It''s acidic.\n');
end

