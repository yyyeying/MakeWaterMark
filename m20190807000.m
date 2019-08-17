x = [];
x0 = rand
x = [x, [x0]];
u0 = 3.5699456;
u = u0 + (4-u0)*rand
for i = 1:9
    newx = u*x(i)*(1-x(i));
    x = [x, [newx]];
end
x