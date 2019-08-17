function watermark = watermark_spreading_extract(picture, key)
picture_map = load_pic(picture);
[picture_width, picture_height, picture_channel] = size(picture_map);
key_file = fopen(key, 'r');
key_text = fscanf(key_file,'%f');
%  [x, y, watermark_size, spread_times, x0, u0, QIM_step, message_size, num_zero]
x = key_text(1);
y = key_text(2);
watermark_size = key_text(3);
spread_times = key_text(4);
x0 = key_text(5);
u0 = key_text(6);
QIM_step = key_text(7);
message_size = key_text(8);
num_zero = key_text(9);
% message_size = watermark_size * 8 * spread_times;
message_extract = [];
col = 0;
row = y;
%disp('x')
%disp(x+col)
%disp('y')
%disp(row)
for i = 1:message_size
    value_extract = QIM_decode(picture_map(x+col, row), QIM_step);
    message_extract = [message_extract, value_extract];
    row = row + 1;
    if row  == picture_width
        col = col + 1;
        row = 1;
    end
end
%disp('x')
%disp(x+col)
%disp('y')
%disp(row)
message_extract = haming_decode(message_extract, num_zero);
false_random_list = random_list(spread_times, x0, u0);
new_random_list = [];
for i = 1:watermark_size*8
	new_random_list = [new_random_list, false_random_list];
end 
spreading_list = xor(new_random_list, message_extract);
watermark_extract = [];
for i  = 1:watermark_size
    watermark_byte = 0;
    for j = 1:8
        watermark_bit = 0;
        for k = 1:spread_times
            watermark_bit = watermark_bit + spreading_list((i-1)*8*spread_times+(j-1)*spread_times+k);
        end
        watermark_bit = round(watermark_bit/spread_times);
        watermark_byte = watermark_byte*2+watermark_bit;
    end
    watermark_byte;
    watermark_byte = char(watermark_byte);
    watermark_extract = [watermark_extract, watermark_byte];
end
watermark = watermark_extract;
fclose(key_file);
end