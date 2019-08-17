function watermark = jpeg_lbs_extract(picture, key)
key_file = fopen(key, 'r');
key_text = fscanf(key_file,'%f');
x = key_text(1)
y = key_text(2)
watermark_size = key_text(3)
picture = jpeg_read(picture);
coef_arrays = picture.coef_arrays;
y_channel = coef_arrays{1};
string = []
for i = 1:watermark_size
    byte = 0;
    for j = 1:8
        disp([(i-1)*8 + (j-1) + x, y])
        bit = mod(y_channel((i-1)*8 + (j-1) + x, y), 2);
        byte = byte*2 + bit;
    end
    byte = char(byte)
    string = [string, [byte]]
end
watermark = string
end