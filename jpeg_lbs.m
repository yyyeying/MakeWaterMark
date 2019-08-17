function [picture, key_path] = jpeg_lbs(cover_file, watermark)
watermark_file = fopen(watermark, 'r');
watermark_text = fread(watermark_file)
watermark_size = size(watermark_text)
watermark_size = watermark_size(1)
cover = jpeg_read(cover_file)
x = fix((cover.image_width - watermark_size * 8) * rand)
y = fix(cover.image_height * rand)
position = [x, y, watermark_size];
key = num2str(position);
key_path = 'key.txt'
key_file = fopen(key_path, 'w');
fprintf(key_file, '%s', key);
coef_arrays = cover.coef_arrays;
y_channel = coef_arrays{1};
for i = 1:watermark_size
    for j = 1:8
        y_channel((i-1)*8 + (j-1) + x, y) = y_channel((i-1)*8 + (j-1) + x, y) - mod(y_channel((i-1)*8 + (j-1) + x, y), 2) + bitget(watermark_text(i), 9 - j);
    end
end
picture = 'lbs.jpg'
coef_arrays{1} = y_channel;
cover.coef_arrays = coef_arrays;
jpeg_write(cover, picture)
end