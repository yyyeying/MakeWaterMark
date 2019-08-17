function [list, x0, u] = random_list(length, x00, u00)
x = [];
x0 = x00;
if x00 == 2
    x0 = rand;
end
x = [x, x0]; 
u0 = 3.5699456;
u = u00;
if u00 == 5
    u = u0 + (4-u0)*rand;
end
for i = 1:(length-1)
    newx = u*x(i)*(1-x(i));
    x = [x, newx];
end
list = round(x);
end