A = fix(255 * rand(16))
[u, s ,v] = svd(A);
sa_max = max(max(s))
pepper_noise = imnoise(A, 'salt & pepper');
A = A + 8*pepper_noise;
[u, s, v] = svd(A);
sb_max = max(max(s))
h = hist(A)