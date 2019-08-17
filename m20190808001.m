picture = imread('test.jpg');
[w, h, c] = size(picture)

subplot(3,1,1);
h_r = imhist(picture(:,:,1));
plot(h_r);
title('red');

subplot(3,1,2);
h_g = imhist(picture(:,:,2));
plot(h_g);
title('green');

subplot(3,1,3);
h_b = imhist(picture(:,:,3));
plot(h_b);
title('blue');
